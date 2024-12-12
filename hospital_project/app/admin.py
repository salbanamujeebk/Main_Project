from django.contrib import admin
from .models import CustomUser,Departments,Doctors,Booking,Emergency,Orpahan_care,BloodDonation,PatientConsultation,Messagefromuser

# Register your models here.




admin.site.register(CustomUser)
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking)
admin.site.register(Emergency)
admin.site.register(Orpahan_care)
admin.site.register(PatientConsultation)
admin.site.register(BloodDonation)
admin.site.register(Messagefromuser)



