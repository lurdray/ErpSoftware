from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Department(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=150, default="none")
	head = models.CharField(max_length=150, default="none")
	department_id = models.CharField(max_length=150, default="none")
	time_rate = models.IntegerField(default=0)

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.head
	