from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm, SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from project.models import *
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import random
import string
import datetime

# Create your views here.


def RayBringSec(time_rate, t_seconds):
	#time_rate 4rm the department, t_seconds 4rm the project
	result = (time_rate/100) * t_seconds
	return result


def RayDateToSec(k_date):
	intial = datetime.datetime.utcfromtimestamp(0)
	result = k_date - intial
	return result.total_seconds() / 1000


def RayConvertDate(d,m,y):
	if m == "01":
		m = "Jan"
	elif m == "02":
		m = "Feb"
	elif m == "03":
		m = "Mar"
	elif m == "04":
		m = "Apr"
	elif m == "05":
		m = "May"
	elif m == "6":
		m = "Jun"
	elif m == "07":
		m = "Jul"
	elif m == "08":
		m = "Aug"
	elif m == "09":
		m = "Sep"
	elif m == "10":
		m = "Oct"
	elif m == "11":
		m = "Nov"
	elif m == "12":
		m = "Dec"
	else:
		pass

	#format = Jan 5, 2021 12:00:00
	converted_date = m +" " +d +"," +" " +y +" " +"12:00:00"

	return converted_date



def ray_randomizer(breath=0, length=7):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))

def SignUpView(request):
	if request.method == "POST":
		form1 = SignUpForm(request.POST or None, request.FILES or None)
		form2 = UserForm(request.POST or None, request.FILES or None)
		
		if request.POST.get("password2") != request.POST.get("password1"):
			return HttpResponse("Error!  -Please make sure both passwords are similar")
			
		else:
			user = form2.save()
			user.set_password(request.POST.get("password1"))
			user.save()
			
					
			department = form1.save(commit=False)
			department.user = user
			department.department_id = ray_randomizer(4,10)
			department.save()

			if department.name == "design":
				department.time_rate = 23.88
			elif department.name == "cutlist":
				department.time_rate = 11.94
			elif department.name == "project-service":
				department.time_rate = 0.25
			elif department.name == "material-estimate":
				department.time_rate = 11.94
			elif department.name == "store":
				department.time_rate = 0.25
			elif department.name == "supply-chain":
				department.time_rate = 11.94
			elif department.name == "cutting":
				department.time_rate = 0.5
			elif department.name == "edge-banding":
				department.time_rate = 1
			elif department.name == "cnc":
				department.time_rate = 0.5
			elif department.name == "assembly":
				department.time_rate = 11.94
			elif department.name == "cleaning":
				department.time_rate = 1
				department.u_time_rate = 0.88
			elif department.name == "dispatch":
				department.time_rate = 1
				department.u_time_rate = 0.88
			elif department.name == "installation":
				department.time_rate = 23.88
				department.u_time_rate = 21.15

			elif department.name == "upholstery":
				department.u_time_rate = 0

			else:
				pass

			department.save()

			return HttpResponseRedirect(reverse("main:login"))
	
	else:
		form1 = SignUpForm()
		form2 = UserForm()
		return render(request, "main/sign_up.html", {"form1": form1, "form2": form2})


def LoginView(request):
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse("department:department_index"))
			else:
				return HttpResponse("Incorrect Login!")

		else:
			return HttpResponse("Incorrect Login!")
	else:
		context = {}
		return render(request, "main/login.html", context)



def BriefPsnView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		address = request.POST.get("address")
		phone = request.POST.get("phone")
		email = request.POST.get("email")

		client_id = ray_randomizer(4, 10)

		client = Client.objects.create(name=name, address=address, phone=phone, email=email, client_id=client_id)
		client.save()
		
		#return HttpResponse(client.name)
		return HttpResponseRedirect(reverse("main:brief_job", args=(client.id,)))


	else:
		context = {}
		return render(request, "main/brief_psn.html", context)



def BriefJobView(request, client_id):
	if request.method == "POST":
		client = Client.objects.get(id=client_id)

		description = request.POST.get("description")
		payment_mode = request.POST.get("payment_mode")
		awareness = request.POST.get("awareness")
		min_price = request.POST.get("min_price")
		max_price = request.POST.get("max_price")
		time_range = request.POST.get("time_range")
		terms = request.POST.get("terms")

		brief = Brief.objects.create(client=client, description=description, payment_mode=payment_mode, awareness=awareness, min_price=min_price, max_price=max_price, time_range=time_range, terms=terms)
		brief.save()

		return HttpResponseRedirect(reverse("main:brief_opt", args=(brief.id,)))


	else:
		context = {}
		return render(request, "main/brief_job.html", context)





def BriefOptView(request, brief_id):
	if request.method == "POST":
		brief = Brief.objects.get(id=brief_id)

		drawal_type = ""
		cabinet_type = ""

		brief.board = request.POST.get("board_type")
		brief.accessories = request.POST.get("accessories")
		brief.bed_type = request.POST.get("bed_type")
		brief.sofa_seats = request.POST.get("sofa_seats")

		if str(request.POST.get("pedestral_drawal")) == "on":
			drawal_type += "Pedestral drawal,"
			#return HttpResponse("yuji")
		if request.POST.get("side_drawal") == "on":
			drawal_type += "Side drawal,"
		if request.POST.get("open_shelf") == "on":
			drawal_type += "Open shelf,"

		if request.POST.get("upper") == "on":
			cabinet_type += "Upper,"
		if request.POST.get("lower") == "on":
			cabinet_type += "Lower,"

		brief.drawal_type = drawal_type
		brief.cabinet_type = cabinet_type

		brief.save()
		#return HttpResponse(request.POST.get("pedestral_drawal"))

		return HttpResponseRedirect(reverse("main:brief_psn"))



	else:
		context = {}
		return render(request, "main/brief_opt.html", context)





def UserLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("main:login"))
