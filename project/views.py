from django.shortcuts import render
from department.models import Department
from project.models import Project, Comment, ProjectCommentConnector, PImage, BriefPImageConnector
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from main.views import RayBringSec
import datetime as ray_datetime
from datetime import date, datetime


# Create your views here.
def AddProjectView(request):
	if request.method == "POST":
		pass


	else:
		page_title = "Add Project"
		context = {"page_title": page_title}
		return render(request, "project/add_project.html", context)


		comment = Comment.objects.create(name=name, comment=comment, pub_date=pub_date)
		comment.save()
		post = get_object_or_404(Post, slug=slug)
		pc = PostCommentConnector(post=post, comment=comment, pub_date=pub_date)
		pc.save()



################comments shit
def CommentView(request, project_id):
	department = Department.objects.get(user__pk=request.user.id)
	project = Project.objects.get(id=project_id)
	if request.method == "POST":
		title = request.POST.get("title")
		project_comment = request.POST.get("project_comment")

		comment = Comment.objects.create(title=title, comment=project_comment, commenter=department.name)
		comment.save

		pc = ProjectCommentConnector(project=project, comment=comment)
		pc.save()


		page_title = "Comments for Project"
		comments = project.comments.order_by("-pub_date")

		context = {"page_title": page_title, "department": department, "project": project, "comments": comments}
		return render(request, "project/comment.html", context)



	else:
		page_title = "Comment for Project"
		comments = project.comments.order_by("-pub_date")

		context = {"page_title": page_title, "department": department, "project": project, "comments": comments}
		return render(request, "project/comment.html", context)

###################################


def GalleryView(request, project_id):
	department = Department.objects.get(user__pk=request.user.id)
	project = Project.objects.get(id=project_id)
	if request.method == "POST":
		pass

	else:
		page_title = "Project Images"
		project_images = project.brief.images.order_by("-pub_date")

		
		context = {"page_title": page_title, "department": department, "project": project, "project_images": project_images}
		return render(request, "project/gallery.html", context)








def ProjectDetailView(request, project_id):
	department = Department.objects.get(user__pk=request.user.id)
	project = Project.objects.get(id=project_id)
	brief = project.brief

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

		try:


			if department.name == "cutting":
				cutting_detail = request.POST.get("cutting_detail")
				if cutting_detail == "on":
					if project.cutting_detail == True:
						pass
					else:
						project.cutting_detail = True
						cutting_rtime = datetime.now()
						project.cutting_rtime = cutting_rtime
						if project.project_type == "not_upholstery":
							project.status += 4
						else:
							pass

				else:
					pass

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))



			elif department.name == "cutlist":
				optimized_production_drawing = request.FILES["optimized_production_drawing"]
				if project.optimized_production_drawing:
					pass
				else:
					if project.project_type == "not_upholstery":
						project.status += 20
					else:
						pass

				cutlist_rtime = datetime.now()
				project.cutlist_rtime = cutlist_rtime
				project.optimized_production_drawing = optimized_production_drawing
				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))


			elif department.name == "material-estimate":
				material_estimate = request.FILES["material_estimate"]
				if project.material_estimate:
					pass
				else:
					if project.project_type == "not_upholstery":
						project.status += 20
					else:
						project.status += 2

				materials_rtime = datetime.now()
				project.materials_rtime = materials_rtime
				project.material_estimate = material_estimate
				
				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))


			elif department.name == "store":
				try:
					material_requested = request.FILES["material_requested"]
					if project.material_requested:
						pass
					else:
						if project.project_type == "not_upholstery":
							project.status += 6.67
						else:
							project.status += 2

					project.material_requested = material_requested
					store_requested_rtime = datetime.now()
					project.store_requested_rtime = store_requested_rtime
					
		


				except:
					pass

				try:
					material_issued = request.FILES["material_issued"]
					if project.material_issued:
						pass
					else:
						if project.project_type == "not_upholstery":
							project.status += 6.67
						else:
							project.status += 2

					project.material_issued = material_issued
					store_issued_rtime = datetime.now()
					project.store_issued_rtime = store_issued_rtime
					

				except:
					pass

				project.save()
				return HttpResponseRedirect(reverse("project:all_project"))


			elif department.name == "supply-chain":
				supply_chain_detail = request.POST.get("supply_chain_detail")
				if supply_chain_detail == "on":
					if project.supply == True:
						pass
					else:
						project.supply = True
						supply_rtime = datetime.now()
						project.supply_rtime = supply_rtime
						if project.project_type == "not_upholstery":
							project.status += 6.67
						else:
							project.status += 2

				else:
					pass

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))



			elif department.name == "edge-banding":
				edge_banding_detail = request.POST.get("edge_banding_detail")
				if edge_banding_detail == "on":
					if project.edge_banding_detail == True:
						pass
					else:
						project.edge_banding_detail = True
						edge_banding_rtime = datetime.now()
						project.edge_banding_rtime = edge_banding_rtime
						if project.project_type == "not_upholstery":
							project.status += 4
						else:
							pass


				else:
					pass


				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))

			elif department.name == "cnc":
				cnc_detail = request.POST.get("cnc_detail")
				if cnc_detail == "on":
					if project.cnc_detail == True:
						pass
					else:
						project.cnc_detail = True
						cnc_rtime = datetime.now()
						project.cnc_rtime = cnc_rtime
						if project.project_type == "not_upholstery":
							project.status += 4
						else:
							pass


				else:
					pass

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))


			elif department.name == "assembly":
				assembly_detail = request.POST.get("assembly_detail")
				if assembly_detail == "on":
					if project.assembly == True:
						pass
					else:
						project.assembly = True        
						assembly_rtime = datetime.now()
						project.assembly_rtime = assembly_rtime     
						if project.project_type == "not_upholstery":   
							project.status += 4
						else:
							pass
	                               

				else:
					pass

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))



			elif department.name == "cleaning":
				cleaning = request.POST.get("cleaning")
				if cleaning == "on":
					if project.cleaning == True:
						pass
					else:
						project.cleaning = True
						cleaning_rtime = datetime.now()
						project.cleaning_rtime = cleaning_rtime
						if project.project_type == "not_upholstery":
							project.status += 4
						else:
							project.status += 5

				else:
					pass

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))


			elif department.name == "dispatch":
				dispatch = request.POST.get("dispatch")
				if dispatch == "on":
					if project.dispatch == True:
						pass
					else:
						project.dispatch = True
						dispatch_rtime = datetime.now()
						project.dispatch_rtime = dispatch_rtime
						if project.project_type == "not_upholstery":
							project.status += 11
						else:
							project.status += 5

				else:
					pass

				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))



			elif department.name == "installation":
				installation = request.POST.get("installation")
				if installation == "on":
					if project.installation == True:
						pass
					else:
						project.installation = True
						installation_rtime = datetime.now()
						project.installation_rtime = installation_rtime
						if project.project_type == "not_upholstery":
							project.status += 11
						else:
							project.status += 5

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
					u_design_quotation = request.FILES["u_design_quotation"]
					if project.u_design_quotation:
						pass
					else:
						project.status += 2
					project.u_design_quotation = u_design_quotation
					u_design_rtime = datetime.now()
					project.u_design_rtime = u_design_rtime
					project.save()

				except:
					pass

				try:
					u_production_drawing = request.FILES["u_production_drawing"]
					if project.u_production_drawing:
						pass
					else:
						project.status += 2
					project.u_production_drawing = u_production_drawing
					cutlist_rtime = datetime.now()
					project.cutlist_rtime = cutlist_rtime
					project.save()

				except:
					pass


				if u_frame == "on":
					if project.u_frame == True:
						pass
					else:
						project.status += 2
					project.u_frame = True
					frame_rtime = datetime.now()
					project.frame_rtime = frame_rtime
					project.save()


				if carpenter == "on":
					if project.carpenter == True:
						pass
					else:
						project.status += 28
					project.carpenter = True
					carpenter_rtime = datetime.now()
					project.carpenter_rtime = carpenter_rtime
					project.save()

				if foaming == "on":
					if project.foaming == True:
						pass
					else:
						project.status += 10
					project.foaming = True
					foaming_rtime = datetime.now()
					project.foaming_rtime = foaming_rtime
					project.save()

				if tailoring == "on":
					if project.tailoring == True:
						pass
					else:
						project.status += 21
					project.tailoring = True
					tailoring_rtime = datetime.now()
					project.tailoring_rtime = tailoring_rtime
					project.save()

				if tacking == "on":
					if project.tacking == True:
						pass
					else:
						project.status += 10
					project.tacking = True
					tacking_rtime = datetime.now()
					project.tacking_rtime = tacking_rtime
					project.save()


				if spraying == "on":
					if project.spray == True:
						pass
					else:
						project.status += 2
					project.spray = True
					spray_rtime = datetime.now()
					project.spray_rtime = spray_rtime
					project.save()



				project.save()

				return HttpResponseRedirect(reverse("project:all_project"))

		except:
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

		if department.name == "project-service" or department.name == "ict":
			projects = Project.objects.order_by("-pub_date")

		else:
			if department.name == "cutlist":
				projects = Project.objects.filter(project_type="not_upholstery").order_by("-pub_date")


			elif department.name == "material-estimate":
				projects = []
				for project in Project.objects.order_by("-pub_date"):
					if project.project_type == "upholstery":
						if project.status >= 4:
							projects.append(project)
					else:
						if project.status >= 20:
							projects.append(project)




			elif department.name == "store":
				projects = []
				for project in Project.objects.order_by("-pub_date"):
					if project.project_type == "upholstery":
						if project.status >= 6:
							projects.append(project)
					else:
						if project.status >= 40:
							projects.append(project)



			elif department.name == "supply-chain":
				projects = []
				for project in Project.objects.order_by("-pub_date"):
					if project.project_type == "upholstery":
						if project.status >= 8:
							projects.append(project)
					else:
						if project.status >= 46:
							projects.append(project)


			#########not upholstery

			elif department.name == "cutting":
				projects = []
				for project in Project.objects.filter(project_type="not_upholstery"):
					if project.status >= 52 or project.status >= 58:
							projects.append(project)

			elif department.name == "edge-banding":
				projects = []
				for project in Project.objects.filter(project_type="not_upholstery"):
					if project.status >= 56 or project.status >= 62:
							projects.append(project)

			elif department.name == "cnc":
				projects = []
				for project in Project.objects.filter(project_type="not_upholstery"):
					if project.status >= 60 or project.status >= 66:
							projects.append(project)

			elif department.name == "assembly":
				projects = []
				for project in Project.objects.filter(project_type="not_upholstery"):
					if project.status >=64 or project.status >= 70:
							projects.append(project)



			#############upholstery

			elif department.name == "upholstery":
				projects = Project.objects.filter(project_type="upholstery")




			elif department.name == "cleaning":
				projects = []
				for project in Project.objects.order_by("-pub_date"):
					if project.project_type == "upholstery":
						if project.status >= 83 or project.status >= 85:
							projects.append(project)
					else:
						if project.status >= 68 or project.status >= 74:
							projects.append(project)


			elif department.name == "dispatch":
				projects = []
				for project in Project.objects.order_by("-pub_date"):
					if project.project_type == "upholstery":
						if project.status >= 88 or project.status >= 90:
							projects.append(project)
					else:
						if project.status >= 72 or project.status >= 78:
							projects.append(project)


			elif department.name == "installation":
				projects = []
				for project in Project.objects.order_by("-pub_date"):
					if project.project_type == "upholstery":
						if project.status >= 93 or project.status >= 95:
							projects.append(project)
					else:
						if project.status >= 83 or project.status >= 89:
							projects.append(project)








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