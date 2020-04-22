from django.contrib import admin
from market.models import Category, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quanity')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
