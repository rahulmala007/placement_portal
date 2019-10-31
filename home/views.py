from django.shortcuts import render
from .models import *

def index(request):
	return render(request, 'home/home.html')

def studentsList(request):
	students = Student.objects.all()
	context = {
		'students': students,
	}

	return render(request, 'home/studentsList.html', context)


