from django.contrib import admin
from .models import productcategory,product,bill,bill_products
# Register your models here.

admin.site.register(productcategory)

admin.site.register(product)

admin.site.register(bill)

admin.site.register(bill_products)