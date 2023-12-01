from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ReviewViewSet, CategoryViewSet
from .services.flash_sale import FlashSaleListCreateView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),

]