from django.contrib import admin
from .models import Product,Order,OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "total_price", "created_at")
    inlines = [OrderItemInline]
admin.site.register(Product)