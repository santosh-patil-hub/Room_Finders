"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# RoomFindersBackend/urls.py
from django.contrib import admin
from django.urls import path, include  # include() is used to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include URLs from all apps
    path('room/', include('apps.room.urls')),  # Include URLs from the room app
    path('custom_user/', include('apps.custom_user.urls')),  # Include URLs from the custom_user app
    path('category/', include('apps.category.urls')),  # Include URLs from the category app
    path('comment/', include('apps.comment.urls')),  # Include URLs from the comment app
    path('bookmark/', include('apps.bookmark.urls')),  # Include URLs from the bookmark app
    path('location/', include('apps.location.urls')),  # Include URLs from the location app
]
