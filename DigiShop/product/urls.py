from product.views import *
from django.urls import path

urlpatterns = [
    path('products/search/', search),
    path('latest-products/', LatestProductsList.as_view()),
    path('products/<slug:category_slug>/', CategoryDetailView.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>',
         ProductDetailView.as_view()),
]
