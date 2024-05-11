from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Profile
from .forms import UserInfoForm



def signup(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Account successfully created for '+ user.username)
                return redirect('index')
        else:
            messages.success(request, 'Whoops, there was a problem signing up, try again')
            return redirect('signup')


    else:
        return render(request, 'signup.html', {'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have bee logged in...")
            return redirect('index')
        else:
            messages.error(request, 'Username or password incorrect')
            return redirect('loginpage')
    form = UserCreationForm(request.POST)
        
    #context = {'form':form}
    return render(request, 'loginpage.html')

def logoutpage(request):
    logout(request)
    messages.success(request, "You have bee logged out...")
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

# def update_info(request):
#     if request.user.is_authenticated:
#         current_user = Profile.objects.get(user__id=request.user.id)
#         form = UserInfoForm(request.POST or None, instance=current_user)

#         if form.is_valid():
#             form.save()

#             messages.success(request, "Your Info has been updated" )
#             return redirect('index')
#         return render(request, 'update_info.html', {'form':form})
#     else:
#         messages.success(request, "You must be logged in to access that page" )
#         return redirect('index')
# def category_summary(request):
#     categories = Category.objects.all()
#     return render(request, 'category_summary.html', {'categories':categories})









# Create your views here.
