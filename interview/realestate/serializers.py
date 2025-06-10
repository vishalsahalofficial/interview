from rest_framework import serializers
from .models import Apartment
# from .serializers import ApartmentSerializer


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
