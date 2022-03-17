from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserApplication

# Create your views here.


@login_required
def index(request):
    'function to create an application'
    if request.method == "POST":
        #get all field values
        title = request.POST.get("title", None)
        first_name = request.POST.get("firstname", None)
        surname = request.POST.get("surname", None)
        d_o_b = request.POST.get("d_o_b", None)
        address = request.POST.get("address", None)
        telephone = request.POST.get("telephone", None)
        bidding_settings = request.POST.get("bidding_settings", None)
        google_id = request.POST.get("google_id", None)
        company_name = request.POST.get("company_name", None)

        #checks if the user is not submitting an existing google ID
        if UserApplication.objects.filter(google_id=google_id).exists():
            messages.error(request, "An Application with that GOOGLE ID already exists")
        #creates application
        else:
            UserApplication.objects.create(
                title=title,
                first_name=first_name,
                surname=surname,
                d_o_b=d_o_b,
                company_name=company_name,
                address=address,
                telephone=telephone,
                bidding_settings=bidding_settings,
                google_id=google_id,
            )
            return redirect("applications")

    return render(request, "formapp/customerSubmitForm.html")


@login_required
def show_applications(request):
    '''
    Function to fetch all applications submitted successfully
    '''
    applications = UserApplication.objects.all()
    context = {"applications": applications}
    return render(request, "formapp/showApplications.html", context)


@login_required
def delete_application(request, id):
    '''
    # Function to delete an application using it's id
    '''
    application = UserApplication.objects.get(id=id)
    application.delete()
    return redirect("applications")
