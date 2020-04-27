from django.shortcuts import render
from basicApp.forms import UserInfo,UserProfileInfoForm

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# Create your views here.
def index(request):
    return render(request,'basicApp/index.html')


def register(request):

    registered=False

    if request.method =='POST':
        userForm=UserInfo(data=request.POST)
        userForm2=UserProfileInfoForm(data=request.POST)

        if userForm.is_valid() and userForm2.is_valid():

            user=userForm.save()
            user.set_password(user.password)
            user.save()

            profile=userForm2.save(commit=False)
            profile.user=user

            if 'profile_pics' in request.FILES:
                profile.profile_pics=request.FILES['profile_pics']
            profile.save()

            registered=True
        else:
            print(userForm.errors,userForm2.errors)

    else:
        userForm = UserInfo()
        userForm2 = UserProfileInfoForm()
    return render(request,'basicApp/registration.html',
                    {'user_Form':userForm,
                     'user_Form2':userForm2,
                     'registered':registered})




def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
              return HttpResponse("NOT A active USER!!")

        else:
            print("UserName : {},password{} = tried to login".format(username,password))
            return HttpResponse("NOT A VALID USER!!")

    else:
        return render(request,'basicApp/login.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
















