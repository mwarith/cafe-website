from django.contrib import admin
from .models import Order, OrderItem, PointTransaction

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'points_earned')
    inlines = [OrderItemInline]

@admin.register(PointTransaction)
class PointTransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'points', 'transaction_type')