from rest_framework.views import APIView
from rest_framework.response import Response
from apps.category.models import Category
from .serializers import CategorySerializer

class CategoryListView(APIView):
    def get(self, request):  # sourcery skip: use-named-expression
        search_query = request.query_params.get('q', None)
        
        if search_query:
            categories = Category.objects.filter(name__icontains=search_query)
        else:
            categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
