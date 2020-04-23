from django.contrib import admin
from market.models import Category, Item, Stock, MyBug


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quanity')


class StockAdmin(admin.ModelAdmin):
    list_display = ('administrator', 'item', 'name')


class MyBugAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'name')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Stock, StockAdmin)
admin.site.register(MyBug, MyBugAdmin)
