from django.shortcuts import render,redirect
from account.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    if request.method =="POST":
        form =LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            if User.objects.filter(email = email).exists():
                username = User.objects.get(email=email).username
                user = authenticate(username=username, password= password)

                if user is not None:
                    login(request,user)
                    return redirect("home_page")
                else:
                    form.add_error(None,"Email ya da Parola Yanlış.")
                    return render(request,'account/login.html',{'form':form})
            else:
                form.add_error(None,"Email ile kayıtlı bir kullanıcı yok.")
                return render(request,'account/login.html', {'form':form})
        else:
            return render(request,'account/login.html',{'form':form})


    form = LoginForm()
    return render(request, 'account/login.html',{'form':form})

def register_request(request):
    return render(request, 'account/register.html')

def change_password(request):
    return render(request, 'account/change_password.html')


def logout_request(request):
    return render(request,'account/logout.html')
