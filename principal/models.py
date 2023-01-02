from django.db import models
from distutils.command.upload import upload
from email.policy import default
from django.utils.html import mark_safe
 
# Create your models here.
class Banner(models.Model):
    img = models.CharField(max_length=250)
    alt_text = models.CharField(max_length=300)

    class Meta: #alterar o banner
        verbose_name_plural = '1. Banners'

class Category(models.Model):
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta: # enumeracao no administrador  Category
        verbose_name_plural = '2. Categories'
    
    def img_tag_path(self):  # Lenvando a imagem ao admim
        return mark_safe('<img src="%s" width="100" heigth="100" />' %(self.image.url))

    def __str__(self):
        return self.title

class Marca(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="marca_imgs/")

    class Meta: #alterar o Marcas
        verbose_name_plural = '3. Marcas'

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=100)
    color_codigo = models.CharField(max_length=100)  # trazendo a Cor

    class Meta: #alterar o Cores
        verbose_name_plural = '4. Colors'
    
    def color_tag_path(self):  # Lenvando a Cor ao admim
        return mark_safe('<div style="width:100px; heigth:100px; background:%s;"></div>'%(self.color_codigo))
        # return mark_safe( '<div style="color: #%s; width:100px; heigth:100px; background:%s;"></div>' % (self.color_codigo))
        # color_tag_path.allow_tags = True

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=100) 

    class Meta: #alterar o banner
        verbose_name_plural = '5. Sizes'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length=400) #Apelido
    datail = models.TextField() # detalhe
    specs = models.TextField() # Especificao
    # price = models.PositiveIntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) # Deletendo tudo
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Deletendo tudo
    color = models.ForeignKey(Color, on_delete=models.CASCADE) # Deletendo tudo
    size = models.ForeignKey(Size, on_delete=models.CASCADE) # Deletendo tudo
    # marca = models.ForeignKey(Marca, on_delete=models.CASCADE) # Ativo/ tru /false
    status = models.BooleanField(default=True)# Ativo/ tru /false
    is_feat_caracterico =models.BooleanField(default=False)

    class Meta: # Enumerando o Produtos
        verbose_name_plural = '6. Productos'

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):  # Atributos do produto
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta: #alterar o banner
        verbose_name_plural = '7. ProductAttributes'

    def __str__(self):
        return self.product.title  # Retornno o titulo do Produto
