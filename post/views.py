from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm

#using messages
from django.contrib import messages
# handle login form
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

#resctrict access to some pages 
from django.contrib.auth.decorators import login_required
def home(request):
    # return HttpResponse('Hello Learns!!!')
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #get username 
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account succefully created for ' + user)
            # After user has registered take them to login page
            return redirect('signin')
    context = {'form': form}
    #return HttpResponse('Hello Learns!!!')
    return render(request, "register.html", context)


# def register(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     #return HttpResponse('Hello Learns!!!')
#     return render(request, "register.html", context)



# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    context = {}
    return render(request, 'login.html', context)

def logout(request): 
    return redirect('home')

@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')