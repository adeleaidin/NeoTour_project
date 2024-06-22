from django.urls import path
from . import views

urlpatterns = [
    path('booking-create/', views.BookingCreateAPIView.as_view(), name='booking-create'),
    path('recommend-tours/', views.RecommendTourListAPIView.as_view(), name='recommend-tour-list'),
    path('tour-detail/<int:pk>/', views.TourDetailAPIView.as_view(), name='tour-detail'),
    path('tours-list/', views.TourListAPIView.as_view(), name='tour-list'),

]
