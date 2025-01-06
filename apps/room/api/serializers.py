from rest_framework import serializers
from ..models import Room
from apps.category.models import Category  # Import the Category model
from apps.city.models import City  # Import the City model
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth import get_user_model

User = get_user_model()  # Resolve the custom user model



class RoomCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # Validating that at least 3 images are provided

    class Meta:
        model = Room
        fields = [
            'id', 'title', 'description', 'location', 'floor', 'landmark',
            'address', 'area', 'category', 'city', 'user', 'facilities',
            'allowable_in_room', 'light_responsibility', 'image1', 'image2',
            'image3', 'image4', 'image5'
        ]

class RoomUpdateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    
    class Meta:
        model = Room
        fields = [
            'title', 'description', 'location', 'floor', 'landmark',
            'address', 'area', 'category', 'city', 'facilities',
            'allowable_in_room', 'light_responsibility', 'image1', 'image2',
            'image3', 'image4', 'image5'
        ]
        
class RoomDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id']
