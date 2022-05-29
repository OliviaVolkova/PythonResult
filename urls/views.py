from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from urls.forms import UserForm, UrlForm
from urls.models import UrlModel
from urls.utils import get_random_string


class AllUrlsView(View):
    template_name = 'all_urls.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            urls = UrlModel.objects.filter(user_id=user.id).order_by('-count')
            return render(request, self.template_name, {
                'urls': urls
            })
        else:
            return redirect("/sign_in")

    def post(self, request):
        UrlModel.objects.filter(id=request.POST.get("url_id", "")).delete()
        return redirect("/all_urls/")


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
            return redirect('/')
        return render(request, self.template_name, {
            'form': userForm
        })


class DefaultView(View):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)


class AddUrlView(View):
    template_name = 'add_url_page.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form': UrlForm
        })

    def post(self, request):
        form = UrlForm(request.POST)

        if form.is_valid():
            model = form.save(commit=False)
            model.new_url = get_random_string(6)
            model.user = request.user
            model.url = form.cleaned_data.get('url')
            while model.__class__.objects.filter(new_url=model.new_url).exclude().exists():
                model.new_url = get_random_string(6)
            model.save()

            return render(request, self.template_name, {
                'form': UrlForm
            })
        return render(request, self.template_name, {
            'errors': form.errors
        })


class Redirect(View):
    def get(self, request, new_url):
        try:
            url = UrlModel.objects.get(new_url=new_url)
            url.count += 1
            url.save()
            return HttpResponseRedirect(url.url)
        except:
            return redirect("/all_urls/")
