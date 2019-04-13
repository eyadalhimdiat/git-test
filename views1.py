from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import DonationTypeForm, DonationForm
from .models import donationMade, donationtype




def donate(request):
    return render(request, 'registration/donate.html')


@user_passes_test(lambda u: u.is_superuser)
def donation_Management(request):
    donations = donationMade.objects.all()
    return render(request, 'donationManagement.html', {'donations': donations})



@user_passes_test(lambda u: u.is_superuser)
def donation_Type_Management(request):
    donationTypes=donationtype.objects.all()
    return render(request, "donationTypeManagement.html", {'donationTypes': donationTypes})




def add_donation_type(request):
    if request.method == "POST":
        form = DonationTypeForm(request.POST)
        print("form validation")
        if form.is_valid():
            print("creating a user object")
            donationtype.objects.get_or_create(**form.cleaned_data)
            # type = form.save(commit=False)
            # type.save()
            return redirect('donate:donationTypeManagement')
    else:
        form = DonationTypeForm()
        print(form)
        return  render(request, 'addDonationType.html', {'form': form})


def delete_donation(request,id):
    donationMade.objects.filter(pk=id).delete()
    return redirect('donate:donationManagement')

def delete_donation_type(request,pk):
    donationtype.objects.filter(pk=pk).delete()
    return redirect('donate:donation_Type_Management')



def donation_detail(request, id):
    print("in donation_details")
    if request.method == "POST":
        form = DonationForm(request.POST)
        print("form validation")
        if form.is_valid():
            print("creating a user object")
            user = form.save(commit=False)
            # print(user)
            user.save()

            # donationInfo = form.cleaned_data
            # donationInfo['user']= request.session["userData"]["firstname"]+" "+ request.session["userData"]["lastname"]
            # donation = donationInfo['donation']
            #
            # donationInfo['donation'] = donation.toString
            # donationDate = donationInfo['date']
            # donationInfo['date']=str(donationDate.date())
            #
            #
            # request.session["donationData"] = donationInfo
            # print(request.session["donationData"])


            print("after save")
            return redirect("cart:cart", id=id)
    else:
        print("in else")
        form = DonationForm()
        print(form)
        return render(request, "donation.html", {'form': form})




