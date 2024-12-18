
from django.urls import path
from apps.comment.api import views

urlpatterns = [
    path('', views.comments, name='comments'),  # Define your app's views
    # Add other paths specific to the room app here
]
