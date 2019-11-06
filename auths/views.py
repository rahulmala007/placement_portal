# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

# def register(request):
# 	if request.method == 'POST':
		
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		email = request.POST['email']
# 		User.objects.create_user(username, email, password)
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 		else:
# 			return render(request, 'auths/signup.html')

# 		return redirect('core:home')
# 	else:
# 		return render(request, 'auths/signup.html')


# # def login2(request):
# # 	if request.method == 'POST':
# # 		form = UserCreationForm(request.POST)
# # 		username = request.POST['username']
# # 		password = request.POST['password']
# # 		user = User.objects.get(username=username)
# # 		if user is not None:
# # 			login(request, user)
# # 			return redirect('core:home')
# # 	return render(request, 'auths/login.html')
	
