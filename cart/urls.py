from django.urls import path, include
from .views import *
from rest_framework import routers


app_name = 'cart'

router = routers.DefaultRouter()
router.register('add-item', CartViewSet, basename='additemcart')
router.register('view-cart', ViewCartViewSet, basename='viewcart')


urlpatterns = [
    path('', include(router.urls)),
    path('edit-cart/<int:pk>/', EditCartView.as_view(), name='update-cart'),
]
