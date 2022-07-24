from django.contrib import admin
from .models import *

class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'firm', 'mark', 'slug', 'photo', 'price', 'year', 'distance', 'power', 'transmission', 'fuel', 'time_create', 'content', 'is_published', 'shops')
    list_display_links = ('id', 'firm', 'time_create')
    search_fields = ('firm', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("firm", "mark", "year", "shops", "distance")}


class ShopsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'slug', 'content')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Auto, AutoAdmin)
admin.site.register(Shops, ShopsAdmin)