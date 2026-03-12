from django.urls import path

from .views import AllergyCheckView, MenuItemListView, RestaurantListView, SafeMenuView, SearchMenuView


urlpatterns = [
    path('check-allergy/', AllergyCheckView.as_view(), name='check-allergy'),
    path('search-menu/', SearchMenuView.as_view(), name='search-menu'),
    path('safe-menu/<int:user_id>/<int:restaurant_id>/', SafeMenuView.as_view(), name='safe-menu'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:restaurant_id>/menu/', MenuItemListView.as_view(), name='restaurant-menu-items'),
]
