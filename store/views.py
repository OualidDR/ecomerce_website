from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .forms import SignUpForm



def home_view(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products':products})



def about_view(request):
    
    return render(request,'about.html', {})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None :
            login(request, user)
            messages.success(request, ("You Have been Logged In !"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error please try again  !"))
            return redirect('login')

    else :
        return render(request,'login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, ("You have Been Logged out . . . "))
    return redirect('login')



def register_view(request):
    form = SignUpForm()
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            #login user
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("You Have Been Registerde Successfully . . . "))
            return redirect('home')
        else: 
            messages.success(request, ("Oops There Was A Problem Registering  please Try Again ! . . . "))
            return redirect('register')


    return render(request,'register.html', {'form' : form })


def product_view(request, pk):
    product=Product.objects.get(id = pk )
            

    return render(request,'product.html', {'product':product})


def category_view(request):
    
    return render(request,'category.html', {})
