from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'rating',
        'has_sizes',
        'image',
        'date_added'
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
