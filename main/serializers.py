from rest_framework import serializers
from .models import Tour, Category, Review, Booking
import re

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'review',
            'nickname',
            'photo',
        ]

class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            'id',
            'image',
            'title',
        ]

class TourDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = [
            'id',
            'title',
            'image',
            'description',
            'reviews',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "tour",
            "num_people",
            "phone_number",
            "additional_comments"
        ]

    def validate_phone_number(self, value):
        pattern = r"^\+996\d{9}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                {
                    "error": "Invalid phone number. It should start with +996 and have 12 digits."
                }
            )

        return value
    def validate_num_people(self, value):
        if value < 1 or value > 6:
            raise serializers.ValidationError(
                {
                    "error": "Number of people must be between 1 and 6."
                }
            )
        return value


