# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .bbn import HorseIDBayesianNetwork;


bbn = HorseIDBayesianNetwork();
bbn.clear_values(None);
bbn.declere_variables(None);


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
		return str({ bbn.IDENTIFIABILITY:	self.identifiablity,
		bbn.LOCATION:					self.location,
		bbn.CHIP_WORK:					self.chip_work,
		bbn.PASSPORT:					self.passport,
		bbn.PASSPORT_AVAILABLE:			self.passport_available,
		bbn.ID_USING:					self.id_using,
		bbn.ID_VERIFYING:				self.id_verifying,
		bbn.ID_USING_MARKING:			self.id_using_marking,
		bbn.MARKINGS_CORRECT:			self.markings_correct,
		bbn.DISTINCTIVE_TRAITS:			self.distinctive_traits,
		bbn.OWNER_STA:					self.owner_sta,
		bbn.GOOD_ID:					self.good_id });





class Graph(model.Model):
	nodes					= models.Array();
	edges 					= models.Array();

	def __str__(self):
		return str({'nodes': nodes, 'edges':edges});







class FunctionResponse(models.Model):
	"""docstring for FunctionResponse"""
	state 					= models.BooleanField(default=False);
	status					= models.BooleanField(default=False);
	data	 				= models.CharField(max_length=100, blank=True, default='');

	def __str__(self):
		return str({'state': state, 'status':status, 'data':data});
		









