from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', views.index , name='index'),
    path('students', views.studentsList , name='students'),
]
