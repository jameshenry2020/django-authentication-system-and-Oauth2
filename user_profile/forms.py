from django import forms
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from phonenumber_field.modelfields import PhoneNumberField


class UserUpdateFrom(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username']


class UserProfileUpdateForm(forms.ModelForm):
    phone_number = PhoneNumberField(max_length=20)
    date_of_birth = forms.DateField(help_text='enter the date format yyyy-mm-dd')
    class Meta:
        model= UserProfile
        fields = ['bio', 'phone_number','date_of_birth','profile_image', 'gender', 'address']
