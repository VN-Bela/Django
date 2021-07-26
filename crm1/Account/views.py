from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    # Create Object
    customers =Customer.objects.all()
    orders=Order.objects.all()
    content={'customers':customers,'orders':orders}
    return render(request,'Account/dashboard.html',content)

# product page
def product(request):
    #return HttpResponse("Product Page")
    # Create Object
    products=Product.objects.all()
    return render(request,'Account/product.html',{'products':products})
# Customer Profile Page

def customer(request):
    #return HttpResponse("customer Page")
    return render(request,'Account/customer.html')
