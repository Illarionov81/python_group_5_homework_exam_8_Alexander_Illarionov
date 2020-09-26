from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('pk', 'name', 'category', )
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('pk', 'author', 'product', 'mark',)
    list_display_links = ('pk', 'author',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
