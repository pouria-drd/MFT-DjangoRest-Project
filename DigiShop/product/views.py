from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product, Category
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer, CategorySerializer


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        product = self.get_object(category_slug)
        serializer = CategorySerializer(product)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        product = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
