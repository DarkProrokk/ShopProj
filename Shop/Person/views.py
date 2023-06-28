from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('main_page')
	template_name = 'users/signup.html'


# def register_request(request):
# 	if request.method == "POST":
# 		form = CustomUserCreationForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful.")
# 			return HttpResponse('Всё готово')
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = CustomUserCreationForm()
# 	return render(request, template_name="users/signup.html", context={"register_form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"login_form": form})

def logout_user(request):
	logout(request)
	return redirect('login')