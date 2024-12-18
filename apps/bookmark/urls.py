
from django.urls import path
from apps.bookmark.api import views

urlpatterns = [
    path('', views.bookmarks, name='bookmarks'),  # Define your app's views
    # Add other paths specific to the room app here
]
