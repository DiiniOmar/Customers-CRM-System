from django.shortcuts import render, redirect
from .forms import  LoginForm, UserCreationForm, CreateCustomerForms, UpdateCustomerForms
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.contrib import messages

#Home page
def indexView(request):
    return render(request, 'webapp/index.html')


#Register a User
def register(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account is been created successfully!")
            return redirect('my-login')
    context = {'form':form}
    return render (request, 'webapp/register.html', context=context)

#login user
def my_login(request):
    form = LoginForm()
    if request.method=='POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user =  authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
                
    context = {'form':form}
    return render(request,'webapp/my_login.html', context=context)

#User logout
def user_logout(request):
    auth.logout(request) 
    messages.success(request, "Logout success!")
    return redirect("my-login")


#Dashboard / CrUD operation
@login_required(login_url= "my-login")
def dashboard(request):
    my_records = Customer.objects.all()
    context = {'records': my_records}
    return render (request, 'webapp/dashboard.html', context=context)

#create a customer record
@login_required(login_url="my-login")
def CreateCustomer(request):
    form = CreateCustomerForms()
    if request.method=='POST':
        form = CreateCustomerForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer is been created successfully!")
            return redirect('dashboard')
    context= {'form': form}
    return render(request, 'webapp/create_record.html', context=context)

#update a customer record
@login_required(login_url="my-login")
def UpdateCustomer(request, pk):
    all_record= Customer.objects.get(id=pk)
    form = UpdateCustomerForms(instance=all_record)
    
    if request.method == 'POST':
        form = UpdateCustomerForms(request.POST,instance=all_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer details has been updated!")
            return redirect("dashboard")
    context= {'form': form}
    return render(request, 'webapp/update_record.html', context=context)

#Read / view a singular customer

@login_required (login_url='my-login')
def SinglurCustomer(request, pk):
    all_records= Customer.objects.get(id=pk)
    context = {'record': all_records}
    return render(request, 'webapp/views_record.html', context= context)


#Delete Customer
@login_required(login_url="my-login")
def DeleteCustomer(request, pk):
   record = Customer.objects.get(id=pk)
   record.delete()
   messages.success(request, "Customer details is has been deleted! ")
   return redirect("dashboard")