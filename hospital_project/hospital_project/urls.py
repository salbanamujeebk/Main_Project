"""hospital_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoprojecdt.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

# USER

    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('outreach',views.outreach,name='outreach'),
    path('kidney_care',views.kidney_care,name='kidney_care'),
    path('paliative',views.paliative,name='paliative'),
    path('donations',views.donations,name='donations'),
    path('blood_donation',views.blood_donation,name='blood_donation'),
    path('hair_donation',views.hair_donation,name='hair_donation'),
    path('other_donation',views.other_donation,name='other_donation'),
    path('emergency',views.emergency,name='emergency'),
    path('orphan_care',views.orphan_care,name='orphan_care'),
    path('health_insurance',views.health_insurance,name='health_insurance'),
    path('health_checkup',views.health_checkup,name='health_checkup'),
    path('registration',views.registration,name='registration'),
    path('Login',views.Login,name='Login'),
    path('logout',views.logout,name='logout'),
    path('send_otp',views.send_otp,name='send_otp'),
    path('password_reset_request',views.password_reset_request,name='password_reset_request'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_new_password',views.set_new_password,name='set_new_password'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('view_payment',views.view_payment,name='view_payment'),
    # path('departments',views.departments,name='departments'),
    path('contact',views.contact,name='contact'),
    path('department_doctors/<int:department_id>', views.department_doctors, name='department_doctors'),
    path('doctors/', views.doctors, name='doctors'),
    path('success',views.success,name='success'),
    path('prescription',views.prescription,name='prescription'),
    path('payment_details/<int:id>',views.payment_details,name='payment_details'),
    path('creditcard/<int:id>',views.creditcard,name='creditcard'),
    path('debitcard',views.debitcard,name='debitcard'),
    path('complete_payment',views.complete_payment,name='complete_payment'),
    
    


# DOCTOR
    
    path('doctor_home',views.doctor_home,name='doctor_home'),
    path('appoinments',views.appointments,name='appoinments'),
    path('consultation/<int:id>/',views.consultation,name='consultation'),
    # path('doctor/<int:id>/appointments/', views.appointments, name='appointments'),
    path('my_patients',views.my_patients,name='my_patients'),
    path('patient_history/<int:id>',views.patient_history,name='patient_history'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    path('approve_app/<int:id>',views.approve_app,name='approve_app'),
    path('remuneration',views.remuneration,name='remuneration'),
    # path('remuneration/<int:consultation_id>/',views.remuneration,name='remuneration'),
    path('remuneration_report',views.remuneration_report,name="remuneration_report"),



#ADMIN
    path('registration_doctor',views.registration_doctor,name='registration_doctor'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('doctors_list',views.doctors_list,name='doctors_list'),
    path('patients_list',views.patients_list,name='patients_list'),
    path('patient_details',views.patient_details,name='patient_details'),
    path('total_appoinments',views.total_appoinments,name='total_appoinments'),
    #  path('total_appoinments', views.total_appoinments, name='total_appoinments'),
    path('approve_app',views.approve_app,name='approve_app'),
    path('reject_app',views.reject_app,name='reject_app'),
    # path('doctor_details',views.doctor_details,name='doctor_details'),
    # path('departments_list',views.departments_list,name='departments_list'),
    path('doctor_view',views.doctor_view,name='doctor_view'),
    path('doctor_details/<int:id>/', views.doctor_details, name='doctor_details'),
    path('add_departments',views.add_departments,name='add_departments'),
    path('departments/', views.departments, name='departments'),
    path('update_department/<int:id>',views.update_department,name='update_department'),
    path('delete_department/<int:id>',views.delete_department,name='delete_department'),
    path('delete_doctor/<int:id>',views.delete_doctor,name='delete_doctor'),
    path('records',views.records,name='records'),
    path('user_feedback',views.user_feedback,name='user_feedback'),
    # path('dashboard_view',views.dashboard_view,name='dashboard_view'),
    path('financial_area',views.financial_area,name='financial_area'),
    path('paliative_details',views.paliative_details,name='paliative_details'),
    path('donation_details',views.donation_details,name='donation_details'),
    path('insurance_details',views.insurance_details,name='insurance_details'),
    path('orphancare_details',views.orphancare_details,name='orphancare_details'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)