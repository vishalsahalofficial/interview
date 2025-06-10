from django.urls import path
from .views import ApartmentListCreateView, ApartmentRetrieveUpdateDestroyView

urlpatterns = [
    path('apartments/', ApartmentListCreateView.as_view(), name='apartment-list-create'),
    path('apartments/<int:pk>/', ApartmentRetrieveUpdateDestroyView.as_view(), name='apartment-detail'),
]
