from django.contrib import admin
from .models import Product, Category, Review


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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Displays the fields and values
    for Review model in admin panel.
    """
    list_display = ('username', 'message', 'product', 'created_on')
    search_fields = ['username', 'created_on']
    list_filter = ['created_on']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
