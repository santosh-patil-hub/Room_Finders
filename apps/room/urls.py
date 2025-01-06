from django.urls import path
from apps.room.api.views import RoomCreateView, RoomUpdateView, RoomDeleteView

urlpatterns = [
    path('rooms/create/', RoomCreateView.as_view(), name='room-create'),  # Create room
    path('rooms/<int:pk>/', RoomUpdateView.as_view(), name='room-update'),  # Update room
    path('rooms/<int:pk>/', RoomDeleteView.as_view(), name='room-delete'),  # Delete room
]
