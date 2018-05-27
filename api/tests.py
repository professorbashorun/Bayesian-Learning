# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import unittest
from bbn import HorseIDBayesianNetwork


bbn = HorseIDBayesianNetwork();





class HorseIDBayesianNetworkTest(unittest.TestCase):
	"""Brief Introduction to BayesianNetworkTest"""

	GOOD 			= "TEST PASSED";
	BAD				= "TEST FAILED";



	def build(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system build function
		
			Request Format:
				request=void

		"""
		self.assertEquals(bbn.build(request), True);
		return self.GOOD;
		#DONE






	def run(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system run function
		
			Request Format:
				request=void

		"""
		bbn.build(request);
		self.assertEquals(bbn.run(request),	True);
		return self.GOOD;
		#DONE






	def update(self, request=None):#TODO:	Needs data to test			
		"""
		This function is used for testing the Horse Identification Bayesian Network system update function
		
			Request Format:
				request = { 
					dataset:	{
						'variable1': [values1], 
						... 
						'variableN': [valuesN] 
					}, 
					'graph': [
						(variable1_i, variable1_j),
						(variable2_i, variable2_j),
						...
						(variableN_i, variableN_j)
					]
				}

			Response Format:
				response=Boolean

		"""
		bbn.build(request);
		if type(request) == None :
			request = {'dataset': {
				bbn.IDENTIFIABILITY:		[[0.1], [0.9]],		
				bbn.LOCATION:				[[0.9], [0.1]],		
				bbn.CHIP_WORK:				[[0.3, 0.3], [0.7, 0.7]],
				bbn.CHIPPED:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT_AVAILABLE:		[[0.7, 0.3], [0.3, 0.7]],
				bbn.ID_USING:				[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],		
				bbn.ID_VERIFYING:			[[0.8], [0.2]],		
				bbn.ID_USING_MARKING:		[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],
				bbn.MARKINGS_CORRECT:		[[0.9], [0.1]],		
				bbn.DISTINCTIVE_TRAITS:		[[0.7], [0.3]],		
				bbn.OWNER_STA:				[[0.7], [0.3]],
				bbn.GOOD_ID:				[[0.1,0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1], 
													   [0.9,0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]]
				},
				'graph':[			
					#VARIABLES FROM 			VARIABLES TO							#ARROW FROM 							ARROW TO
					(bbn.identifiability, 		bbn.good_id),							#identifiability 		------> 		good_id
					(bbn.location, 				bbn.chipped),							#location 				------> 		chipped
					(bbn.location, 				bbn.chip_work),							#location 				------> 		chip_work
					(bbn.location, 				bbn.passport),							#location  				------> 		passport
					(bbn.chipped, 				bbn.id_using),							#chipped 				------> 		id_using	
					(bbn.chip_work, 			bbn.id_using),							#chip_work  			------> 		id_using
					(bbn.passport, 				bbn.passport_available),				#passport 				------> 		passport_available			
					(bbn.passport_available, 	bbn.id_using),							#passport_available 	------> 		id_using
					(bbn.markings_correct, 		bbn.id_using_marking),					#markings_correct 		------> 		id_using_marking
					(bbn.distinctive_traits, 	bbn.id_using_marking),					#distinctive_traits 	------> 		id_using_marking
					(bbn.passport_available, 	bbn.id_using_marking),					#passport_available  	------>		 	id_using_marking
					(bbn.id_verifying, 			bbn.good_id),							#id_verifying  			------> 		good_id
					(bbn.id_using, 				bbn.good_id),							#id_using 				------> 		good_id
					(bbn.id_using_marking, 		bbn.good_id),							#id_using_marking 		------> 		good_id
					(bbn.owner_sta, 			bbn.good_id),							#owner_sta 				------> 		good_id
				]
			};
		bbn.run(request);
		self.assertEquals(bbn.update(request), {'time': "", 'accuracy': ""});
		return self.GOOD;
		#NEED REVIEW







	def initialise_space(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system initialise function
		
			Request Format:
				request=void

		"""
		self.assertEquals(bbn.initialise_space(request), True);
		return self.GOOD;
		#DONE







	def set_universe(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system set universe function
		
			Request Format:
				request=void

		"""
		self.assertEquals(bbn.set_universe(request), True);
		return self.GOOD;
		#DONE






	def clear_values(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system clear value function
		
			Request Format:
				request=void

		"""
		self.assertEquals(bbn.clear_values(request), True);
		return self.GOOD;
		#DONE







	def use_default_values(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system use_default_values function
		
			Request Format:
				request=void

		"""
		self.assertEquals(bbn.use_default_values(request), True);
		return self.GOOD;
		#DONE






	def declare_variables(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system declare variables function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.declare_variables(request), True);
		return self.GOOD;
		#DONE




	def update_values(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system update function

			Request Format:
				request={data:{'variable1': values1, ... 'variableN': valuesN }}

		"""
		bbn.build(request);
		if type(request) == type(None):
			request={'data': {
				bbn.IDENTIFIABILITY:		[[0.1], [0.9]],		
				bbn.LOCATION:				[[0.9], [0.1]],		
				bbn.CHIP_WORK:				[[0.3, 0.3], [0.7, 0.7]],
				bbn.CHIPPED:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT_AVAILABLE:		[[0.7, 0.3], [0.3, 0.7]],
				bbn.ID_USING:				[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],		
				bbn.ID_VERIFYING:			[[0.8], [0.2]],		
				bbn.ID_USING_MARKING:		[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],
				bbn.MARKINGS_CORRECT:		[[0.9], [0.1]],		
				bbn.DISTINCTIVE_TRAITS:		[[0.7], [0.3]],		
				bbn.OWNER_STA:				[[0.7], [0.3]],
				bbn.GOOD_ID:				[[0.1,0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1], 
													   [0.9,0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]]
				}
			};
		self.assertEquals(bbn.update_values(request), True);
		return self.GOOD;
		#NEED REVIEW





	def load_sizes(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_sizes function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.load_sizes(request), True);
		return self.GOOD;
		#NEED REVIEW






	def set_evidences(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system set evidence function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.set_evidences(request), True);
		return self.GOOD;
		#NEED REVIEW







	def set_cpds(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system set_cpds function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.set_cpds(request), True);
		return self.GOOD;
		#NEED REVIEW







	def load_cpds(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_cpds function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.set_cpds(request), True);
		return self.GOOD;
		#NEED REVIEW







	def draw_default_graph(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system draw_default_graph function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.draw_default_graph(request), True);
		return self.GOOD;
		#NEED REVIEW







	def draw_graph(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system draw_graph function

			Request Format:
				request={'graph': [(A1,B1),(A2,B2), ... (AN,BN),]}

		"""
		bbn.build(request);
		if type(request) == type(None):
			request={'graph':[			
					#VARIABLES FROM 			VARIABLES TO							#ARROW FROM 							ARROW TO
					(bbn.identifiability, 		bbn.good_id),							#identifiability 		------> 		good_id
					(bbn.location, 				bbn.chipped),							#location 				------> 		chipped
					(bbn.location, 				bbn.chip_work),							#location 				------> 		chip_work
					(bbn.location, 				bbn.passport),							#location  				------> 		passport
					(bbn.chipped, 				bbn.id_using),							#chipped 				------> 		id_using	
					(bbn.chip_work, 			bbn.id_using),							#chip_work  			------> 		id_using
					(bbn.passport, 				bbn.passport_available),				#passport 				------> 		passport_available			
					(bbn.passport_available, 	bbn.id_using),							#passport_available 	------> 		id_using
					(bbn.markings_correct, 		bbn.id_using_marking),					#markings_correct 		------> 		id_using_marking
					(bbn.distinctive_traits, 	bbn.id_using_marking),					#distinctive_traits 	------> 		id_using_marking
					(bbn.passport_available, 	bbn.id_using_marking),					#passport_available  	------>		 	id_using_marking
					(bbn.id_verifying, 			bbn.good_id),							#id_verifying  			------> 		good_id
					(bbn.id_using, 				bbn.good_id),							#id_using 				------> 		good_id
					(bbn.id_using_marking, 		bbn.good_id),							#id_using_marking 		------> 		good_id
					(bbn.owner_sta, 			bbn.good_id),							#owner_sta 				------> 		good_id
				]
			};
		self.assertEquals(bbn.draw_graph(request), True);
		return self.GOOD;
		#DONE




	def build_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system build_model function

			Request Format:
				request=void

		"""
		bbn.build(request);
		self.assertEquals(bbn.build_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def load_cpds_to_model(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_cpds_to_model function

			Request Format:
				request=void

		"""
		bbn.build(request);
		bbn.run(request)
		self.assertEquals(bbn.load_cpds_to_model(request), True);
		return self.GOOD;
		#NEED REVIEW






	def load_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_model function

			Request Format:
				request=void

		"""
		bbn.build(request);
		self.assertEquals(bbn.load_model(request), True);
		return self.GOOD;
		#NEED REVIEW







	def train_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system train_model function

			Request Format:
				request={data:{'variable1': values1, ... 'variableN': valuesN }, 'graph': [(variable1_i, variable1_j),(variable2_i, variable2_j),,}

		"""
		if type(request) == type(None):
			request = {'data': {
				bbn.IDENTIFIABILITY:		[[0.1], [0.9]],		
				bbn.LOCATION:				[[0.9], [0.1]],		
				bbn.CHIP_WORK:				[[0.3, 0.3], [0.7, 0.7]],
				bbn.CHIPPED:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT_AVAILABLE:		[[0.7, 0.3], [0.3, 0.7]],
				bbn.ID_USING:				[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],		
				bbn.ID_VERIFYING:			[[0.8], [0.2]],		
				bbn.ID_USING_MARKING:		[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],
				bbn.MARKINGS_CORRECT:		[[0.9], [0.1]],		
				bbn.DISTINCTIVE_TRAITS:		[[0.7], [0.3]],		
				bbn.OWNER_STA:				[[0.7], [0.3]],
				bbn.GOOD_ID:				[[0.1,0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1], 
													   [0.9,0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]]
				},
				'graph':[			
					#VARIABLES FROM 			VARIABLES TO							#ARROW FROM 							ARROW TO
					(bbn.identifiability, 		bbn.good_id),							#identifiability 		------> 		good_id
					(bbn.location, 				bbn.chipped),							#location 				------> 		chipped
					(bbn.location, 				bbn.chip_work),							#location 				------> 		chip_work
					(bbn.location, 				bbn.passport),							#location  				------> 		passport
					(bbn.chipped, 				bbn.id_using),							#chipped 				------> 		id_using	
					(bbn.chip_work, 			bbn.id_using),							#chip_work  			------> 		id_using
					(bbn.passport, 				bbn.passport_available),				#passport 				------> 		passport_available			
					(bbn.passport_available, 	bbn.id_using),							#passport_available 	------> 		id_using
					(bbn.markings_correct, 		bbn.id_using_marking),					#markings_correct 		------> 		id_using_marking
					(bbn.distinctive_traits, 	bbn.id_using_marking),					#distinctive_traits 	------> 		id_using_marking
					(bbn.passport_available, 	bbn.id_using_marking),					#passport_available  	------>		 	id_using_marking
					(bbn.id_verifying, 			bbn.good_id),							#id_verifying  			------> 		good_id
					(bbn.id_using, 				bbn.good_id),							#id_using 				------> 		good_id
					(bbn.id_using_marking, 		bbn.good_id),							#id_using_marking 		------> 		good_id
					(bbn.owner_sta, 			bbn.good_id),							#owner_sta 				------> 		good_id
				]
			};
		self.assertEquals(bbn.train_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def test_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system test_model function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.test_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def update_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system update_model function

			Request Format:
				#request={data:{'variable1': values1, ... 'variableN': valuesN }, 'graph': [(variable1_i, variable1_j),(variable2_i, variable2_j),,}

		"""
		if type(request) == type(None):
			request = {'data': {
				bbn.IDENTIFIABILITY:		[[0.1], [0.9]],		
				bbn.LOCATION:				[[0.9], [0.1]],		
				bbn.CHIP_WORK:				[[0.3, 0.3], [0.7, 0.7]],
				bbn.CHIPPED:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT:				[[0.7, 0.3], [0.3, 0.7]],		
				bbn.PASSPORT_AVAILABLE:		[[0.7, 0.3], [0.3, 0.7]],
				bbn.ID_USING:				[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],		
				bbn.ID_VERIFYING:			[[0.8], [0.2]],		
				bbn.ID_USING_MARKING:		[[0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1], [0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]],
				bbn.MARKINGS_CORRECT:		[[0.9], [0.1]],		
				bbn.DISTINCTIVE_TRAITS:		[[0.7], [0.3]],		
				bbn.OWNER_STA:				[[0.7], [0.3]],
				bbn.GOOD_ID:				[[0.1,0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1 , 0.1], 
											[0.9,0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9, 0.9, 0.9 , 0.9, 0.9, 0.9 , 0.9]]
				},
				'graph':[			
					#VARIABLES FROM 			VARIABLES TO							#ARROW FROM 							ARROW TO
					(bbn.identifiability, 		bbn.good_id),							#identifiability 		------> 		good_id
					(bbn.location, 				bbn.chipped),							#location 				------> 		chipped
					(bbn.location, 				bbn.chip_work),							#location 				------> 		chip_work
					(bbn.location, 				bbn.passport),							#location  				------> 		passport
					(bbn.chipped, 				bbn.id_using),							#chipped 				------> 		id_using	
					(bbn.chip_work, 			bbn.id_using),							#chip_work  			------> 		id_using
					(bbn.passport, 				bbn.passport_available),				#passport 				------> 		passport_available			
					(bbn.passport_available, 	bbn.id_using),							#passport_available 	------> 		id_using
					(bbn.markings_correct, 		bbn.id_using_marking),					#markings_correct 		------> 		id_using_marking
					(bbn.distinctive_traits, 	bbn.id_using_marking),					#distinctive_traits 	------> 		id_using_marking
					(bbn.passport_available, 	bbn.id_using_marking),					#passport_available  	------>		 	id_using_marking
					(bbn.id_verifying, 			bbn.good_id),							#id_verifying  			------> 		good_id
					(bbn.id_using, 				bbn.good_id),							#id_using 				------> 		good_id
					(bbn.id_using_marking, 		bbn.good_id),							#id_using_marking 		------> 		good_id
					(bbn.owner_sta, 			bbn.good_id),							#owner_sta 				------> 		good_id
				]
			};
		self.assertEquals(bbn.update_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def describe_node(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system describe_node function

			Request Format:
				request={'node':value}

		"""
		request = {'node': bbn.identifiability};
		self.assertEquals(bbn.describe_node(request), True);
		return self.GOOD;
		#NEED REVIEW





	def check_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system check_model function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.check_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def get_nodes(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_nodes function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.get_nodes(request),  True);
		#NEED REVIEW





	def get_edges(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_edges function

			Request Format:
				request=void

		"""
		self.assertEquals(bbn.get_edges(request), True);
		return self.GOOD;
		#NEED REVIEW






	def get_cpds(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_cpds function

			Request Format:
				request={'node':value}
		"""
		request = {'node': bbn.identifiability };
		self.assertEquals(bbn.get_cpds(request), True);
		return self.GOOD;
		#NEED REVIEW





	def get_cardinality(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_cardinality function

			Request Format:
				request={'node':value}

		"""
		request = {'node': bbn.identifiability };
		self.assertEquals(bbn.get_cardinality(request), True);
		return self.GOOD;
		#NEED REVIEW





	def get_local_independencies(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_local_independencies function

			Request Format:
				request={'variables':values}

		"""
		request = {'variables': [bbn.identifiability] };
		self.assertEquals(bbn.get_local_independencies(request), True);
		return self.GOOD;
		#NEED REVIEW





	def get_active_trail_nodes(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_active_trail_nodes function

			Request Format:
				request={'variables':values, 'observed':values}

		"""
		request={'variables':[bbn.identifiability], 'observed':None}
		self.assertEquals(bbn.get_active_trail_nodes(request), True);
		return self.GOOD;
		#NEED REVIEW






	def query(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system query function

			Request Format:
				request={'variables':value, 'evidence':value, 'elimination_order':value}

		"""
		request={'variables':[bbn.identifiability], 'evidence':None, 'elimination_order':None}
		self.assertEquals(bbn.query(request), True);
		return self.GOOD;
		#NEED REVIEW





	def map_query(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system map_query function

			Request Format:
				request={'variables':value, 'evidence':value, 'elimination_order':value}

		"""
		request={'variables':[bbn.identifiability], 'evidence':None, 'elimination_order':None}
		self.assertEquals(bbn.map_query(request), True);
		return self.GOOD;
		#NEED REVIEW






	def test_all(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system test_all function

			Request Format:
				request =	{	
				data:	{	
					'variable1': 		values1,
					'variable2': 		values2,
					... 
					'variableN': 		valuesN 
				}, 
				'graph': [
					(variable1_i, 		variable1_j),
					(variable2_i, 		variable2_j),
					...
					(variableN_i, 		variableN_j)
				],
				'node'		:			'value',
				'variables'	:			[variable1, variable2, ... variableN ],
				'observed'	:			'values',
				'evidence'	:			[values],
				'elimination_order':	[values]
			}

		"""
		return {
		"build": 					self.build(request),
		"run":						self.run(request),
		"update":					self.update(request),
		"initialise_space":			self.initialise_space(request),
		"set_universe":				self.set_universe(request),
		"clear_values":				self.clear_values(request),
		"use_default_values":		self.use_default_values(request),
		"declare_variables":		self.declare_variables(request),
		"update_values":			self.update_values(request),
		"load_sizes":				self.load_sizes(request),
		"set_evidence":				self.set_evidence(request),
		"set_cpds":					self.set_cpds(request),
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
		#NEED REVIEW








	def runTest(self):
		return test_all();

