from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from account.forms import loginform,registerform
# Create your views here.
def loginForm(request):
    if request.user.is_authenticated:
        return redirect('/')

    form=loginform(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            form.add_error('username','username with this information not found')

    context={
        "form":form
    }
    return render(request, 'loginForm.html', context)
def registerForm(request):
    form=registerform(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    if form.is_valid():
        username=form.cleaned_data['username']
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        user=authenticate(request,username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        login(request,user)
        return redirect('/')
    context={
        "form":form
    }
    return render(request, 'registerForm.html', context)

def Edit_information(request):
    me=User.objects.filter(username=request.user).first()

    if request.method=='POST':
        information = request.POST
        # state=None
        me.email=information['email']
        me.first_name=information['first_name']
        me.last_name=information['last_name']
        me.set_password(information['password'])
        print(information['password'])
        me.save()

    context={
    # 'state':state
    }
    return render(request,'edit_info.html',context)