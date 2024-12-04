from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient
# Create your views here.


def hospital_index(request):
    return render(request, 'health/hospital.html')

def hospital_about(request):
    return render(request, 'health/about_hospital.html')

def hospital_appointment(request):
    return render(request, 'health/appointment_hos.html', {})

def form_process(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('mail')
        addressline1 = request.POST.get('addressline1')
        addressline2 = request.POST.get('addressline2')
        phone = request.POST.get('phone_no')

        try:
            Patient.objects.create(
                first_name = first_name, 
                last_name = last_name, 
                date_of_birth = date_of_birth, 
                email = email, 
                addressline1 = addressline1,
                addressline2 = addressline2, 
                phone = phone)
            
            return redirect('success')  # redirect to a different URL or view
        except Exception as e:
            return HttpResponse('<h4>Error creating patient: %s</h4>' % str(e))
        
def success(request):
    return HttpResponse('Form submitted Successfully')
        
