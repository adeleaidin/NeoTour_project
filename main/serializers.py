from rest_framework import serializers
from .models import Tour, Category, Review, Booking
import re

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class PhoneValidator:
    def __init__(self, country_code='+996'):
        self.country_code = country_code

    def __call__(self, value):
        pattern = r'^\+996\d{9}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(f'Invalid phone number. It should start with {self.country_code} and have 12 digits.')

class BookingSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[PhoneValidator()])

    class Meta:
        model = Booking
        fields = '__all__'
