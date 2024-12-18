
from django.urls import path
from apps.city.api import views

urlpatterns = [
    path('', views.citys, name='citys'),  # Define your app's views
    # Add other paths specific to the room app here
]
