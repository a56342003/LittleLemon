from django.contrib import admin
from .models import Booking, Menu
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'bookingDate')
    list_filter = ('name',)
    search_fields = ['name']

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    list_filter = ('title',)
    search_fields = ['title']

admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)