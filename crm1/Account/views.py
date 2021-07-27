from django.db.models.query import prefetch_related_objects
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
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

def createOrder(request):
    form=OrderForm()
    if request.method=="POST":
        #print('Printing Post',request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'Account/order_form.html',context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        #print('Printing Post',request.POST)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'Account/order_form.html',context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'Account/delete.html',context)