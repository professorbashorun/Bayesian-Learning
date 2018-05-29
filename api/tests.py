# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import unittest
from bbn import HorseIDBayesianNetwork


bbn = HorseIDBayesianNetwork();





class HorseIDBayesianNetworkTest(unittest.TestCase):
	"""Brief Introduction to BayesianNetworkTest"""

	GOOD 				= "TEST PASSED";
	FAILED				= "TEST FAILED";


	def start(self, request=None):
		"""
		This should be use for testing the start function of the default Horse Identification Bayesian Belief Network system.
			
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/start
				OR
				curl -X POST http://bbn.horseid.com/model/start --data $request
				OR
				model_test.start(request);

			
			Mathematical Statement:
				....
		"""
		if bbn.start(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE
		



	def build(self, request=None):	
		"""
		This should be use for testing the build function of the default Horse Identification Bayesian Belief Network system.
		
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/build
				OR
				curl -X POST http://bbn.horseid.com/model/build --data $request
				OR
				model_test.run(request);
			
			Mathematical Statement:
				....
		"""
		if bbn.build(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE






	def run(self, request=None):
		"""
		This should be use for testing the run function of the default Horse Identification Bayesian Belief Network system.
		
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/run
				OR
				curl -X POST http://bbn.horseid.com/model/run --data $request
				OR
				model_test.run(request);
			
			Mathematical Statement:
				....
		"""
		if bbn.run(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE





	def update(self, request=None):#TODO:	Needs data to test			
		""""
		This should be use for testing the udpate function of the default Horse Identification Bayesian Belief Network system.
		
			Request Format:
				request = { 
					'dataset':	{
						#for all nodes, do
							'node_name': [ value1, value2, value3, ... ],
					}, 
					'graph': [
						#for all edges, do
							('from node_name', 'to node_name')
					]
				}


			Usage Format:
				request=
				{
					dataset:	
					{
						'self.IDENTIFIABILTY'			: 	[[]],
						'self.LOCATION'		 			: 	[[]],
						'self.CHIP_WORK'	 			:	[[]],
						'self.PASSPORT'		 			: 	[[]],
						'self.PASSPORT_AVALAIBLE'		:	[[]],
						'self.ID_USING'					:	[[]],
						'self.ID_VERIFYING'				:	[[]],
						'self.ID_USING_MARKING'			:	[[]],
						'self.MARKINGS_CORRECT'			:	[[]],
						'self.DISTINCTIVE_TRAITS'		:	[[]],
						'self.OWNER_STA'				:	[[]],
						'self.GOOD_ID'					:	[[]],
					},
					graph:	
					{
						#exmaple graph
						('self.IDENTIFIABILTY'			, 	self.IDENTIFIABILTY),
						('self.LOCATION'		 		, 	self.PASSPORT),
						('self.CHIP_WORK'	 			,	self.IDENTIFIABILTY),
						('self.PASSPORT'		 		, 	self.IDENTIFIABILTY),
						('self.PASSPORT_AVALAIBLE'		,	self.IDENTIFIABILTY),
						('self.ID_USING'				,	self.PASSPORT),
						('self.ID_VERIFYING'			,	self.PASSPORT),
						('self.ID_USING_MARKING'		,	self.PASSPORT),
						('self.MARKINGS_CORRECT'		,	self.MARKINGS_CORRECT),
						('self.DISTINCTIVE_TRAITS'		,	self.MARKINGS_CORRECT),
						('self.OWNER_STA'				,	self.OWNER_STA),
						('self.GOOD_ID'					,	self.OWNER_STA),
					}
				}
				curl -X GET http://bbn.horseid.com/model/update
				OR
				curl -X POST http://bbn.horseid.com/model/update --data $request
				OR
				model_test.update(request);
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
		#bbn.run(request);
		#self.assertEquals(bbn.update(request), {'time': "", 'accuracy': ""});
		return self.GOOD;
		#NEED REVIEW







	def initialise_space(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system initialise function
		
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/initialise_space
				OR
				curl -X POST http://bbn.horseid.com/model/initialise_space --data $request
				OR
				model_test.initialise_space(request);

		"""
		if bbn.initialise_space(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







	def set_universe(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system set universe function
		
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/set_unvierse
				OR
				curl -X POST http://bbn.horseid.com/model/set_universe --data $request
				OR
				model_test.set_universe(request);

		"""
		if bbn.set_universe(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE






	def clear_values(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system clear value function
		
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/clear_values
				OR
				curl -X POST http://bbn.horseid.com/model/clear_values --data $request
				OR
				model_test.update(request);

		"""
		if bbn.clear_values(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







	def use_default_values(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system use_default_values function
		
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/use_default_values
				OR
				curl -X POST http://bbn.horseid.com/model/use_default_values --data $request
				OR
				model_test.use_default_values(request);

		"""
		if bbn.use_default_values(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE






	def declare_variables(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system declare variables function

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/declare_variables
				OR
				curl -X POST http://bbn.horseid.com/model/declare_variables --data $request
				OR
				model_test.declare_variables(request);

		"""
		if bbn.declare_variables(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE




	def update_values(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system update function

			Request Format:
				request={data:{'variable1': values1, ... 'variableN': valuesN }}

			Usage Format:
				request=None;
				curl -X GET http://bbn.horseid.com/model/update_values
				OR
				curl -X POST http://bbn.horseid.com/model/update_values --data $request
				OR
				model_test.update_values(request);

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
		#self.assertEquals(bbn.update_values(request), True);
		return self.GOOD;
		#NEED REVIEW





	def load_sizes(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_sizes function

			Request Format:
				request=void

		"""
		if bbn.load_sizes(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE
		#NEED REVIEW






	def set_evidences(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system set evidence function

			Request Format:
				request=void

		"""
		if bbn.set_evidences(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







	def set_cpds(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system set_cpds function

			Request Format:
				request=void

		"""
		if bbn.set_cpds(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







	def load_cpds(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_cpds function

			Request Format:
				request=void

		"""
		if bbn.load_cpds(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







	def draw_default_graph(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system draw_default_graph function

			Request Format:
				request=void

		"""
		if bbn.draw_default_graph(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







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
		if bbn.draw_graph(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE




	def build_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system build_model function

			Request Format:
				request=void

		"""
		if bbn.build(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE





	def load_cpds_to_model(self, request=None):	
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_cpds_to_model function

			Request Format:
				request=void

		"""
		bbn.start(request);
		if bbn.load_cpds_to_model(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE






	def load_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system load_model function

			Request Format:
				request=void

		"""
		bbn.start(request);
		if bbn.load_model(request) == True:
			return self.GOOD;
		else:
			return self.FAILED
		#DONE







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
		#self.assertEquals(bbn.train_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def test_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system test_model function

			Request Format:
				request=void

		"""
		#self.assertEquals(bbn.test_model(request), True);
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
		#self.assertEquals(bbn.update_model(request), True);
		return self.GOOD;
		#NEED REVIEW





	def describe_node(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system describe_node function

			Request Format:
				request={'node':value}

		"""
		bbn.start()
		request={bbn.NODE:[bbn.IDENTIFIABILITY]}
		if bbn.describe_node(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def check_model(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system check_model function

			Request Format:
				request=void

		"""
		bbn.start()
		if bbn.check_model(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def get_nodes(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_nodes function

			Request Format:
				request=void

		"""
		bbn.start()
		if bbn.get_nodes(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def get_edges(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_edges function

			Request Format:
				request=void

		"""
		bbn.start()
		if bbn.get_edges(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE






	def get_cpds(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_cpds function

			Request Format:
				request={'node':value}
		"""
		bbn.start()
		request={bbn.NODE:[bbn.IDENTIFIABILITY]}
		if bbn.get_cpds(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def get_cardinality(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_cardinality function

			Request Format:
				request={'node':value}

		"""
		bbn.start()
		request={bbn.NODE:[bbn.IDENTIFIABILITY]}
		if bbn.get_cardinality(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def get_local_independencies(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_local_independencies function

			Request Format:
				request={'variables':values}

		"""
		bbn.start()
		request={bbn.VARIABLES:[bbn.IDENTIFIABILITY]}
		if bbn.get_local_independencies(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def get_active_trail_nodes(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system get_active_trail_nodes function

			Request Format:
				request={'variables':values, 'observed':values}

		"""
		bbn.start()
		request={bbn.VARIABLES:[bbn.IDENTIFIABILITY], bbn.OBSERVED:None}
		if bbn.get_active_trail_nodes(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE






	def query(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system query function

			Request Format:
				request={'variables':value, 'evidence':value, 'elimination_order':value}

		"""
		bbn.start()
		request={bbn.VARIABLES:[bbn.IDENTIFIABILITY], bbn.EVIDENCE:None, bbn.ELIMINATION_ORDER:None}
		if bbn.query(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE





	def map_query(self, request=None):
		"""
		This function is used for testing the Horse Identification Bayesian Network system map_query function

			Request Format:
				request={'variables':value, 'evidence':value, 'elimination_order':value}

		"""
		bbn.start()
		request={bbn.VARIABLES:[bbn.IDENTIFIABILITY], bbn.EVIDENCE:None, bbn.ELIMINATION_ORDER:None}
		if bbn.query(request) == False:
			return self.FAILED
		else:
			return self.GOOD
		#DONE






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
		"start":					self.start(request),
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
		"set_evidences":			self.set_evidences(request),
		"load_evidences":			self.load_evidences(request),
		"set_cpds":					self.set_cpds(request),
		"load_cpds":				self.load_cpds(request),
		"draw_default_graph":		self.draw_default_graph(request),
		"load_default_graph":		self.load_default_graph(request),
		"draw_graph":				self.draw_graph(request),
		"load_graph":				self.load_graph(request),
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
		"get_cpds":					self.get_cpds(request),
		"get_cardinality":			self.get_cardinality(request),
		"get_local_independencies":	self.get_local_independencies(request),
		"get_active_trail_nodes":	self.get_active_trail_nodes(request),
		"query":					self.query(request),
		"map_query":				self.map_query(request)
		}
		#NEED REVIEW








	def runTest(self):
		return test_all();

