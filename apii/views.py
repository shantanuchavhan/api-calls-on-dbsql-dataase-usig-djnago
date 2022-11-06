from django.shortcuts import render
from rest_framework import viewsets
from apii.models import book
from apii.serializers import bookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class bookViewSet(viewsets.ModelViewSet):
    queryset= book.objects.all()
    serializer_class=bookSerializer
    
    #companies/{companyId}/emplyees
   


