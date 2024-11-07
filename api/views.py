from django.shortcuts import render
from rest_framework import generics
from portfolio.models import Category, Portfolio
from .serializers import CategorySerializer, PortfolioSerializer




class CategoryApiView(generics.ListAPIView):
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer
    
    
    

class PortfolioApiView(generics.ListAPIView):
    queryset =  Portfolio.objects.all()
    serializer_class = PortfolioSerializer