from django.urls import path

from .views import MenuItemListView, RestaurantListView


urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:restaurant_id>/menu/', MenuItemListView.as_view(), name='restaurant-menu-items'),
]
