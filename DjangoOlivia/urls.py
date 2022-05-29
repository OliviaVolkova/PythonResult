"""DjangoOlivia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views

from urls.views import SignUp, DefaultView, AddUrlView, AllUrlsView, Redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('sign_in/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),

    path('', include('django.contrib.auth.urls')),

    path('sign_up/', SignUp.as_view(), name='sign_up'),

    path('', DefaultView.as_view(), name='default'),

    path('add/', AddUrlView.as_view(), name='add_url'),

    path('all_urls/', AllUrlsView.as_view(), name='all_urls'),

    path('<str:new_url>', Redirect.as_view(), name='redirect')
]
