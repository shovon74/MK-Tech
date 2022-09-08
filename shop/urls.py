from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.Productview)
router.register('users', views.Userview)
router.register('createusers', views.CreateUserview)

urlpatterns = [
    path('', include(router.urls)),
]