from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import UserForm, nonAuthUserForm
from django.contrib.auth.models import User
from Donate.models import donationMade
from .models import User

def home(request):
    donationMade.objects.filter(paid=False).delete()
    return render(request, 'home.html')


def edit_user(request,pk):

    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        print(user)
        form = UserForm(request.POST, instance=user)
        print(form)
        if form.is_valid():
            User.objects.filter(pk=pk).delete()
            print("saving the form")
            form.save()
            return redirect('donationManagement')
    else:
        form = UserForm(instance=user)
    return render(request,'edit_user.html', {'form': form})



def delete_user(request,pk):
    User.objects.filter(pk=pk).delete()
    return redirect('userManagement')



def add_user(request):

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user, created = User.objects.get_or_create(**form.cleaned_data)
            print(user)
            print(created)
            #user = form.save(commit=False)
            #user.save()
            return redirect('userManagement')

    else:
        print("in else")
        form = UserForm()
        print(form)
        return render(request, "add_user.html", {'form': form})






@user_passes_test(lambda u: u.is_superuser)
def user_Management(request):
    users = User.objects.all()
    return render(request, "userManagement.html", {'users': users})




def admintemplate(request):
    return render(request, "AdminTemplate.html")


def donation(request):
    print("in donation")
    if (request.user.is_authenticated):
        #print(request.user.role)
        form = UserForm
        print(form)
    else:
        form = nonAuthUserForm
    if request.method == "POST":
        form = form(request.POST)
        print("form validation")
        if form.is_valid():
            print("creating a user object")
            user, created = User.objects.get_or_create(**form.cleaned_data)
            #user = form.save(commit=False)
            #user.save()

            # userInfo=form.cleaned_data
            # userRole=userInfo['role']
            # userInfo['role'] = userRole.toString
            #
            #
            #
            # request.session["userData"]=userInfo
            # print(request.session["userData"])



            return redirect("donate:donation_detail", id=user.id)
    else:
        print("in else")
        form = form()
        print(form)
        return render(request,"donation.html", {'form': form})












