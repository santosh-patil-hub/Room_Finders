from rest_framework.views import APIView
from rest_framework.response import Response
from apps.city.models import City
from .serializers import CitySerializer

# List all cities or search by name
class CityListView(APIView):
    def get(self, request):  # sourcery skip: use-named-expression
        search_query = request.query_params.get('q', None)
        
        if search_query:
            cities = City.objects.filter(name__icontains=search_query)
        else:
            cities = City.objects.all()

        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
