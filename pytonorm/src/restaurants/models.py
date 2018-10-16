from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	Name = models.CharField(max_length=120)
	Description = models.TextField(default='Description Not Provided')
	Location = models.TextField(max_length=120, null=True, blank=True)