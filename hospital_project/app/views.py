from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login 
from .models import Departments, Doctors, Emergency, Orpahan_care
from .forms import BookingForm

# Create your views here.


# USER


def index(request):
    return render(request,'users/index.html')

# def Login(request):
#      return render(request,'login.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        Username = request.POST['username']
        if CustomUser.objects.filter(username=Username).exists():
            return render(request, 'users/registration.html', {'error': 'username already exists'})
        age = request.POST['age']
        Phonenumber = request.POST['phone']
        if CustomUser.objects.filter(Phonenumber=Phonenumber).exists():
            return render(request, 'users/registration.html', {'error': 'Phonenumber already exists'})
        dob = request.POST['dob']
        Address = request.POST['address']
        Email = request.POST['email']
        if CustomUser.objects.filter(email=Email).exists():
            return render(request, 'users/registration.html', {'error': 'email already exists'})
        Password = request.POST['password']
        print("pass : ",Password)
        data = CustomUser.objects.create_user(first_name=name, username=Username, Age=age,DOB=dob,Address=Address,email=Email,password=Password,usertype="user")
        data.save()
        return redirect(Login)
    else:
        # return HttpResponse("success")
        return render(request,'users/registration.html')


# def Login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             if user.is_staff:
#                 return redirect('/admin/')  
#             else:
#                 if user.usertype == "user": 
#                     return HttpResponse('success')
#                     # return render(request,'home.html')  
#                 elif user.usertype == "doctor":
#                     return HttpResponse('success')  
#                 elif user.usertype == "admin":
#                     return redirect('/admin/')
#                 else:
#                     return HttpResponse("error")
#         else:
#             context = {
#                 'message': "Invalid credentials"
#             }
#             return render(request, 'login.html', context)
#     else:
#         return render(request, 'login.html')
    


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')  
            else:
                if user.usertype == "user": 
                    return redirect(home)  
                elif user.usertype == "doctor":
                    return redirect(doctor_home)  
                elif user.usertype == "admin":
                    return redirect('/admin/')
                else:
                    return HttpResponse("error")
        else:
            context = {
                'message': "Invalid credentials"
            }
            return render(request, 'users/login.html', context)
    else:
        return render(request, 'users/login.html')




def profile(request):
    prof=CustomUser.objects.get(id=request.user.id)
    return render(request,'users/profile.html',{'data':prof})


def editprofile(request):
    edit_prof=CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        edit_prof.first_name=request.POST['Name']
        edit_prof.Address=request.POST['Address']
        edit_prof.Phonenumber=request.POST['Phone']
        edit_prof.username=request.POST['Username']
        edit_prof.email=request.POST['Email']
        edit_prof.Age=request.POST['Age']
        edit_prof.DOB=request.POST['DOB']   
        # if 'Image' in request.FILES:
        #     editprof.Image = request.FILES['Image']
        # edit_prof.save()
        return redirect(profile)
    else:
        return render(request,'users/editprofile.html',{'data':edit_prof})


def home(request):
    dept= Departments.objects.all()  
    return render(request,'users/home.html',{'department':dept})

def outreach(request):
    return render(request,'users/outreach.html')

def kidney_care(request):
    return render(request,'users/kidney_care.html')

def paliative(request):
    return render(request,'users/paliative.html')

def donations(request):
    return render(request,'users/donations.html')


def emergency(request):
    emerg= Emergency.objects.all()  
    return render(request,'users/emergency.html',{'emergency':emerg})

def orphan_care(request):
    orph=Orpahan_care.objects.all()
    return render(request,'users/orphan_care.html',{'orphan_care':orph})

def health_insurance(request):
    return render(request,'users/health_insurance.html')

def health_checkup(request):
    return render(request,'users/health_checkup.html')

def about(request):
    return render(request,'users/about.html')






# def booking(request):
#     if request.method=="POST":
#         form=BookingForm(request.POST)
#         if form.os_valid():form.save()
#     form = BookingForm()
#     frm = {
#         'form': form
#     }
#     return render(request,'booking.html',frm)



def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = BookingForm()
    
    return render(request, 'users/booking.html', {'form': form})



# def doctors(request):
#     doct={
#         'doctors': Doctors.objects.all()
#     }
#     print(doct)
#     return render(request,'doctor.html',doct)



def doctors(request):
    doct= Doctors.objects.all()
    return render(request,'users/doctor.html', {'doctors': doct})




def departments(request):
    dept= Departments.objects.all()  
    return render(request,'users/department.html',{'department':dept})




def contact(request):
    return render(request,'users/contact.html')



# DOCTORS



def registration_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        Username = request.POST['username']
        if CustomUser.objects.filter(username=Username,usertype="doctor").exists():
            return render(request, 'doctors/doctor_reg.html', {'error': 'username already exists'})
        age = request.POST['age']
        Phonenumber = request.POST['phone']
        if CustomUser.objects.filter(Phonenumber=Phonenumber,usertype="doctor",).exists():
            return render(request, 'doctors/doctor_reg.html', {'error': 'Phonenumber already exists'})
        dob = request.POST['dob']
        Address = request.POST['address']
        Email = request.POST['email']
        if CustomUser.objects.filter(email=Email,usertype="doctor").exists():
            return render(request, 'doctors/doctor_reg.html', {'error': 'email already exists'})
        Password = request.POST['password']
        speciality=request.POST['speciality']
        department=request.POST['department']
        image=request.FILES['Image']
        data = CustomUser.objects.create_user(username=Username, Age=age,DOB=dob,Address=Address,email=Email,password=Password,usertype="doctor")
        data.save()
        try:
            data1 = Doctors.objects.create(doc=data,name=name,speciality=speciality,department=department,image=image)
            data1.save()
        except Exception as e:
            print(e)
            
        return redirect(Login)
    else:
        # return HttpResponse("success")
        return render(request,'doctors/doctor_reg.html')


def doctor_home(request):
    return render(request,'doctors/doctor_home.html')



def appoinments(request):
    return render(request,'doctors/appoinments.html')


def my_patients(request):
    return render(request,'doctors/my_patients.html')


def patient_history(request):
    return render(request,'doctors/patient_history.html')