from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from urls.forms import UserForm


class SignUp(View):
    template_name = 'sign_up.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, self.template_name, {
            'form': UserForm()
        })

    def post(self, request):
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            username = userForm.cleaned_data.get('username')
            password = userForm.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('')
        return render(request, self.template_name, {
            'form': userForm
        })


