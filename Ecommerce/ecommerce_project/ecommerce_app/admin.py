from django.contrib import admin
from .models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cname','slug']
    prepopulated_fields = {'slug':('cname',)}
admin.site.register(Category,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pname','slug','price','available','stock','created','updated']
    prepopulated_fields = {'slug':('pname',)}
    list_editable = ['price','available','stock']
    list_per_page = 20
admin.site.register(Product,ProductAdmin)