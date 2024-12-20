from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

# Register your models on the admin sections
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
