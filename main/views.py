from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Tour, Booking
from .serializers import TourListSerializer, TourDetailSerializer, CategorySerializer, ReviewSerializer, BookingSerializer
from .filters import DiscoveryTourFilter, RecommendTourFilter
from .pagination import CustomPagination


class TourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = DiscoveryTourFilter
    serializer_class = TourListSerializer

# class DiscoveryTourListAPIView(generics.ListAPIView):
#     queryset = Tour.objects.all()
#     serializer_class = TourListSerializer


class RecommendTourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.exclude(season__isnull=True).order_by('season')
    serializer_class = TourListSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = RecommendTourFilter



class TourDetailAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
