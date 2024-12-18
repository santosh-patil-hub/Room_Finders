
from django.urls import path
from apps.category.api import views

urlpatterns = [
    path('', views.categories, name='categories'),  # Define your app's views
    # Add other paths specific to the room app here
]
