from rest_framework import generics, status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


def _extract_error_message(detail):
    if isinstance(detail, dict):
        first_value = next(iter(detail.values()), "An error occurred")
        return _extract_error_message(first_value)
    if isinstance(detail, list):
        first_item = detail[0] if detail else "An error occurred"
        return _extract_error_message(first_item)
    return str(detail)


class StandardizedResponseMixin:
    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        response.data = {
            "status": "error",
            "message": _extract_error_message(response.data),
        }
        return response


class OrderListCreateView(StandardizedResponseMixin, generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        user_id = self.request.query_params.get('user')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            "status": "success",
            "data": response.data,
        }
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "status": "error",
                    "message": _extract_error_message(serializer.errors),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "status": "success",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
