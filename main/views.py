from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect

# Create your views here.


def main(request):
    meals = Meals.objects.all()
    category = Category.objects.all()
    context1 = {'meals':meals, 'category':category}
    return render(request, 'index.html', context=context1)

def contact(request):
    return render(request, 'contact.html')

def shopDetails(request):
    return render(request, 'shop-details.html')

def shopingCart(request):
    return render(request, 'shoping-cart.html')


def message(request):
    if request.method=='POST':
        send=Client()
        send.email=request.POST.get('email')
        send.save()
        return HttpResponseRedirect('/')