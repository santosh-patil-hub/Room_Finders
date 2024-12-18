
from django.urls import path
from apps.room.api import views

urlpatterns = [
    path('', views.index, name='room_index'),  # Define your app's views
    # Add other paths specific to the room app here
]
