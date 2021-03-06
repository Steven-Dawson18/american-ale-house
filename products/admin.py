"""Products admin"""
from django.contrib import admin


from .models import Product, Category, ReviewRating

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'image',
        'added_date',
    )

    ordering = ('added_date',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewRating)
