from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    # Create Object
    customers =Customer.objects.all()
    orders=Order.objects.all()

    # count Number of customer & Order
    total_customer=customers.count()
    total_order=orders.count()
    
    # total devliverd Order
    delivered=orders.filter(status="Delivered").count()

    # total pending Order
    pending=orders.filter(status="Pending").count()

    content={'customers':customers,'orders':orders,'total_order':total_order,'deliverd':delivered,'pending':pending}
    return render(request,'Account/dashboard.html',content)

# product page
def product(request):
    #return HttpResponse("Product Page")
    # Create Object
    products=Product.objects.all()
    return render(request,'Account/product.html',{'products':products})
# Customer Profile Page

def customer(request,pk_test):

    customer=Customer.objects.get(id=pk_test)
    #return HttpResponse("customer Page")
   
    orders=customer.order_set.all()
    total_order=orders.count()
    
    context={'customer':customer,'orders':orders,'total_order':total_order}

    return render(request,'Account/customer.html',context)
