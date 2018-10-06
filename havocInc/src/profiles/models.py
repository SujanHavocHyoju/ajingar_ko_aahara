# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	Name = models.CharField(max_length=120)
	Description = models.TextField(default='Description Not Provided')
									# or null=True
#	Location = models.CharField(max_length=120, default='Location Not Provided', blank=True, null=True)
#	Job = models.CharField(max_length=120, null=True)

	def __unicode__(self):
		return self.Name