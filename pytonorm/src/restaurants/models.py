from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='Description Not Provided')
	location = models.CharField(max_length=120, null=True, blank=True)
	category = models.CharField(max_length=120, null=True, blank=True)
	added_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	#my_date = models.DateTimeField(auto_now=False, auto_now_add=False)