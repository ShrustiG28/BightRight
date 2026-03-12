from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MenuItem, Restaurant
from .recommendation_service import generate_recommendations
from .serializers import MenuItemSerializer, RestaurantSerializer
from users.models import UserProfile


class StandardizedResponseMixin:
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        detail = response.data
        if isinstance(detail, dict):
            detail = next(iter(detail.values()), "An error occurred")
        if isinstance(detail, list):
            detail = detail[0] if detail else "An error occurred"
        response.data = {
            "status": "error",
            "message": str(detail),
        }
        return response


class RestaurantListView(StandardizedResponseMixin, generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "status": "success",
            "data": response.data,
        }
        return response


class MenuItemListView(StandardizedResponseMixin, generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(restaurant_id=self.kwargs["restaurant_id"])

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "status": "success",
            "data": response.data,
        }
        return response


class AllergyCheckView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        menu_item_id = request.data.get("menu_item_id")

        try:
            user = UserProfile.objects.get(id=user_id)
            menu_item = MenuItem.objects.get(id=menu_item_id)
        except UserProfile.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except MenuItem.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "Menu item not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        user_allergies = [item.strip() for item in user.allergies.split(",") if item.strip()]
        ingredients = [item.strip() for item in menu_item.ingredients.split(",") if item.strip()]
        has_risk = detect_allergy_risk(user_allergies, ingredients)

        if has_risk:
            return Response(
                {
                    "status": "success",
                    "allergy_risk": True,
                    "message": "This dish may contain ingredients you are allergic to",
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "status": "success",
                "allergy_risk": False,
            },
            status=status.HTTP_200_OK,
        )


class SafeMenuView(APIView):
    def get(self, request, user_id, restaurant_id):
        try:
            user = UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        menu_items = MenuItem.objects.filter(restaurant_id=restaurant_id)
        user_allergies = [item.strip() for item in user.allergies.split(",") if item.strip()]

        safe_menu_items = []
        for menu_item in menu_items:
            ingredients = [item.strip() for item in menu_item.ingredients.split(",") if item.strip()]
            has_risk = detect_allergy_risk(user_allergies, ingredients)
            if not has_risk:
                safe_menu_items.append(
                    {
                        "id": menu_item.id,
                        "name": menu_item.name,
                        "price": menu_item.price,
                        "diet_tags": menu_item.diet_tags,
                        "ingredients": menu_item.ingredients,
                    }
                )

        return Response(
            {
                "status": "success",
                "safe_menu_items": safe_menu_items,
            },
            status=status.HTTP_200_OK,
        )


class SearchMenuView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        if not query:
            return Response(
                {
                    "status": "error",
                    "message": "Search query is required",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) | Q(ingredients__icontains=query)
        )

        results = [
            {
                "id": menu_item.id,
                "name": menu_item.name,
                "price": menu_item.price,
                "diet_tags": menu_item.diet_tags,
                "ingredients": menu_item.ingredients,
            }
            for menu_item in menu_items
        ]

        return Response(
            {
                "status": "success",
                "results": results,
            },
            status=status.HTTP_200_OK,
        )


class RecommendationView(APIView):
    def get(self, request, user_id, restaurant_id):
        mood = request.GET.get("mood")
        time_of_day = request.query_params.get("time")
        try:
            user = UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            return Response(
                {
                    "status": "error",
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        menu_items = MenuItem.objects.filter(restaurant_id=restaurant_id)
        recommended = generate_recommendations(user, menu_items, mood, time_of_day)

        return Response(
            {
                "status": "success",
                "recommended_items": recommended,
            },
            status=status.HTTP_200_OK,
        )
