from rest_framework.generics import UpdateAPIView
from .serializers import RoomUpdateSerializer
from rest_framework.views import APIView
from .serializers import RoomCreateSerializer
from ..models import Room
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .serializers import RoomDeleteSerializer

class RoomCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can create rooms

    def post(self, request):
        serializer = RoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": "Room created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Room creation failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)




class RoomUpdateView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        room = self.get_object()
        serializer = RoomUpdateSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Room updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Room update failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class RoomDeleteView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDeleteSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        room = self.get_object()
        room.delete()
        return Response({
            "message": "Room deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
