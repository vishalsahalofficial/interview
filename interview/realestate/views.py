from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Apartment
from .serializers import ApartmentSerializer

class ApartmentListCreateView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'rent': ['gte', 'lte'],
        'bedrooms': ['in'],
        'city': ['icontains']
    }
    ordering_fields = ['posted_date', 'rent']
    ordering = ['-posted_date']

class ApartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
