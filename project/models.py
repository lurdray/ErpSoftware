from django.db import models
from django.utils import timezone

# Create your models here.

class Ict(models.Model):
	project_id = models.CharField(max_length=150, default="none")
	ict = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.project_id




class Material(models.Model):
	name = models.CharField(max_length=150, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name


class Estimate(models.Model):
	materials = models.ManyToManyField(Material, through="MaterialEstimateConnector", through_fields=("estimate", "material"),)
	total_price = models.IntegerField(blank=True, null=True)
	item_count = models.IntegerField(blank=True, null=True)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.total_price


class Client(models.Model):
	name = models.CharField(max_length=150, default="none")
	phone = models.CharField(max_length=150, default="none")
	email = models.CharField(max_length=150, default="none")
	address = models.TextField()
	client_id = models.CharField(max_length=150, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name


class Brief(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
	description = models.TextField()
	payment_mode = models.CharField(max_length=150, default="none")
	awareness = models.CharField(max_length=150, default="none")
	min_price = models.CharField(max_length=150, default="none")
	max_price = models.CharField(max_length=150, default="none")
	time_range = models.CharField(max_length=150, default="none")
	terms = models.TextField()
	board = models.CharField(max_length=150, default="none")
	accessories = models.CharField(max_length=150, default="none")
	bed_type = models.CharField(max_length=150, default="none")
	cabinet_type = models.CharField(max_length=150, default="none")
	sofa_seats = models.IntegerField(blank=True, null=True)
	drawal_type = models.CharField(max_length=150, default="none")

	design_quotation = models.FileField(upload_to='project/design_quotation/', blank=True)
	presentation_drawing = models.FileField(upload_to='project/presentation_drawing/', blank=True)
	production_drawing = models.FileField(upload_to='project/production_drawing/', blank=True)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.max_price





class ProjectImage(models.Model):
	project_id = models.CharField(max_length=150, default="none")
	image = models.ImageField(upload_to='project/images/', blank=True)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.project_id



class Project(models.Model):
	title = models.CharField(max_length=150, default="none")
	project_id = models.CharField(max_length=150, default="none")
	project_type = models.CharField(max_length=150, default="none")
	delivery_date = models.CharField(max_length=150, default="none")
	t_seconds = models.IntegerField(default=0)
	status = models.CharField(max_length=150, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	work_order = models.FileField(upload_to='project/work_order/', blank=True)

	images = models.ManyToManyField(ProjectImage, through="ProjectImageConnector", through_fields=("project", "image"),)
	brief = models.ForeignKey(Brief, on_delete=models.CASCADE, default="")

	optimized_production_drawing = models.FileField(upload_to='project/optimised_production_drawing/', blank=True)

	cutting_detail = models.BooleanField(default=False, blank=True)
	edge_banding_detail = models.BooleanField(default=False, blank=True)
	cnc_detail = models.BooleanField(default=False, blank=True)

	#upholstery details
	u_design_quotation = models.FileField(upload_to='project/u_design_quotation/', blank=True)
	u_production_drawing = models.FileField(upload_to='project/u_production_drawing/', blank=True)
	u_frame = models.BooleanField(default=False)
	#upholstery_detail =  models.ForeignKey(Upholstery, on_delete=models.CASCADE, blank=True, null=True)
	
	carpenter = models.BooleanField(default=False)
	foaming = models.BooleanField(default=False)
	tailoring = models.BooleanField(default=False)
	tacking = models.BooleanField(default=False)

	spray = models.BooleanField(default=False)


	material_estimate = models.FileField(upload_to='project/material_estimate/', blank=True)



	#other details
	#material_estimate_id = models.CharField(max_length=150, default="none")
	assembly = models.BooleanField(default=False)
	cleaning = models.BooleanField(default=False)
	dispatch = models.BooleanField(default=False)
	installation = models.BooleanField(default=False)
	
	frame = models.BooleanField(default=False)
	ict = models.BooleanField(default=False)



	def __str__(self):
		return self.title




class MaterialEstimateConnector(models.Model):
	material = models.ForeignKey(Material, on_delete=models.CASCADE, default="")
	estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

class ProjectImageConnector(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
	image = models.ForeignKey(ProjectImage, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)
