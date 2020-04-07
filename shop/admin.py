from django.contrib import admin
from .models import Category, Product, ProductImage, CustomerQuestions


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


@admin.register(CustomerQuestions)
class CustomerQuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerQuestions._meta.fields]

    class Meta:
        model = CustomerQuestions
