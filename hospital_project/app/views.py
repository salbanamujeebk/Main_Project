from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login , logout
from .models import Departments, Doctors, Emergency, Orpahan_care,Booking, PatientConsultation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from django.shortcuts import get_object_or_404



# USER


def index(request):
    return render(request,'users/login.html')


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
        Image=request.FILES['Image']
        print("image :   ",Image)
        data = CustomUser.objects.create_user(first_name=name, username=Username,Image=Image,
                                               Age=age,DOB=dob,Address=Address,email=Email,
                                               password=Password,usertype="user")
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


import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PasswordResetRequestForm

def send_otp(email):
    otp = random.randint(100000, 999999) 
    send_mail(
        'Your OTP Code',
        f'Your OTP code is: {otp}',
        'shahanafathima2985@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
                otp = send_otp(email) 

                context = {
                            "email":email,
                            "otp":otp
                }

                return render(request,'verify_otp.html',context) 
            except User.DoesNotExist:
                messages.error(request, "Email address not found.")
    else:
        form = PasswordResetRequestForm()
    return render(request, 'password_reset_request.html', {'form': form})


def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otpold = request.POST.get('otpold')
        otp = request.POST.get('otp')

        if otpold==otp :

            context = {
                'otp' : otp,
                'email' : email
            }

            return render(request,'set_new_password.html',context)
        else:
            messages.error(request, "Invalid OTP.")
    return render(request, 'verify_otp.html')


def set_new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        try:
            user = CustomUser.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password has been reset successfully.")
            return redirect(Login)  # Redirect to login page
        except User.DoesNotExist:
            messages.error(request, "Email address not found.")
    return render(request, 'set_new_password.html', {'email': email})


def logout(request):
    auth.logout(request)
    return redirect(Login)


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
        if 'Image' in request.FILES:
            edit_prof.Image = request.FILES['Image']
        edit_prof.save()
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


# def booking(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('success')
#     else:
#         form = BookingForm()
#     messages.success(request, "Consultation details submitted successfully!")
#     return render(request, 'users/booking.html', {'form': form})




def booking(request):
    data = CustomUser.objects.get(id=request.user.id)
    doctors_name  = Doctors.objects.all()
    if request.method == "POST":
        patient_name= request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        booking_date=request.POST.get('bookingdate')
        dname = request.POST.get('dname')
        dname1 = Doctors.objects.get(id=dname)
        
        data1 = Booking.objects.create(user=data,p_name=patient_name,p_phone=phone,p_email=email,booking_date=booking_date,name=dname1)
        data1.save()
        return redirect(success)
    else:
        context = {
            "data":data,
            "doctors":doctors_name
        }
        return render(request, 'users/booking.html',context)

        
def success(request):
    return render(request,'users/success.html')


def view_payment(request):
    data = CustomUser.objects.get(id=request.user.id)
    book = Booking.objects.filter(user=data.id)
    return render(request,'users/view_payment.html',{'data':book})




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


def prescription(request):
    data = CustomUser.objects.get(id=request.user.id)
    presc = PatientConsultation.objects.filter(user_id=data.id)
    for i in presc:
        print(i.status)
    return render(request, 'users/prescription.html',{'presc':presc} )


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


def consultation(request, id):
    print(id)
    patient = Booking.objects.get(id = id)

    if request.method == "POST": 
        print('post')  
        name = request.POST.get('name')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        state = request.POST.get('state')
        condition = request.POST.get('condition')
        medicine = request.POST.get('medicine')
        doctor = request.user
      
        consultation1 = PatientConsultation.objects.create(user_id=patient.user,name=name,age=age,height=height,weight=weight,state=state,condition=condition,medicine=medicine,doctor=doctor,status="COMPLETED")
        consultation1.save()
        # print("hghghg")
        # messages.success(request, "Consultation details submitted successfully!")
        # return redirect('consultation')
        return redirect(appointments)
        
    else:
        return render(request, 'doctors/consultation.html',{'patient':patient})

def send_appr(email):
    otp = date.today()
    send_mail(
        'yor appointment is approved',
        f'this mail is send by this date: {otp}',
        'salbanamujeebali@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp

def send_rej(email):
    otp = date.today()
    send_mail(
        'yor appointment is Rejected',
        f'this mail is send by this date: {otp}',
        'salbanamujeebali@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp


def approve_app(request,id):
    data = CustomUser.objects.get(id=request.user.id)
    book = Booking.objects.get(id=id)
    email = book.user.email
    if request.method == 'POST':
        status = request.POST['status']
        if status == 'Approve':
            book.status = status
            book.save()
            try:
                user = CustomUser.objects.get(email=book.user.email)
                otp = send_appr(email) 

                
            except User.DoesNotExist:
                messages.error(request, "Email address not found.")
            return redirect(appointments)
        elif status == 'Reject':
            book.status = status
            book.save()
            try:
                user = CustomUser.objects.get(email=book.user.email)
                otp = send_rej(email) 

                
            except User.DoesNotExist:
                messages.error(request, "Email address not found.")
            return redirect(appointments)
        else:
            return redirect(appointments)
    else:
        return redirect(appointments)


def reject_app(request):
    return HttpResponse('done')


def my_patients(request):
    data = CustomUser.objects.get(id=request.user.id)
    consultation1 = PatientConsultation.objects.filter(doctor=data)
    print(consultation1)
    return render(request,'doctors/my_patients.html', {'consultation': consultation1})


def patient_history(request,id):
    details = PatientConsultation.objects.get(id=id)
    return render(request,'doctors/patient_history.html',{'details': details})



def doctor_profile(request):
    proff=Doctors.objects.get(id=request.user.id)
    return render(request,'doctors/doctor_profile.html',{'data':proff})



# ADMIN



def admin_home(request):
    total_doctors = Doctors.objects.count()  
    total_patients = PatientConsultation.objects.count() 
    total_appointments = Booking.objects.count()  
    total_departments = Departments.objects.count()  

    context = {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'total_departments': total_departments,
    }
    return render(request,'admin/admin_home.html',context)




def registration_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        Username = request.POST['username']
        if CustomUser.objects.filter(username=Username, usertype="doctor").exists():
            return render(request, 'admin/doctor_reg.html', {'error': 'Username already exists'})
        
        age = request.POST['age']
        Phonenumber = request.POST['phone']
        if CustomUser.objects.filter(Phonenumber=Phonenumber, usertype="doctor").exists():
            return render(request, 'admin/doctor_reg.html', {'error': 'Phonenumber already exists'})
        
        dob = request.POST['dob']
        Address = request.POST['address']
        Email = request.POST['email']
        if CustomUser.objects.filter(email=Email, usertype="doctor").exists():
            return render(request, 'admin/doctor_reg.html', {'error': 'Email already exists'})
        
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
        
        return redirect('doctors_list')
        # return HttpResponse("success")
    
    
    else:
        return render(request, 'admin/doctor_reg.html')


def doctors_list(request):  
    doctors = Doctors.objects.all()
    return render(request,'admin/doctors_list.html',{'doctors':doctors})


# def doctor_details(request,id):
#     doctors = Doctors.objects.all(id=id)
#     return render(request,'admin/doctor_details.html',{'doctors':doctors})

def doctor_details(request, id):
    doctor = get_object_or_404(Doctors, id=id)
    return render(request, 'admin/doctor_details.html', {'doctor': doctor})


def delete_doctor(request,id):
    data=Doctors.objects.get(id=id)
    data.delete()
    return redirect(doctors_list)


def patients_list(request):
    consultation1 = PatientConsultation.objects.all()
    print(consultation1)
    return render(request, 'admin/patients_list.html', {'consultation': consultation1})


def patient_details(request):
    details = PatientConsultation.objects.all()
    return render(request,'admin/patient_details.html',{'details': details})



# def patients_list(request):
#     try:
#         consultations = PatientConsultation.objects.all()
#     except Exception as e:
#         messages.error(request, f"An error occurred: {str(e)}")
#         consultations = [] 

#     return render(request, 'admin/patients_list.html', {'consultations': consultations})

def total_appoinments(request):
    return render(request,'admin/total_appoinments.html')

def total_appoinments(request):
    bookings = Booking.objects.all()
    return render(request, 'admin/total_appoinments.html', {'bookings': bookings})


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


def delete_department(request,id):
    data=Departments.objects.get(id=id)
    data.delete()
    return redirect(departments)


def records(request):
    return render(request,'admin/records.html')



def user_feedback(request):
    return render(request,'admin/user_feedback.html')



