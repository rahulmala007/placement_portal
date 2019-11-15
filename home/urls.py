from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', views.index , name='index'),
    path('students', views.studentsList , name='students'),
    path('changestatus', views.changestatus , name='changestatus'),
    path('students/<int:student_id>', views.studentDetails , name='studentDetails'),
    path('search',views.search, name='search'),
    path('showStudent',views.showStudent, name='showStudent'),
    path('searchStudent',views.searchStudent,name='searchStudent'),
    path('searchStudentList',views.searchStudentList,name='searchStudentList'),
    path('branchlist',views.branchlist,name="branchlist"),
    path('branchlistshow',views.branchlistshow,name="branchlistshow")
]
