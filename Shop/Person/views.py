from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from Person.models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('main_page')
	template_name = 'users/signup.html'


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


class ProfileDetailView(DetailView):
	model = CustomUser
	context_object_name = 'profile'
	template_name = 'users/user_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = f'Страница пользователя: {self.object.username}'
		return context

