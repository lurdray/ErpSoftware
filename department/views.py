from django.shortcuts import render
from department.models import Department
from project.models import Project, Brief, Client, Comment, PImage, BriefPImageConnector
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from main.views import ray_randomizer, RayBringSec, RayConvertDate, RayDateToSec
import datetime as ray_datetime
from datetime import date, datetime



####################
def IndexView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)

		recent_projects = Project.objects.order_by("-pub_date")[:10]
		recent_briefs = Brief.objects.order_by("-pub_date")[:10]
		recent_clients = Client.objects.order_by("-pub_date")[:10]
		recent_comments = Comment.objects.order_by("-pub_date")[:10]

		latest_project = Project.objects.order_by("-pub_date")[:1]
		latest_brief = Brief.objects.order_by("-pub_date")[:1]
		latest_client = Client.objects.order_by("-pub_date")[:1] 
		latest_comment = Comment.objects.order_by("-pub_date")[:1]

		brief_count = Brief.objects.all().count()
		client_count = Client.objects.all().count()
		project_count = Project.objects.all().count()
		comment_count = Comment.objects.all().count()

		try:
			project_one = latest_project[0]
			project_images = project.one.brief.images

		except:
			project_images = None


		context = {"department": department, "page_title": page_title, "recent_projects": recent_projects, "recent_briefs": recent_briefs,
		"recent_clients": recent_clients, "recent_comments": recent_comments, "latest_project": latest_project, "latest_brief": latest_brief, 
		"latest_client": latest_client, "latest_comment": latest_comment, "brief_count": brief_count, "client_count": client_count,
		"project_count": project_count, "comment_count": comment_count, "project_images": project_images
		}
		return render(request, "department/index.html", context)


def TutorialView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)
		context = {"department": department, "page_title": page_title}
		return render(request, "department/tutorial.html", context)



def ProfileView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)
		context = {"department": department, "page_title": page_title}
		return render(request, "department/profile.html", context)



def SettingView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)
		context = {"department": department, "page_title": page_title}
		return render(request, "department/setting.html", context)


def NoficationView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)
		context = {"department": department, "page_title": page_title}
		return render(request, "department/setting.html", context)





def HowItWorksView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)
		context = {"department": department, "page_title": page_title}
		return render(request, "department/hiw.html", context)



########################



def ClientBriefView(request):
	if request.method == "POST":
		pass

	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "Briefs"
		briefs = Brief.objects.all()
		context = {"briefs": briefs, "department": department, "page_title": page_title}
		return render(request, "department/client_brief.html", context)



def BriefDetailView(request, brief_id):
	brief = Brief.objects.get(id=brief_id)
	department = Department.objects.get(user__pk=request.user.id)
	page_title = "Brief from %s" % (brief.client)
	project_id = ray_randomizer(4, 10)
	
	if request.method == "POST":

		try:
			project_image = request.FILES["project_image"]
			info = request.POST.get("info")
			uploader = department.name
			pi = PImage.objects.create(info=info, image=project_image, uploader=uploader)
			pi.save()

			bpi = BriefPImageConnector.objects.create(brief=brief, image=pi)
			bpi.save()

		except:
			pass


		if department.name == "project-service":
			try:
				work_order = request.FILES["work_order"]
				title = request.POST.get("title")
				project_type = request.POST.get("project_type")
				delivery_date = str(request.POST.get("delivery_date"))
				project_id = request.POST.get("project_id")

				#format = 01/23/4534
				d = delivery_date[0]+delivery_date[1]
				m = delivery_date[3]+delivery_date[4]
				y = delivery_date[6]+delivery_date[7]+delivery_date[8]+delivery_date[9]
				delivery_date = RayConvertDate(d,m,y) 

				k1 = datetime(int(y), int(m), int(d))
				#k1 = 
				#k0 = date.today()
				k0 = datetime.now()
				#return HttpResponse(k1)

				delta = k1 - k0
				delivery_seconds = delta.days*24*60*60 + (delta.seconds)
				delivery_days = (delivery_seconds /60/60/24)

				project = Project.objects.create(title=title, work_order=work_order, project_type=project_type, delivery_date=delivery_date, delivery_days=delivery_days, project_id=project_id, brief=brief)

				#return HttpResponse(delivery_days)
				if project_type == "not_upholstery":

					cutlist_stime = k0 + ray_datetime.timedelta(days=0.2*delivery_days)
					materials_stime = k0 + ray_datetime.timedelta(days=0.4*delivery_days)
					#store_requested_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					#store_issued_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					store_requested_stime = k0 + ray_datetime.timedelta(days=0.6*delivery_days)
					store_issued_stime = k0 + ray_datetime.timedelta(days=0.6*delivery_days)
					supply_stime = k0 + ray_datetime.timedelta(days=0.6*delivery_days)

					#not upholstery shit
					cutting_stime = k0 + ray_datetime.timedelta(days=0.8*delivery_days)
					edge_banding_stime = k0 + ray_datetime.timedelta(days=0.8*delivery_days)
					cnc_stime = k0 + ray_datetime.timedelta(days=0.8*delivery_days)
					assembly_stime = k0 + ray_datetime.timedelta(days=0.8*delivery_days)

					cleaning_stime = k0 + ray_datetime.timedelta(days=0.8*delivery_days)
					dispatch_stime = k0 + ray_datetime.timedelta(days=1*delivery_days)
					installation_stime = k0 + ray_datetime.timedelta(days=1*delivery_days)

					project.cutting_stime = cutting_stime
					project.edge_banding_stime = edge_banding_stime
					project.cnc_stime = cnc_stime
					project.assembly_stime = assembly_stime


				elif project_type == "upholstery":
					u_design_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					cutlist_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					materials_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					store_requested_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					store_issued_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					supply_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)

					#upholstery shit
					frame_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days) #wood section 0.2857
					spray_stime = k0 + ray_datetime.timedelta(days=0.1429*delivery_days)
					carpenter_stime = k0 + ray_datetime.timedelta(days=0.4286*delivery_days)
					foaming_stime = k0 + ray_datetime.timedelta(days=0.5716*delivery_days)
					tailoring_stime = k0 + ray_datetime.timedelta(days=0.8574*delivery_days)
					tacking_stime = k0 + ray_datetime.timedelta(days=1*delivery_days)

					cleaning_stime = k0 + ray_datetime.timedelta(days=1*delivery_days)
					dispatch_stime = k0 + ray_datetime.timedelta(days=1*delivery_days)
					installation_stime = k0 + ray_datetime.timedelta(days=1*delivery_days)

					project.u_design_stime = u_design_stime
					project.frame_stime = frame_stime
					project.spray_stime = spray_stime
					project.carpenter_stime = carpenter_stime
					project.foaming_stime = foaming_stime
					project.tailoring_stime = tailoring_stime
					project.tacking_stime = tacking_stime
					

				else:
					pass

				
				project.cutlist_stime = cutlist_stime
				project.materials_stime = materials_stime
				project.store_requested_stime = store_requested_stime
				project.store_issued_stime = store_issued_stime
				
				
				project.supply_stime = supply_stime
				
				project.cleaning_stime = cleaning_stime
				project.dispatch_stime = dispatch_stime
				project.installation_stime = installation_stime

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))
				
			except:
				return HttpResponseRedirect(reverse("project:all_project"))

		elif department.name == "design":
			brief = Brief.objects.get(id=brief.id)
			try:
				design_quotation = request.FILES["design_quotation"]
				brief.design_quotation = design_quotation
				brief.save()
			except:
				pass

			try:
				presentation_drawing = request.FILES["presentation_drawing"]
				brief.presentation_drawing = presentation_drawing
				brief.save()
			except:
				pass

			try:
				production_drawing = request.FILES["production_drawing"]
				brief.production_drawing = production_drawing
				brief.save()
			except:
				pass

			
			
			
			
			brief.save()

			return HttpResponseRedirect(reverse("department:client_brief"))

		elif department.name == "cutlist":
			optimized_production_drawing = request.FILES["optimized_production_drawing"]

			project = Project.objects.get(brief__pk=brief.id)
			project.optimized_production_drawing = optimized_production_drawing
			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))

		else:
			return HttpResponseRedirect(reverse("department:client_brief"))



	else:
		try:
			project = Project.objects.get(brief__pk=brief.id)
			project_detail_id = project.id
			counter = RayBringSec(department.time_rate, project.t_seconds)
			context = {"department": department, "page_title": page_title, "project_id": project_id, "brief": brief, "project_detail_id": project_detail_id, "project": project, "counter": counter}
			return render(request, "department/brief_detail.html", context)

		except:
			#counter = RayBringSec(department.time_rate, project.t_seconds)
			context = {"department": department, "page_title": page_title, "project_id": project_id, "brief": brief}
			return render(request, "department/brief_detail.html", context)





def AddDepartmentView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "department/add_department.html", context)
	



def AllDepartmentView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "department/all_department.html", context)
	


def EditDepartmentView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "department/edit_department.html", context)



def DeleteDepartmentView(request):
	if request.method == "POST":
		pass


	else:
		pass