from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'auths'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="auths/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auths/logout.html"), name='logout'),
    
]
