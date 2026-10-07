from django.shortcuts import render, get_object_or_404
from .models import Category, Dish


def home(request):
    featured = Dish.objects.filter(is_featured=True, is_available=True)[:6]
    categories = Category.objects.all()
    return render(request, "menu/home.html", {
        "featured": featured,
        "categories": categories,
    })


def menu_list(request):
    categories = Category.objects.all()
    return render(request, "menu/menu_list.html", {"categories": categories})


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, "menu/dish_detail.html", {"dish": dish})