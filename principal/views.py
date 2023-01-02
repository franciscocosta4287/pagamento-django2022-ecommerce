from django.shortcuts import render
from .models import Category, Marca, Product, ProductAttribute, Banner

# Create your views here.
def home(request):
    banners = Banner.objects.all().order_by('-id')  # Banner
    data = Product.objects.filter(is_feat_caracterico = True).order_by('-id')  # Em destaque
    return render(request, 'index.html', {'data':data, 'banners':banners})

def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data':data})

def marca_list(request):
    data=Marca.objects.all().order_by('-id')
    return render(request, 'marca_list.html', {'data':data})

def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    marcas=Product.objects.distinct().values('marca__title','marca__id')
    colors=ProductAttribute.objects.distinct().values('color__title','color_id', 'color__color_codigo')
    sizes=ProductAttribute.objects.distinct().values('size__title','size__id')

    return render(request, 'product_list.html', 
    {
        'data':data,
        'cats':cats,
        'marcas':marcas,
        'colors':colors,
        'sizes':sizes
    }
    )