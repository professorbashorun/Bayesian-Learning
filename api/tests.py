# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.



import unittest
import bbn




class HorseIDBayesianNetworkTest(unittest.TestCase):
	"""docstring for BayesianNetwork"""



	def build(self):
		request = None;
		self.assertEquals(bbn.build(request), True);



	def run(self):
		request = None;
		self.assertEquals(bbn.run(request),	True);




	def update(self):
		request = None;
		self.assertEquals(bbn.update_model(request), True);




	def initialise_space(self):
		request = None;
		self.assertEquals(bbn.initialise_space(request), True);




	def define_universe(self):
		request = None;
		self.assertEquals(bbn.define_universe(request), True);




	def clear_values(self):
		request = None;
		self.assertEquals(bbn.clear_values(request), True);




	def use_default_values(self):
		request = None;
		self.assertEquals(bbn.use_default_values(request), True);



	def declare_variables(self):
		request = None;
		self.assertEquals(bbn.declare_variables(request), True);




	def update_values(self):
		request = None;
		self.assertEquals(bbn.update_values(request), True);




	def load_sizes(self):
		request = None;
		self.assertEquals(bbn.load_sizes(request), True);




	def define_evidence(self):
		request = None;
		self.assertEquals(bbn.define_evidence(request), True);




	def define_cpds(self):
		request = None;
		self.assertEquals(bbn.define_cpds(request), True);




	def load_cpds(self):
		request = None;
		self.assertEquals(bbn.define_cpds(request), True);




	def draw_default_graph(self):
		request = None;
		self.assertEquals(bbn.draw_default_graph(request), True);




	def draw_graph(self):
		request = None;
		self.assertEquals(bbn.draw_graph(request), True);




	def build_model(self):
		request = None;
		self.assertEquals(bbn.build_model(request), True);




	def load_cpds_to_model(self):
		request = None;
		self.assertEquals(bbn.load_cpds_to_model(request), True);



	def load_model(self):
		request = None;
		self.assertEquals(bbn.load_model(request), True);



	def train_model(self):
		request = None;
		self.assertEquals(bbn.train_model(request), True);



	def test_model(self):
		request = None;
		self.assertEquals(bbn.test_model(request), True);



	def update_model(self):
		request = None;
		self.assertEquals(bbn.update_model(request), True);


	def describe_node(self):
		request = None;
		self.assertEquals(bbn.describe_node(request), True);



	def check_model(self):
		request = None;
		self.assertEquals(bbn.check_model(request), True);



	def get_nodes(self):
		request = None;
		self.assertEquals(bbn.get_nodes(request),  True);




	def get_edges(self):
		request = None;
		self.assertEquals(bbn.get_edges(request), True);



	def get_cpds(self):
		request = None;
		self.assertEquals(bbn.get_cpds(request), True);



	def get_cardinality(self):
		request = None;
		self.assertEquals(bbn.get_cardinality(request), True);




	def get_local_independencies(self):
		request = None;
		self.assertEquals(bbn.get_local_independencies(request), True);



	def get_active_trail_nodes(self):
		request = None;
		self.assertEquals(bbn.get_active_trail_nodes(request), True);



	def query(self):
		request = None;
		self.assertEquals(bbn.query(request), True);



	def map_query(self):
		request = None;
		self.assertEquals(bbn.map_query(request), True);







	def test_all(self):
		request = None;
		return {
		"build": 					self.build(request),
		"run":						self.run(request),
		"update":					self.update(request),
		"initialise_space":			self.initialise_space(request),
		"define_universe":			self.define_universe(request),
		"clear_values":				self.clear_values(request),
		"use_default_values":		self.use_default_values(request),
		"declare_variables":		self.declare_variables(request),
		"update_values":			self.update_values(request),
		"load_sizes":				self.load_sizes(request),
		"define_evidence":			self.define_evidence(request),
		"define_cpds":				self.define_cpds(request),
		"load_cpds":				self.load_cpds(request),
		"draw_default_graph":		self.draw_default_graph(request),
		"draw_graph":				self.draw_graph(request),
		"build_model":				self.build_model(request),
		"load_cpds_to_model":		self.load_cpds_to_model(request),
		"load_model":				self.load_model(request),
		"train_model":				self.train_model(request),
		"test_model":				self.test_model(request),
		"update_model":				self.update_model(request),
		"describe_node":			self.describe_node(request),
		"check_model":				self.check_model(request),
		"get_nodes":				self.get_nodes(request),
		"get_edges":				self.get_edges(request),
		"get_cardinality":			self.get_cardinality(request),
		"get_local_independencies":	self.get_local_independencies(request),
		"get_active_trail_nodes":	self.get_active_trail_nodes(request),
		"query":					self.query(request),
		"map_query":				self.map_query(request)
		}

