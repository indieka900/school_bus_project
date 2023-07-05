from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, DriverForm, StudentForm, FeedbackForm
from django.contrib import messages
from .models import Student


def home(request):
	return render(request,'school_app/index.html')
def about(request):
	return render(request,'school_app/aboutus.html')


def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!') 
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('adminPage')
        else:
            messages.error(request, 'Username or password does not exists')
            return redirect('home')
    return render(request,'school_app/adminLogin.html')
    
    
def register(request):
	if request.method == 'POST':
		f = CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			user = f.cleaned_data.get('username')
			messages.success(request, 'Account was successfully created for ' + user)
			return redirect('adminPage')

	else:
		f = CustomUserCreationForm()
	return render(request,'school_app/register.html',{'form': f})


def log_out(request):
     logout(request)
     return redirect('login')

def addDriver(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # # generate a unique password with 8 characters for the user
            # password = User.objects.make_random_password(length=8)
            # # set the password for the user (without hashing)
            # user.password = password
            # # save the user to the database
            user.save()
            return redirect('adminPage')
    context = {'form': form}
    #return render(request, 'dataApp/register.html', context)
    return render(request, 'school_app/addDriver.html',context)


def addStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # # generate a unique password with 8 characters for the user
            # password = User.objects.make_random_password(length=8)
            # # set the password for the user (without hashing)
            # user.password = password
            # # save the user to the database
            user.save()
            return redirect('adminPage')
    context = {'form': form}
    #return render(request, 'dataApp/register.html', context)
    return render(request, 'school_app/addStudent.html',context)
 
def parentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user= Student.objects.get(parent_name=username)
            if user.password == password:
                messages.success(request, f"Succesfully logged in as {user.name}")
                return redirect('parentTrack')
            else:
                messages.error(request, f'parent or password does not exists ')
                #return redirect('home')
        except:
            messages.error(request, f'Parent does not exists in our database!') 
    return render(request,'school_app/parentLogin.html')


def parentTrack(request):
	return render(request,'school_app/parentTrack.html')
def contactus(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'school_app/contactus.html', context)
def admin(request):
	return render(request,'school_app/admin.html')
def login_view(request):
	return render(request,'school_app/login.html')
# Create your views here.
