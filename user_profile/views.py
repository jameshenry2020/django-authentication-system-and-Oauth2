from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateFrom, UserProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
class UserDashboard(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        u_form = UserUpdateFrom(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)
        context={
            'user_form':u_form,
            'profile_form':p_form
        }
        return render(request, 'profile/home.html', context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateFrom(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, f'account updated successfully')
            return redirect('home')

        return render(request, 'profile/home.html', context)


@login_required
def index_view(request):
    return render(request, 'profile/index.html')


