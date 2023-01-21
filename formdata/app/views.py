from django.shortcuts import render
from . models import Form
import datetime
# Create your views here.


def index(request):
    form = Form.objects.all()
    return render(request, 'index.html', {
        'form': form,
    })


def form_submit(request):
    print('testing')
    if request.method == 'POST':
        print('testing')
        first_name = request.POST.get('first_name')
        print('_________________',first_name)
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        print('gender',gender)
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        # whatsapp = request.POST.get('whatsapp')
        # print('_________________', whatsapp)
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        cnic = request.POST.get('cnic')
        profession = request.POST.get('profession')
        print(profession)
        organization = request.POST.get('organization')
        designation = request.POST.get('designation')
        monthly_income = request.POST.get('monthly_income')
        working_since = request.POST.get('working_since')
        print('---------workin',working_since)
        # working_since_date =

        qualification = request.POST.get('qualification')

        add = Form(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            address=address,
            # whatsapp=whatsapp,
            mobile_no=mobile_no,
            email=email,
            cnic=cnic,
            profession=profession,
            organization=organization,
            designation=designation,
            monthly_income=monthly_income,
            working_since=working_since,
            qualification=qualification,
        )
        add.save()

    return render(request, 'index.html')