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
    

    day_data =  DataPool(
           series=
            [{'options': {
            'source': DayTotal.objects.all()},
                'terms': [{'day': 'dayNum',
                'placed': 'num'}]
                },

             ]) 

    day_cht = Chart(
            datasource = day_data,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'day': [
                    'placed']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Number of Students Placed: Day-Wise'},
               'xAxis': {
                   'title':{'text': 'Day'}},
               'yAxis': {
                   'title': {'text': 'Students Placed'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': False}},)
                   
    return render(request,'check.html', 
        {'chart_list': [br_cht, pi_cht,day_cht]})


@login_required()
def studentsList(request):

	students = Student.objects.all().order_by('roll')
	context = {}
	context.update(csrf(request))
	context['students']=students

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
			profile = form.cleaned_data.get('profile')
			day = form.cleaned_data.get('day')
			slot = form.cleaned_data.get('slot')
			student.placed = True
			student.company = company
			student.sector = sector
			student.profile = profile
			student.branch.num+=1
			student.day=day
			student.slot=slot
			

			dobj = Day.objects.filter(dayNum=day, branch=student.branch)
			
			if dobj.count()==0:

				Day.objects.create(dayNum=day, branch=student.branch)
				dobj = Day.objects.get(dayNum=day, branch=student.branch)

			else:
				dobj = dobj[0]

			numObj = DayTotal.objects.filter(dayNum=day)
			
			if numObj.count()==0:
				
				DayTotal.objects.create(dayNum=day)
				numObj = DayTotal.objects.get(dayNum=day)
			
			else:
				numObj = numObj[0]

			dobj.num += 1
			dobj.save()

			numObj.num+=1;
			numObj.save();
			student.save()
			student.branch.save()
	
		return redirect('home:students')
	else:
		data = {
		'placed':True,
		'company':student.company,
			'sector':student.sector,
			'profile':student.profile,	
			'day':student.day,
			'slot':student.slot}
		form = StudentPlacedForm(initial=data)
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

		dobj = Day.objects.get(dayNum=student.day, branch=student.branch)
	
		student.branch.num-=1
		

		dobj.num -= 1
		dobj.save()
		
		numObj = DayTotal.objects.get(dayNum=student.day)
		numObj.num-=1;

		numObj.save();
		student.branch.save()
		student.save()

	return redirect('home:studentDetails', student_id= id)


def search(request):
	if request.method=="POST":
		search_text=request.POST['search_text']
		print(search_text)
		students = Student.objects.filter(name__contains = search_text)
		students |= Student.objects.filter(company__contains = search_text)
		students |= Student.objects.filter(branch__branchName__contains = search_text)
		students |= Student.objects.filter(roll__contains = search_text)

	else:
		search_text=" "
		students=[]

	return render(request,'home/ajax_search.html',{'students':students})

def showStudent(request):
	
	context={}
	context.update(csrf(request))
	context['students']=Student.objects.all().order_by('roll')
	return render_to_response('home/showStudent.html',context)


def searchStudent(request):
	if request.method=="POST":
		search_text=request.POST['search_text']
		val = request.POST['val']
		place=request.POST['place']
		
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

	return render(request,'home/ajax_searchStudent.html',{'students':students})



def searchStudentList(request):
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



def branchlistshow(request):

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

	return render(request, 'home/ajax_searchStudent.html', {'students': students})


