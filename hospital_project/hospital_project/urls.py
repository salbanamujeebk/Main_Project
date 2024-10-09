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
    path('emergency',views.emergency,name='emergency'),
    path('orphan_care',views.orphan_care,name='orphan_care'),
    path('health_insurance',views.health_insurance,name='health_insurance'),
    path('health_checkup',views.health_checkup,name='health_checkup'),
    path('registration',views.registration,name='registration'),
    path('Login',views.Login,name='Login'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    # path('departments',views.departments,name='departments'),
    path('contact',views.contact,name='contact'),
    path('department_doctors/<int:department_id>', views.department_doctors, name='department_doctors'),
    path('doctors/', views.doctors, name='doctors'),
    


# DOCTOR
    
    path('doctor_home',views.doctor_home,name='doctor_home'),
    path('appoinments',views.appointments,name='appoinments'),
    path('consultation',views.consultation,name='consultation'),
    # path('doctor/<int:doctor_id>/appointments/', views.appointments, name='doctor_appointments'),
    path('my_patients',views.my_patients,name='my_patients'),
    path('patient_history',views.patient_history,name='patient_history'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),



#ADMIN
    path('registration_doctor',views.registration_doctor,name='registration_doctor'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('doctors_list',views.doctors_list,name='doctors_list'),
    path('patients_list',views.patients_list,name='patients_list'),
    path('total_appoinments',views.total_appoinments,name='total_appoinments'),
    #   path('total_appoinments', views.total_appoinments, name='total_appoinments'),
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





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)