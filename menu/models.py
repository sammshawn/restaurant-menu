from django.db import models


class Category(models.Model):
    """A menu category like Starters, Main Dishes, Drinks."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Dish(models.Model):
    """A single menu item."""

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="dishes/", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category__display_order", "name"]
        verbose_name_plural = "Dishes"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def formatted_price(self):
        return f"KES {self.price:,.0f}"