from django.contrib import admin
from store.models import Product, Category, Gallery, Specific, Size, Color

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0

class SpecificInline(admin.TabularInline):
    model = Specific
    extra = 0

class SizeInline(admin.TabularInline):
    model = Size
    extra = 0

class ColorInline(admin.TabularInline):
    model = Color
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'stock_qty', 'in_stock', 'vendor', 'featured']
    list_editable = ['featured']
    list_filter = ['category', 'date']  
    search_fields = ['title']
    inlines = [GalleryInline, SpecificInline, SizeInline, ColorInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
