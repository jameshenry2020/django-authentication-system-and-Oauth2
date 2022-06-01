from django.urls import path
from .views import UserDashboard

urlpatterns= [
    path('', UserDashboard.as_view(), name='home'),
]