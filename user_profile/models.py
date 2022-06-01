from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio=models.TextField(verbose_name=_('Bio'), default="tell us about yourself")
    phone_number=PhoneNumberField(default='+234********', max_length=20)
    date_of_birth=models.DateField(verbose_name =_('Date of Birth'), blank=True, null=True)
    profile_image=models.ImageField(verbose_name=_("Profile Image"), default="/profile_img/pic.png", upload_to='profile_img')
    gender=models.CharField(max_length=7, verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER)
    address=models.TextField(default='your home address...')
    


    def __str__(self):
        return self.user.username



