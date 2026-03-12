from rest_framework import generics

from .models import MenuItem, Restaurant
from .serializers import MenuItemSerializer, RestaurantSerializer


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
