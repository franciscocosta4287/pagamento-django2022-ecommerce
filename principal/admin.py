from django.contrib import admin

# Register your models here.
from .models import Banner, Category, Marca, Color, Size, Product, ProductAttribute

admin.site.register(Banner)
# admin.site.register(Category)
admin.site.register(Marca)
# admin.site.register(Color)
admin.site.register(Size)
# admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):  # Lenvando a imagem ao admim
    list_display  = ('title','img_tag_path')
admin.site.register(Category, CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):  # Lenvando a COR ao admim
    list_display  = ('title','color_tag_path')
admin.site.register(Color, ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display  = ('id','title','marca','color','size','status','is_feat_caracterico')
    list_editable = ('status','is_feat_caracterico')

admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display  = ('id','product','price','color','size')
    
admin.site.register(ProductAttribute, ProductAttributeAdmin)
