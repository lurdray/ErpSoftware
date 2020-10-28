from django.shortcuts import render
from department.models import Department
from project.models import Project
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from main.views import RayBringSec


# Create your views here.
def AddProjectView(request):
	if request.method == "POST":
		pass


	else:
		page_title = "Add Project"
		context = {"page_title": page_title}
		return render(request, "project/add_project.html", context)



def ProjectDetailView(request, project_id):
	department = Department.objects.get(user__pk=request.user.id)
	project = Project.objects.get(id=project_id)
	if request.method == "POST":

		if department.name == "cutting":
			cutting_detail = request.POST.get("cutting_detail")
			if cutting_detail == "on":
				project.cutting_detail = True

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))



		elif department.name == "cutlist":
			optimized_production_drawing = request.FILES["optimized_production_drawing"]
			project.optimized_production_drawing = optimized_production_drawing
			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))


		elif department.name == "material-estimate":
			material_estimate = request.FILES["material_estimate"]
			project.material_estimate = material_estimate
			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))



		elif department.name == "edge-banding":
			edge_banding_detail = request.POST.get("edge_banding_detail")
			if edge_banding_detail == "on":
				project.edge_banding_detail = True

			else:
				pass


			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))

		elif department.name == "cnc":
			cnc_detail = request.POST.get("cnc_detail")
			if cnc_detail == "on":
				project.cnc_detail = True

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))


		elif department.name == "assembly":
			assembly_detail = request.POST.get("assembly_detail")
			if assembly_detail == "on":
				project.assembly = True                                               

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))



		elif department.name == "cleaning":
			cleaning = request.POST.get("cleaning")
			if cleaning == "on":
				project.cleaning = True

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))


		elif department.name == "dispatch":
			dispatch = request.POST.get("dispatch")
			if dispatch == "on":
				project.dispatch = True

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))



		elif department.name == "installation":
			installation = request.POST.get("installation")
			if installation == "on":
				project.installation = True

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))



		elif department.name == "ict":
			ict = request.POST.get("ict")
			if ict == "on":
				project.ict = True

			else:
				pass

			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))


		elif department.name == "upholstery":

			#u_design_quotation = request.FILES["u_design_quotation"]
			#u_production_drawing = request.FILES["u_production_drawing"]

			u_frame = request.POST.get("u_frame")
			carpenter = request.POST.get("carpenter")
			foaming = request.POST.get("foaming")
			tailoring = request.POST.get("tailoring")
			tacking = request.POST.get("tacking")
			spraying = request.POST.get("spraying")


			try:
				project.u_design_quotation = request.FILES["u_design_quotation"]
				project.save()

			except:
				pass

			try:
				project.u_production_drawing = request.FILES["u_production_drawing"]
				project.save()

			except:
				pass


			if u_frame == "on":
				project.u_frame = True
				project.save()


			if carpenter == "on":
				project.carpenter = True
				project.save()

			if foaming == "on":
				project.foaming = True
				project.save()

			if tailoring == "on":
				project.tailoring = True
				project.save()

			if tacking == "on":
				project.tacking = True
				project.save()


			if spraying == "on":
				project.spray = True
				project.save()



			project.save()

			return HttpResponseRedirect(reverse("project:all_project"))









	else:
		#return HttpResponse(project.delivery_date)
		page_title = "%s Project Detail" % (project.title)
		counter = RayBringSec(department.time_rate, project.t_seconds)

		context = {"page_title": page_title, "project": project, "department": department, "counter": counter}
		return render(request, "project/project_detail.html", context)


def AllProjectView(request):
	if request.method == "POST":
		pass


	else:
		page_title = "Projects"
		department = Department.objects.get(user__pk=request.user.id)
		if department.name == "upholstery":
			projects = Project.objects.filter(project_type="upholstery")

		elif department.name == "project-service" or department.name == "cleaning" or department.name == "dispatch" or department.name == "installation" :
			projects = Project.objects.all()

		else:
			projects = Project.objects.filter(project_type="not_upholstery")
		
		context = {"projects": projects, "department": department, "page_title": page_title}
		return render(request, "project/all_project.html", context)
		


def EditProjectView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "project/edit_project.html", context)
	



def DeleteProjectView(request):
	if request.method == "POST":
		pass


	else:
		pass