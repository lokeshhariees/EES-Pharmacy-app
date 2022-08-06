from django.shortcuts import render,redirect
from django.views import generic
from .models import product,bill,bill_products
from .forms import billform,billproductform
# Create your views here.
def home(request):
    return render(request,'home.html')

class productlist(generic.ListView):
    model=product

def billdetail(request,pk):
    bill_obj=bill.objects.get(bill_num=pk)
    bill_prds=bill_products.objects.filter(bill_item=bill_obj)
    context={
        'bill':bill_obj,
        'products':bill_prds
    }
    return render(request,'helloworld/bill_detail.html',context)

def billgen(request):
    billing_form=billform(request.POST)
    if billing_form.is_valid():
        bills=billing_form.save()
        return redirect('calculate-total',pk=bills.bill_num)
    return render(request,'helloworld/billadd_form.html',{'form':billing_form})

def calctotal(request,pk):
    bill_pro=bill.objects.get(bill_num=pk)
    products_set=bill_products.objects.filter(bill_item=bill_pro)
    total=2.0
    for product in products_set:
        price=product.bill_product.product_price
        qty=product.quantity
        item_sum=price*qty
        total=total+item_sum
    bill_pro.total_sum=total
    bill_pro.save()
    return redirect('bill-detail',pk=bill_pro.bill_num)


class productupdate(generic.UpdateView):
    model=product
    fields='__all__'
    template_name='helloworld/billadd_form.html'


def searchview(request):
    search_obj=request.GET.get('search')
    results=product.objects.filter(product_name__icontains=search_obj)
    if results:
        te=True
    else:
        results=False
    return render(request,'helloworld/product_list.html',{'product_list':results})


def bill_product_add(request,pk):
    billing_form=billproductform(request.POST)
    bill_obj=bill.objects.get(bill_num=pk)
    if billing_form.is_valid():
        billform_obj=billing_form.save(commit=False)
        product_obj=billform_obj.bill_product
        qty=billform_obj.quantity
        try :
            bill_info=bill_products.objects.get(bill_item=bill_obj,bill_product=product_obj)
            qty=qty+bill_info.quantity
            bill_info.quantity=qty
            bill_info.save()
        except bill_products.DoesNotExist:
            bills=billing_form.save(commit=False)
            bills.bill_item=bill_obj
            bills.save()
        return redirect('calculate-total',pk=bill_obj.bill_num)
    return render(request,'helloworld/billadd_form.html',{'form':billing_form})