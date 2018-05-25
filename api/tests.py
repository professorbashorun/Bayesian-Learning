# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.



import unittest
import bbn




class HorseIDBayesianNetworkTest(unittest.TestCase):
	"""docstring for BayesianNetwork"""



	def build(self):#request=void
		request = None;
		self.assertEquals(bbn.build(request), True);



	def run(self)::#request=void
		request = None;
		self.assertEquals(bbn.run(request),	True);




	def update(self):#request={data:{'variable1': values1, ... 'variableN': valuesN }, 'graph': [(variable1_i, variable1_j),(variable2_i, variable2_j),,}
		request = {'data': {
			bbn.IDENTIFIABILITY:	[[]],		bbn.LOCATION:			[[]],		bbn.CHIP_WORK:			[[]],
			bbn.CHIPPED:			[[]],		bbn.PASSPORT:			[[]],		bbn.PASSPORT_AVAILABLE:	[[]],
			bbn.ID_USING:			[[]],		bbn.ID_VERIFYING:		[[]],		bbn.ID_USING_MARKING:	[[]],
			bbn.MARKINGS_CORRECT:	[[]],		bbn.DISTINCTIVE_TRAITS:	[[]],		bbn.OWNER_STA:			[[]],
			bbn.GOOD_ID:			[[]]
			},
			'graph':[]
		};
		self.assertEquals(bbn.update_model(request), True);




	def initialise_space(self):#request=void
		request = None;
		self.assertEquals(bbn.initialise_space(request), True);




	def define_universe(self):#request=void
		request = None;
		self.assertEquals(bbn.define_universe(request), True);




	def clear_values(self):#request=void
		request = None;
		self.assertEquals(bbn.clear_values(request), True);




	def use_default_values(self):#request=void
		request = None;
		self.assertEquals(bbn.use_default_values(request), True);



	def declare_variables(self):#request=void
		request = None;
		self.assertEquals(bbn.declare_variables(request), True);




	def update_values(self):#request={data:{'variable1': values1, ... 'variableN': valuesN }}
		request={'data': {
			bbn.IDENTIFIABILITY:	[[]],		bbn.LOCATION:			[[]],		bbn.CHIP_WORK:			[[]],
			bbn.CHIPPED:			[[]],		bbn.PASSPORT:			[[]],		bbn.PASSPORT_AVAILABLE:	[[]],
			bbn.ID_USING:			[[]],		bbn.ID_VERIFYING:		[[]],		bbn.ID_USING_MARKING:	[[]],
			bbn.MARKINGS_CORRECT:	[[]],		bbn.DISTINCTIVE_TRAITS:	[[]],		bbn.OWNER_STA:			[[]],
			bbn.GOOD_ID:			[[]]
			}
		};
		self.assertEquals(bbn.update_values(request), True);




	def load_sizes(self):#request=void
		request = None;
		self.assertEquals(bbn.load_sizes(request), True);




	def define_evidence(self):#request=void
		request = None;
		self.assertEquals(bbn.define_evidence(request), True);




	def define_cpds(self):#request=void
		request = None;
		self.assertEquals(bbn.define_cpds(request), True);




	def load_cpds(self):#request=void
		request = None;
		self.assertEquals(bbn.define_cpds(request), True);




	def draw_default_graph(self):#request=void
		request = None;
		self.assertEquals(bbn.draw_default_graph(request), True);




	def draw_graph(self):#request={'graph': [(A1,B1),(A2,B2), ... (AN,BN),]}
		request = {'graph': []};
		self.assertEquals(bbn.draw_graph(request), True);




	def build_model(self):#request=void
		request = None;
		self.assertEquals(bbn.build_model(request), True);




	def load_cpds_to_model(self):#request=void
		request = None;
		self.assertEquals(bbn.load_cpds_to_model(request), True);



	def load_model(self):#request=void
		request = None;
		self.assertEquals(bbn.load_model(request), True);



	def train_model(self):#request={data:{'variable1': values1, ... 'variableN': valuesN }, 'graph': [(variable1_i, variable1_j),(variable2_i, variable2_j),,}
		request = {'data': {
			bbn.IDENTIFIABILITY:	[[]],		bbn.LOCATION:			[[]],		bbn.CHIP_WORK:			[[]],
			bbn.CHIPPED:			[[]],		bbn.PASSPORT:			[[]],		bbn.PASSPORT_AVAILABLE:	[[]],
			bbn.ID_USING:			[[]],		bbn.ID_VERIFYING:		[[]],		bbn.ID_USING_MARKING:	[[]],
			bbn.MARKINGS_CORRECT:	[[]],		bbn.DISTINCTIVE_TRAITS:	[[]],		bbn.OWNER_STA:			[[]],
			bbn.GOOD_ID:			[[]]
			},
			'graph':[]
		};
		self.assertEquals(bbn.train_model(request), True);



	def test_model(self):#
		request = None;
		self.assertEquals(bbn.test_model(request), True);



	def update_model(self):#request={data:{'variable1': values1, ... 'variableN': valuesN }, 'graph': [(variable1_i, variable1_j),(variable2_i, variable2_j),,}
		request = {'data': {
			bbn.IDENTIFIABILITY:	[[]],		bbn.LOCATION:			[[]],		bbn.CHIP_WORK:			[[]],
			bbn.CHIPPED:			[[]],		bbn.PASSPORT:			[[]],		bbn.PASSPORT_AVAILABLE:	[[]],
			bbn.ID_USING:			[[]],		bbn.ID_VERIFYING:		[[]],		bbn.ID_USING_MARKING:	[[]],
			bbn.MARKINGS_CORRECT:	[[]],		bbn.DISTINCTIVE_TRAITS:	[[]],		bbn.OWNER_STA:			[[]],
			bbn.GOOD_ID:			[[]]
			},
			'graph':[]
		};
		self.assertEquals(bbn.update_model(request), True);


	def describe_node(self):#request={'node':value}
		request = {'node': []};
		self.assertEquals(bbn.describe_node(request), True);



	def check_model(self):#request=void
		request = None;
		self.assertEquals(bbn.check_model(request), True);



	def get_nodes(self):
		request = None;
		self.assertEquals(bbn.get_nodes(request),  True);




	def get_edges(self):
		request = None;
		self.assertEquals(bbn.get_edges(request), True);



	def get_cpds(self):#request={'node':value}
		request = None;
		self.assertEquals(bbn.get_cpds(request), True);



	def get_cardinality(self):#request={'node':value}
		request = {'node': []};
		self.assertEquals(bbn.get_cardinality(request), True);




	def get_local_independencies(self):#request={'variables':values}
		request = {'variables': []};
		self.assertEquals(bbn.get_local_independencies(request), True);



	def get_active_trail_nodes(self):#request={'variables':values, 'observed':values}
		request={'variables':[], 'observed':[]}
		self.assertEquals(bbn.get_active_trail_nodes(request), True);



	def query(self):#request={'variables':value, 'evidence':value, 'elimination_order':value}
		request={'variables':[], 'evidence':[], 'elimination_order':[]}
		self.assertEquals(bbn.query(request), True);



	def map_query(self):#request={'variables':value, 'evidence':value, 'elimination_order':value}
		request={'variables':[], 'evidence':[], 'elimination_order':[]}
		self.assertEquals(bbn.map_query(request), True);







	def test_all(self):
		return {
		"build": 					self.build(),
		"run":						self.run(),
		"update":					self.update(),
		"initialise_space":			self.initialise_space(),
		"define_universe":			self.define_universe(),
		"clear_values":				self.clear_values(),
		"use_default_values":		self.use_default_values(),
		"declare_variables":		self.declare_variables(),
		"update_values":			self.update_values(),
		"load_sizes":				self.load_sizes(),
		"define_evidence":			self.define_evidence(),
		"define_cpds":				self.define_cpds(),
		"load_cpds":				self.load_cpds(),
		"draw_default_graph":		self.draw_default_graph(),
		"draw_graph":				self.draw_graph(),
		"build_model":				self.build_model(),
		"load_cpds_to_model":		self.load_cpds_to_model(),
		"load_model":				self.load_model(),
		"train_model":				self.train_model(),
		"test_model":				self.test_model(),
		"update_model":				self.update_model(),
		"describe_node":			self.describe_node(),
		"check_model":				self.check_model(),
		"get_nodes":				self.get_nodes(),
		"get_edges":				self.get_edges(),
		"get_cardinality":			self.get_cardinality(),
		"get_local_independencies":	self.get_local_independencies(),
		"get_active_trail_nodes":	self.get_active_trail_nodes(),
		"query":					self.query(),
		"map_query":				self.map_query()
		}

