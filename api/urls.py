from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView, ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('', include(router.urls)),
]
