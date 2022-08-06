from django.db import models
from django.urls import reverse

# Create your models here.
class productcategory(models.Model):
    category_num=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50,help_text='Enter category name',verbose_name='Category name')

    def __str__(self):
        return self.category_name

class product(models.Model):
    product_num=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,help_text='Enter product name',verbose_name='Product name')
    product_category=models.ForeignKey('productcategory',on_delete=models.SET_NULL,null=True)
    product_price=models.FloatField()

    def __str__(self):
        return self.product_name

    def get_update_url(self):
        return reverse('product-update',args=[str(self.product_num)])

class bill(models.Model):
    bill_num=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=50,help_text='Enter customer name',verbose_name='Customer name')
    product=models.ManyToManyField('bill_products')
    total_sum=models.FloatField(default=2.0)

    def __str__(self):
        return self.customer_name

    def add_product(self):
        return reverse('add-bill-product',args=[str(self.bill_num)])

class bill_products(models.Model):
    bill_pronum=models.AutoField(primary_key=True)
    bill_item=models.ForeignKey('bill',on_delete=models.SET_NULL,null=True)
    bill_product=models.ForeignKey('product',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1,help_text='Default is one')

    def __str__(self):
        return self.bill_product.product_name