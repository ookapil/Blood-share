from django.urls import path
from . import views

app_name='register_app'


urlpatterns=[
	path("", views.Register, name="register"),
	path("success",views.success, name="success"),
	path("login",views.login, name="login"),
	path("login_success",views.login_success, name="login_success"),
]