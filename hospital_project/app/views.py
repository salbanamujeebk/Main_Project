from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login 
from .models import Departments, Doctors, Emergency, Orpahan_care,Booking, PatientConsultation
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date



# USER


def index(request):
    return render(request,'users/index.html')


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


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect(admin_home)  
            else:
                if user.usertype == "user": 
                    return redirect(home)  
                elif user.usertype == "doctor":
                    return redirect(doctor_home)  
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


@login_required
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


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = BookingForm()
    messages.success(request, "Consultation details submitted successfully!")
    return render(request, 'users/booking.html', {'form': form})


def doctors(request):
    doct= Doctors.objects.all()
    return render(request,'users/doctor.html', {'doctors': doct})




# def departments(request):
#     dept= Departments.objects.all()  
#     return render(request,'users/department.html',{'department':dept})

def department_doctors(request, department_id):
    department1 = Departments.objects.get(id=department_id)
    doctors = Doctors.objects.filter(department=department1.dep_name)
    return render(request, 'users/department_doctors.html', {'doctors': doctors, 'department': department1})


def doctor_view(request):
    doctors = Doctors.objects.select_related('department').all()
    department = Departments.objects.get(dep_name=doctors.department) 
    
    context = {
        'doctors': doctors,
        'department': department,
        
    }
    return render(request, 'users/doctor_view.html',context)


def contact(request):
    return render(request,'users/contact.html')



# DOCTORS



# def registration_doctor(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         Username = request.POST['username']
#         if CustomUser.objects.filter(username=Username,usertype="doctor").exists():
#             return render(request, 'doctors/doctor_reg.html', {'error': 'username already exists'})
#         age = request.POST['age']
#         Phonenumber = request.POST['phone']
#         if CustomUser.objects.filter(Phonenumber=Phonenumber,usertype="doctor",).exists():
#             return render(request, 'doctors/doctor_reg.html', {'error': 'Phonenumber already exists'})
#         dob = request.POST['dob']
#         Address = request.POST['address']
#         Email = request.POST['email']
#         if CustomUser.objects.filter(email=Email,usertype="doctor").exists():
#             return render(request, 'doctors/doctor_reg.html', {'error': 'email already exists'})
#         Password = request.POST['password']
#         speciality=request.POST['speciality']
#         department=request.POST['department']
#         image=request.FILES['Image']
#         data = CustomUser.objects.create_user(username=Username, Age=age,DOB=dob,Address=Address,email=Email,password=Password,usertype="doctor")
#         data.save()
#         try:
#             data1 = Doctors.objects.create(doc=data,name=name,speciality=speciality,department=department,image=image)
#             data1.save()
#         except Exception as e:
#             print(e)
            
#         return redirect(Login)
#     else:
#         # return HttpResponse("success")
#         return render(request,'doctors/doctor_reg.html')


def doctor_home(request):
    return render(request,'doctors/doctor_home.html')




def registration_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        Username = request.POST['username']
        if CustomUser.objects.filter(username=Username, usertype="doctor").exists():
            return render(request, 'doctors/doctor_reg.html', {'error': 'Username already exists'})
        
        age = request.POST['age']
        Phonenumber = request.POST['phone']
        if CustomUser.objects.filter(Phonenumber=Phonenumber, usertype="doctor").exists():
            return render(request, 'doctors/doctor_reg.html', {'error': 'Phonenumber already exists'})
        
        dob = request.POST['dob']
        Address = request.POST['address']
        Email = request.POST['email']
        if CustomUser.objects.filter(email=Email, usertype="doctor").exists():
            return render(request, 'doctors/doctor_reg.html', {'error': 'Email already exists'})
        
        Password = request.POST['password']
        speciality = request.POST['speciality']
        department = request.POST['department']
        image = request.FILES['Image']
    
        data = CustomUser.objects.create_user(username=Username, Age=age, DOB=dob, Address=Address, email=Email, password=Password, usertype="doctor", Phonenumber=Phonenumber)
        data.save()
        try:
            data1 = Doctors.objects.create(doc=data, name=name, speciality=speciality, department=department, image=image)
            data1.save()
        except Exception as e:
            print(e)
        
        return redirect(Login)
    
    else:
        return render(request, 'doctors/doctor_reg.html')



# def appoinments(request):
#     return render(request,'doctors/appoinments.html')



def appointments(request):
    doctor = CustomUser.objects.get(id=request.user.id)
    doctor_id = Doctors.objects.get(doc=doctor)  
    today = date.today()
    bookings = Booking.objects.filter(name=doctor_id). order_by('booking_date')
    
    return render(request,'doctors/appoinments.html',{'doctor': doctor_id, 'bookings': bookings, 'today':today})


# def consultation(request):
#     return render(request,'doctors/consultation.html')


def consultation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        condition = request.POST.get('condition')
        medicine = request.POST.get('medicine')
        doctor = request.user

        consultation = PatientConsultation(name=name,dob=dob,age=age,phone=phone,state=state,condition=condition,medicine=medicine,doctor=doctor)
        consultation.save()
        messages.success(request, "Consultation details submitted successfully!")
        return redirect('consultation')
    else:
        return render(request, 'doctors/consultation.html')


def approve_app(request):
    return HttpResponse("done")


def reject_app(request):
    return HttpResponse('done')


def my_patients(request):
    return render(request,'doctors/my_patients.html')


def patient_history(request):
    return render(request,'doctors/patient_history.html')


def doctor_profile(request):
    proff=Doctors.objects.get(id=request.user.id)
    return render(request,'doctors/doctor_profile.html',{'data':proff})




# ADMIN




def admin_home(request):
    return render(request,'admin/admin_home.html')

def doctors_list(request):  
    doctors = Doctors.objects.all()
    return render(request,'admin/doctors_list.html',{'doctors':doctors})

def patients_list(request):
    return render(request,'admin/patients_list.html')

def total_appoinments(request):
    return render(request,'admin/total_appoinments.html')


def doctor_details(request):
    return render(request,'admin/doctor_details.html')


# def doctor_details(request, doctor_id):
#     doctor = get_object_or_404(Doctors, id=doctor_id) 
#     return render(request, 'doctors/doctor_details.html', {'doctor': doctor})

def departments(request):
    dept = Departments.objects.all()
    return render(request, 'admin/department.html', {'department': dept})

#
def add_departments(request):
    if request.method == 'POST':
        dep_name = request.POST['dep_name']
        dep_description = request.POST['dep_description']
        department = Departments(dep_name=dep_name, dep_description=dep_description)
        department.save()
        return redirect('departments')  
    
    return render(request, 'admin/add_departments.html')
    

def update_department(request,id):
    data=Departments.objects.get(id=id)
    print("data ====   ",data)
    if request.method == 'POST':
        name = request.POST.get('dep_name')
        description = request.POST.get('dep_description')

        data.dep_name = name
        data.dep_description = description
        data.save()

        print("name --   ",data.dep_name)
        return redirect(departments) 
    else:
        return render(request, 'admin/update_department.html',{'data':data})


    # return render(request,'admin/update_department.html')






