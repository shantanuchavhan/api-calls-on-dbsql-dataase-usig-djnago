from django.contrib import admin
from django.urls import path,include
from apii.views import bookViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'books', bookViewSet)


urlpatterns = [    
    path('',include(router.urls))
      
]