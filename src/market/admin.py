from django.contrib import admin
from market.models import Category, Item, Stock, MyBug, Administrator, Customer


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quanity')


class StockAdmin(admin.ModelAdmin):
    list_display = ('administrator', 'item', 'name')


class MyBugAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'name')


class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('user', 'registrated_at')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'registrated_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Stock, StockAdmin)
admin.site.register(MyBug, MyBugAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Customer, CustomerAdmin)
