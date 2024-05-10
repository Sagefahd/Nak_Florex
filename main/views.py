from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Category



def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account successfully created for '+ user)
        return redirect('loginpage')
    else:
        form = UserCreationForm()
        context = {'form':form}
    return render(request, 'signup.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password incorrect')
    form = UserCreationForm(request.POST)
    context = {'form':form}
    return render(request, 'loginpage.html', context)

def logoutpage(request):
    logout(request)
    return redirect('loginpage')
    
    
#@login_required(login_url = 'loginpage')
def index(request):
     products = Product.objects.all()
     return render(request, 'index.html', {'products':products})

def about(request):
    return render(request, 'about.html')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request,foo):
    #replace hyphens with spaces
    foo = foo.replace('-', '')
    #grab the category from the url
    try:
        #Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html',{'products':products, 'category':category})

    except:
        messages.success(request, 'That category does not exist')
        return redirect('index')

# def category_summary(request):
#     categories = Category.objects.all()
#     return render(request, 'category_summary.html', {'categories':categories})









# Create your views here.
