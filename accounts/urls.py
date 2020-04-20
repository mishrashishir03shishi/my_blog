from django.conf.urls import url, include
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [

    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),    
] 