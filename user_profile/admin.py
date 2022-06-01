from django.contrib import admin
from .models import UserProfile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['id', 'user','phone_number','date_of_birth', 'gender']


admin.site.register(UserProfile, ProfileAdmin)