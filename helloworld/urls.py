from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('products/',views.productlist.as_view(),name='product-list'),
    path('product/<int:pk>/update/',views.productupdate.as_view(),name='product-update'),
    path('billing/',views.billgen,name='bill'),
    path('calcsum/<int:pk>/',views.calctotal,name='calculate-total'),
    path('bill/<int:pk>/',views.billdetail,name='bill-detail'),
    path('search-result/',views.searchview,name='search-product'),
    path('add-product-in-bill/<int:pk>/',views.bill_product_add,name='add-bill-product'),
]
