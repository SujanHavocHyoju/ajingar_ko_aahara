# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import profile
	# note, we import the profile class,  not the profiles directory

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)
		
