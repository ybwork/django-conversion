"""conversion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as django_auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/login/',
         django_auth_views.LoginView.as_view(template_name='auth/login.html',
                                             redirect_authenticated_user=True),
         name='login'),

    path('accounts/logout/',
         django_auth_views.LogoutView.as_view(),
         name='logout'),

    path('accounts/password-change/',
         django_auth_views.PasswordChangeView.as_view(template_name='auth/password_change_form.html'),
         name='password_change'),

    path('accounts/password-change/done/',
         django_auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'),
         name='password_change_done'),

    path('accounts/password-reset/',
         django_auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'),
         name='password_reset'),

    path('accounts/reset/<uidb64>/<token>/',
         django_auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('accounts/reset/done/',
         django_auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/password-reset/done/',
         django_auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
         name='password_reset_done'),

    path('__debug__/', include(debug_toolbar.urls)),

    path('', include('currencies.urls'))
]