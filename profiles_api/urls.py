from django.urls import path, include, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

router.register('profiles', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello'),
    path('', include(router.urls)),

]
