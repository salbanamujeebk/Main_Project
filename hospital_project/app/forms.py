from django import forms

# from .models import Booking

# class DateInput(forms.DateInput):
#     input_type= 'date'

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = '__all__'

#         widgets = {
#             'booking_date':DateInput(),
#             'booked_on':DateInput()
#         }






class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)