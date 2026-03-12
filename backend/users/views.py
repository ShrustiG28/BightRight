from rest_framework import generics, status
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer


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
        message = _extract_error_message(response.data)
        response.data = {
            "status": "error",
            "message": message,
        }
        return response


class UserListCreateView(StandardizedResponseMixin, generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

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


class UserDetailView(StandardizedResponseMixin, generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data = {
            "status": "success",
            "data": response.data,
        }
        return response
