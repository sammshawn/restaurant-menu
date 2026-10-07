from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order")
    list_editable = ("display_order",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available", "is_featured", "is_vegetarian")
    list_filter = ("category", "is_available", "is_featured", "is_vegetarian")
    search_fields = ("name", "description")
    list_editable = ("is_available", "is_featured")