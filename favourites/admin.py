""" Favourites Admin """
from django.contrib import admin
from .models import Favourites


class FavouritesAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = ('username',)
    search_fields = ('username',)
    list_filter = ('username',)


admin.site.register(Favourites, FavouritesAdmin)
