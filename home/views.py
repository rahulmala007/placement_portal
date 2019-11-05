from django.shortcuts import render, redirect,render_to_response
from .models import *
from .forms import *
from django.template import RequestContext
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect


def index(request):
	return render(request, 'home/home.html')

def studentsList(request):

	students = Student.objects.all()
	context = {}
	context.update(csrf(request))
	context['students']=Student.objects.all()

	return render_to_response('home/studentsList.html',context)

def studentDetails(request, student_id):


	student = Student.objects.get(pk=int(student_id))

	if request.method == 'POST':
		form = StudentPlacedForm(request.POST)
		if form.is_valid():
			placed = form.cleaned_data.get('placed')
			company = form.cleaned_data.get('company')
			sector = form.cleaned_data.get('sector')
			profile = form.cleaned_data.get('profile')
			day = form.cleaned_data.get('day')
			slot = form.cleaned_data.get('slot')
			student.placed = True
			student.company = company
			student.sector = sector
			student.profile = profile
			student.branch.num+=1
			if not placed or company is "" or sector is "" or profile is "":
					return rende

			dobj = Day.objects.filter(dayNum=day, branch=student.branch)
			# print(dobj)
			# print("CCCCCCCCCCCCCCCCCCCC")
			if dobj.count()==0:

				Day.objects.create(dayNum=day, branch=student.branch)
				dobj = Day.objects.get(dayNum=day, branch=student.branch)
			else:
				dobj = dobj[0]

			dobj.num += 1
			dobj.save()
			# print (student.daynum)
			# print("check")
			student.save()
			student.branch.save()
			
		return redirect('home:students')
	else:
		form = StudentPlacedForm()
		if not student.placed:

			context = {
			'form':form,
			'student': student,
			}
		else:

			 context = {
			'form':form,
			'student': student,
			}


		return render(request, 'home/studentDetails.html', context)


def changestatus(request):
	if request.method == 'POST':
		id = request.POST['student_id']
		student = Student.objects.get(id=id)
		student.placed = False
		student.company = ''
		student.sector = ''
		student.profile = ''
		student.slot = 'S1'
		student.day = 0

		student.save()

	# return redirect('home:studentDetails' student.id')
	return redirect('home:studentDetails', student_id= id)


def search(request):
	if request.method=="POST":
		search_text=request.POST['search_text']
		print(search_text)
		students = Student.objects.filter(name__contains = search_text)
	else:
		search_text=" "
		students=[]

	return render(request,'home/ajax_search.html',{'students':students})

def showStudent(request):
	allstudents=Student.objects.all()
	context={'allstudents':allstudents}
	return render(request,'home/showStudent.html',context)


