from django.shortcuts import render
from rest_framework import viewsets
from .models import Property, Tenant, RentalPayment
from .serializers import PropertySerializer, TenantSerializer, RentalPaymentSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    
    serializer_class = PropertySerializer
    
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    
    filterset_fields = ['property_type', 'rental_cost']
    ordering_fields = ['name', 'rental_cost']
