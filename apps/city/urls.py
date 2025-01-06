from django.urls import path
from apps.city.api.views import CityListView

urlpatterns = [
    path('cities/', CityListView.as_view(), name='city-list'),
]
