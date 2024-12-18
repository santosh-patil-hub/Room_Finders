
from django.urls import path
from apps.location.api import views

urlpatterns = [
    path('', views.location, name='room_location'),  # Define your app's views
    # Add other paths specific to the room app here
]
