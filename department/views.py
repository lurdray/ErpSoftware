from django.shortcuts import render
from department.models import Department
from project.models import Project, Brief
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from main.views import ray_randomizer, RayBringSec, RayConvertDate


def IndexView(request):
	if request.method == "POST":
		pass


	else:
		department = Department.objects.get(user__pk=request.user.id)
		page_title = "%s department" % (department.name)
		context = {"department": department, "page_title": page_title}
		return render(request, "department/index.html", context)




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

		if department.name == "project-service":
			title = request.POST.get("title")
			work_order = request.FILES["work_order"]
			project_type = request.POST.get("project_type")
			delivery_date = str(request.POST.get("delivery_date"))
			project_id = request.POST.get("project_id")

			#format = 01/23/4534
			d = delivery_date[0]+delivery_date[1]
			m = delivery_date[3]+delivery_date[4]
			y = delivery_date[6]+delivery_date[7]+delivery_date[8]+delivery_date[9]
			delivery_date = RayConvertDate(d,m,y)

			#delivery_date_hour = RayDateToSec(datetime.datetime(int(y), int(m), int(d), 12, 00, 00))

			project = Project.objects.create(title=title, work_order=work_order, project_type=project_type, delivery_date=delivery_date, project_id=project_id, brief=brief)
			project.save()

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