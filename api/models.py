# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Variables(models.Model):
	"""docstring for HorseIdBayesian"""

	identifiablity 			= models.BooleanField(default=False);
	location 				= models.IntegerField();
	chip_work				= models.BooleanField(default=False);
	passport 				= models.BooleanField(default=False);
	passport_available 		= models.BooleanField(default=False);
	id_using 				= models.BooleanField(default=False);
	id_verifying 			= models.BooleanField(default=False);
	id_using_marking 		= models.BooleanField(default=False);
	markings_correct 		= models.BooleanField(default=False);
	distinctive_traits 		= models.BooleanField(default=False);
	owner_sta 				= models.BooleanField(default=False);
	good_id 				= models.BooleanField(default=False);

	def __str__(self):
		return self.good_id;





class FunctionResponse(models.Model):
	"""docstring for FunctionResponse"""
	state 					= models.BooleanField(default=False);
	status					= models.BooleanField(default=False);
	data	 				= models.CharField(max_length=100, blank=True, default='');

	def __str__(self):
		return self.state;
		









