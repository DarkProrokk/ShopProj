from django.urls import path
from .views import *

urlpatterns = [
	path('register/', SignUpView.as_view(), name='register'),
	path('login/', login_request, name='login'),
	path('logout/', logout_user, name='logout')
]
