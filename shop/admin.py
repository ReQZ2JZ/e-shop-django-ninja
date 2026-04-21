from django.contrib import admin
from .models import VideoCard, Cart, Order, OrderItem


@admin.register(VideoCard)
class VideoCardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "created_at")
    search_fields = ("name",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "qty", "created_at")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "total", "created_at")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product_name", "qty", "price")