from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'Account/dashboard.html')

# product page
def product(request):
    #eturn HttpResponse("Product Page")
    return render(request,'Account/product.html')
# Customer Profile Page

def customer(request):
    #return HttpResponse("customer Page")
    return render(request,'Account/customer.html')
