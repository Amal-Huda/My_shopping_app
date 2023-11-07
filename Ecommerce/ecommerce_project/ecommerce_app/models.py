from django.db import models
from django.urls import reverse

# Create your models here.



class Category(models.Model):
    cname=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    cdescription=models.TextField(blank=True)
    cimage=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('cname',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('ecommerce_app:Products_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.cname)
class Product(models.Model):
    pname=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    pdescription=models.TextField(blank=True)
    pimage=models.ImageField(upload_to='product',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def get_url(self):
        return reverse('ecommerce_app:Product_details',args=[self.category.slug,self.slug])
    class Meta:
        ordering=('pname',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return '{}'.format(self.pname)



