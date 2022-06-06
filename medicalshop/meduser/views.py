from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/medshop/purchase')

        else:
            messages.info(request, "Invalid credentials")
            return redirect('/meduser/login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists, Try again')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email exists, Try again")
                return redirect('register')

            else:

                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)

                user.save()
                return redirect('/meduser/login')

        else:
            messages.info(request, "Password not matching, Reload the program")
            return redirect('/meduser/register')
        return redirect('/medshop')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/medshop')



