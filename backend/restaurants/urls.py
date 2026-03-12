from django.urls import path

from .views import AllergyCheckView, MenuItemListView, RestaurantListView


urlpatterns = [
    path('check-allergy/', AllergyCheckView.as_view(), name='check-allergy'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:restaurant_id>/menu/', MenuItemListView.as_view(), name='restaurant-menu-items'),
]
