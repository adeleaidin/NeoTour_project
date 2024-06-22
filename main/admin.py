from django.contrib import admin
from main.models import Booking, Category, Review, Tour
# Register your models here.

admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(Review)