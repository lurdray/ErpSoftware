from django.db import models
from django.utils import timezone

# Create your models here.

class Ict(models.Model):
	project_id = models.CharField(max_length=150, default="none")
	ict = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.project_id


class Comment(models.Model):
	title = models.CharField(max_length=150, default="none")
	comment = models.TextField()
	commenter = models.CharField(max_length=150, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title




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




class PImage(models.Model):
	project_id = models.CharField(max_length=150, default="none")
	info = models.TextField(default="none")
	image = models.ImageField(upload_to='project/images/', blank=True)
	uploader = models.CharField(max_length=150, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.uploader



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

	images = models.ManyToManyField(PImage, through="BriefPImageConnector", through_fields=("brief", "image"),)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.max_price






class Project(models.Model):
	title = models.CharField(max_length=150, default="none")
	project_id = models.CharField(max_length=150, default="none")
	project_type = models.CharField(max_length=150, default="none")
	delivery_date = models.CharField(max_length=150, default="none")
	delivery_days = models.IntegerField(default=0)
	t_seconds = models.IntegerField(default=0)
	status = models.IntegerField(default=0)
	pub_date = models.DateTimeField(default=timezone.now)

	work_order = models.FileField(upload_to='project/work_order/', blank=True)

	comments = models.ManyToManyField(Comment, through="ProjectCommentConnector", through_fields=("project", "comment"),)

	#images = models.ManyToManyField(PImage, through="ProjectPImageConnector", through_fields=("project", "image"),)
	brief = models.ForeignKey(Brief, on_delete=models.CASCADE, default="")

	optimized_production_drawing = models.FileField(upload_to='project/optimised_production_drawing/', blank=True)

	cutting_detail = models.BooleanField(default=False, blank=True)
	edge_banding_detail = models.BooleanField(default=False, blank=True)
	cnc_detail = models.BooleanField(default=False, blank=True)
	assembly = models.BooleanField(default=False)

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
	material_requested = models.FileField(upload_to='project/material_requested/', blank=True)
	material_issued = models.FileField(upload_to='project/material_issues/', blank=True)
	supply = models.BooleanField(default=False)

	#other details
	cleaning = models.BooleanField(default=False)
	dispatch = models.BooleanField(default=False)
	installation = models.BooleanField(default=False)
	
	frame = models.BooleanField(default=False)
	ict = models.BooleanField(default=False)

	#time span models STANDARD!!!!
	#design_stime = models.CharField(max_length=150, default="none")
	cutlist_stime = models.CharField(max_length=150, default="none")
	materials_stime = models.CharField(max_length=150, default="none")
	store_issued_stime = models.CharField(max_length=150, default="none")
	store_requested_stime = models.CharField(max_length=150, default="none")
	supply_stime = models.CharField(max_length=150, default="none")

	#not upholstery shit
	cutting_stime = models.CharField(max_length=150, default="none")
	edge_banding_stime = models.CharField(max_length=150, default="none")
	cnc_stime = models.CharField(max_length=150, default="none")
	assembly_stime = models.CharField(max_length=150, default="none")

	#upholstery shit
	u_design_stime = models.CharField(max_length=150, default="none")
	frame_stime = models.CharField(max_length=150, default="none") #wood section
	spray_stime = models.CharField(max_length=150, default="none")
	carpenter_stime = models.CharField(max_length=150, default="none")
	foaming_stime = models.CharField(max_length=150, default="none")
	tailoring_stime = models.CharField(max_length=150, default="none")
	tacking_stime = models.CharField(max_length=150, default="none")

	cleaning_stime = models.CharField(max_length=150, default="none")
	dispatch_stime = models.CharField(max_length=150, default="none")
	installation_stime = models.CharField(max_length=150, default="none")


	#time span models REAL!!!!
	cutlist_rtime = models.CharField(max_length=150, default="none")
	materials_rtime = models.CharField(max_length=150, default="none")
	store_issued_rtime = models.CharField(max_length=150, default="none")
	store_requested_rtime = models.CharField(max_length=150, default="none")
	supply_rtime = models.CharField(max_length=150, default="none")

	#not upholstery shit
	cutting_rtime = models.CharField(max_length=150, default="none")
	edge_banding_rtime = models.CharField(max_length=150, default="none")
	cnc_rtime = models.CharField(max_length=150, default="none")
	assembly_rtime = models.CharField(max_length=150, default="none")

	#upholstery shit
	u_design_rtime = models.CharField(max_length=150, default="none")
	frame_rtime = models.CharField(max_length=150, default="none") #wood section
	spray_rtime = models.CharField(max_length=150, default="none")
	carpenter_rtime = models.CharField(max_length=150, default="none")
	foaming_rtime = models.CharField(max_length=150, default="none")
	tailoring_rtime = models.CharField(max_length=150, default="none")
	tacking_rtime = models.CharField(max_length=150, default="none")

	cleaning_rtime = models.CharField(max_length=150, default="none")
	dispatch_rtime = models.CharField(max_length=150, default="none")
	installation_rtime = models.CharField(max_length=150, default="none")




	def __str__(self):
		return self.title




class MaterialEstimateConnector(models.Model):
	material = models.ForeignKey(Material, on_delete=models.CASCADE, default="")
	estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

class BriefPImageConnector(models.Model):
	brief = models.ForeignKey(Brief, on_delete=models.CASCADE, default="")
	image = models.ForeignKey(PImage, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)



class ProjectCommentConnector(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)