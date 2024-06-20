from rest_framework import generics, status
from .models import Tour, Category, Review, Booking
from .serializers import TourSerializer, CategorySerializer, ReviewSerializer, BookingSerializer
from rest_framework.response import Response

class DiscoveryTourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.filter(category__is_discovery=True)
    serializer_class = TourSerializer

class RecommendTourListAPIView(generics.ListAPIView):
    queryset = Tour.objects.exclude(season__isnull=True).order_by('season')
    serializer_class = TourSerializer

class TourCategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TourDetailAPIView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number', '')
        if not phone_number.startswith('+996'):
            phone_number = '+996' + phone_number.lstrip('0')
        request.data['phone_number'] = phone_number

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
