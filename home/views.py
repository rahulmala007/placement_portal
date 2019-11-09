from django.shortcuts import render, redirect,render_to_response
from .models import *
from .forms import *
from django.template import RequestContext
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from chartit import DataPool, Chart, PivotDataPool, PivotChart


def index(request):
    branch_data =  DataPool(
           series=
            [{'options': {
            'source': Branch.objects.all()},
                'terms': [{'branch': 'branchName',
                'placed': 'num'}]
                },

             ]) 

    br_cht = Chart(
            datasource = branch_data,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'branch': [
                    'placed']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Number of Students Placed'},
               'xAxis': {
                   'title':{'text': 'Branch'}},
               'yAxis': {
                   'title': {'text': 'Students Placed'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},)
                   
    pi_cht = Chart(
            datasource = branch_data,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'branch': [
                    'placed']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Number of Students Placed - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Branch'}},
               'yAxis': {
                   'title': {'text': 'Placed'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},)

    return render(request,'check.html', 
        {'chart_list': [br_cht, pi_cht]})

@login_required()
def studentsList(request):

	students = Student.objects.all()
	context = {}
	context.update(csrf(request))
	context['students']=Student.objects.all()

	return render_to_response('home/studentsList.html',context)


@login_required()
def studentDetails(request, student_id):


	student = Student.objects.get(pk=int(student_id))

	if request.method == 'POST':
		form = StudentPlacedForm(request.POST)
		if form.is_valid():
			placed = form.cleaned_data.get('placed')
			company = form.cleaned_data.get('company')
			sector = form.cleaned_data.get('sector')
			roll=form.cleaned_data.get('roll')
			profile = form.cleaned_data.get('profile')
			day = form.cleaned_data.get('day')
			slot = form.cleaned_data.get('slot')
			student.placed = True
			student.company = company
			student.sector = sector
			student.profile = profile
			student.branch.num+=1
			

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
		student.roll=''
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
		students |= Student.objects.filter(company__contains = search_text)
		students |= Student.objects.filter(branch__branchName__contains = search_text)
		students |= Student.objects.filter(roll__contains = search_text)

		# stul = []

		# BRANCH_CHOICES = [
		# 	('CSE', 'Computer Science and Engineering'),
		# 	('MNC', 'Mathematics and Computing'),
		# 	('ECE', 'Electronics and Communication Engineering'),
		# 	('EEE', 'Electronics and Electrical Engineering'),
		# 	('ME', 'Mechanical Engineering'),
		# 	('CE', 'Civil Engineering'),
		# 	('CL', 'Chemical Engineering'),
		# 	('EP' , 'Engineering Physics'),
		# 	('CST','Chemical Science and Technology'),
		# 	('BT','Biotechnology'),
		# ]

		# for tup in BRANCH_CHOICES:
		# 	if search_text in tup[1]:
				
				

		# for stu in Student.objects.all():
		# 	if search_text in stu.branch.get_branchName_display():
		# 		stul.append(stu);

		# students |=stu


	else:
		search_text=" "
		students=[]

	return render(request,'home/ajax_search.html',{'students':students})

def showStudent(request):
	allstudents=Student.objects.all()
	context={}
	context.update(csrf(request))
	context['students']=Student.objects.all()
	return render_to_response('home/showStudent.html',context)


def searchStudent(request):
	if request.method=="POST":
		search_text=request.POST['search_text']
		val = request.POST['val']
		place=request.POST['place']
		# print(search_text)
		# print(val)
		


		
		students = Student.objects.filter(name__contains = search_text)
		students |= Student.objects.filter(company__contains = search_text)
		students |= Student.objects.filter(branch__branchName__contains = search_text)
		students |= Student.objects.filter(roll__contains = search_text)

		if val:
			if place == "True":
				students = students.filter(branch__branchName=val,placed=True)
			elif place == "False" :
				students = students.filter(branch__branchName=val,placed=False)
			else:
				students = students.filter(branch__branchName=val)
		else:
			if place == "True":
				students = students.filter(placed=True)
			elif place == "False" :
				students = students.filter(placed=False)
			else:
				students = students

		


	else:
		search_text=" "
		students=[]

	return render(request,'home/ajax_search.html',{'students':students})


def branchlist(request):

	if request.method == "POST":
		val = request.POST['val']
		place=request.POST['place']


		if val:
			if place == "True":
				students = Student.objects.filter(branch__branchName=val,placed=True)
			elif place == "False" :
				students = Student.objects.filter(branch__branchName=val,placed=False)
			else:
				students = Student.objects.filter(branch__branchName=val)
		else:
			if place == "True":
				students = Student.objects.filter(placed=True)
			elif place == "False" :
				students = Student.objects.filter(placed=False)
			else:
				students = Student.objects.all()




		



	else:
		val = " "
		students = []

	return render(request, 'home/ajax_search.html', {'students': students})


