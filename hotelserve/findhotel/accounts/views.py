from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import HotelForm
from hotel.models import Hotel

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"username taken")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"email taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request,"Account successfully created, thank you for register.")
                createduser = True
                return render(request, 'register.html')
        else:
            messages.warning(request,"Password does not match, please, try again.")
            return render(request, 'register.html')
    else:
        print('Account has not created, please, try again.')
        return render(request, 'register.html')


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        
        else:
            messages.info(request, 'invalid log in')
            return redirect('/')
    else:
        return render(request, '/')

def signout(request):
    logout(request)
    return redirect('/')


@login_required
def edit_profile(request):
    user_instance = User.objects.filter(username=request.user.username)[0]
    context = {
        "user_instance":user_instance
    }
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exclude(username=request.user.username).exists():
                 messages.info(request, "Username Taken")
                 return render(request, 'edit_profile.html', context)
            elif User.objects.filter(email=email).exclude(email=request.user.email).exists():
                 messages.info(request, "Email Taken")
                 return render(request, "edit_profile.html", context)
            else:
                 user_instance.username = username
                 user_instance.first_name = first_name
                 user_instance.last_name = last_name
                 user_instance.email = email
                 user_instance.set_password(password1)
                 user_instance.save()

                 messages.info(request, 'Updated Successfully')
                 user = authenticate(username = username, password = password1)
                 if user is not None:
                    login(request, user)
                    print("profile successfully updated")
                 return render(request, "edit_profile.html")
                
    else:
        return render(request, "edit_profile.html", context)


def add_hotel(request):
    form = HotelForm()
    if request.method == "POST":
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
    }
    return render(request, 'add_hotel.html', context)



def edit_hotel(request, id):
    edit = Hotel.objects.get(id=id)
    form = HotelForm(instance=edit)
    if request.method == "POST":
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'edit_hotel.html', context)
