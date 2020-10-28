from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("brief/", views.BriefPsnView, name="brief_psn"),
	path("brief-job/<int:client_id>/", views.BriefJobView, name="brief_job"),
	path("brief-opt/<int:brief_id>", views.BriefOptView, name="brief_opt"),
	path("register/", views.SignUpView, name="sign_up"),
	path("", views.LoginView, name="login"),
	path("userlogout/", views.UserLogoutView, name="user_logout"),
]
