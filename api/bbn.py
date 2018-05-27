#using pgmpy for probabilistic graphical modelling of Bayesian Network of HorseID
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import pandas as pd;




class HorseIDBayesianNetwork(object):


	current_dataframe = None;#Dataframe
	last_updated_time = None;#Datetime
	"""
	The general workflow is:

		STEP 1		BUILD THE SYSTEM
			I.		initialise space
			II.		set universe
			III.	use default values / set new values
			IV.		set evidences or causal nodes properties
			V.		set Conditional Probability Distribution Table
			VI.		draw default Horse Identification BBN Graph / draw new Horse Identification BBN Graph.
		STEP 2		RUN THE SYSTEM
			I.		load model
		STEP 3		PERFORM INFERENCE, ANALYSIS, AND MODIFICATION TASKS
			I.		update model
			II.		or call any other function.



		General Request Object Format:
			request =	{	
				data:	{	
					'variable1': 		values1,
					'variable2': 		values2,
					... 
					'variableN': 		valuesN 
				}, 
				dataset:{	
					'variable1': 		[values1],
					'variable2': 		[values2],
					... 
					'variableN': 		[valuesN] 
				},
				'graph': [
					(variable1_i, 		variable1_j),
					(variable2_i, 		variable2_j),
					...
					(variableN_i, 		variableN_j)
				],
				'node'		:			'value',
				'variables'	:			{variable1: values, variable2: values, ... variableN: values},
				'variable_card':		{variable1: values, variable2: values, ... variableN: values},
				'values':				[values],
				'observed'	:			'values',
				'evidence'	:			[values],
				'evidence_card':		[values],
				'elimination_order':	[values]
			}



		General Response Object Format:
			response = {
				time:		latest_updated_time,
				accuracy:	current_accuracy
			}

	"""



	def build(self, request=None):
		"""
		This should be use for building the default Horse Identification Bayesian Belief Network graph from initialisation of the variables to drawing the graph.
			
			Request Format:
				request=void

			Mathematical Statement:
				....
		"""
		self.initialise_space(request);	
		self.set_universe(request);
		self.use_default_values(request);
		self.declare_variables(request);
		self.set_evidences(request);
		self.set_cpds(request);
		self.draw_default_graph(request);
		return True;
		#DONE





	def run(self, request=None):
		"""
		This function should be used for loading and running a Bayesian Belief Network on an already built Horse Identification Bayesian Belief Network
			
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
		self.load_model(request);
		return True;
		#DONE





	def update(self, request):
		"""
		This function should be used for loading and running a Bayesian Belief Network on an already built Horse Identification Bayesian Belief Network
			
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

			Mathematical Statement:
				...
		"""
		return self.update_model(request);
		#NEED REVIEW






	def initialise_space(self, request=None):
		"""
		This function should be use for initialising the variable spaces for identifiablity, location, chip_work, passport_space, and so on.
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		
		# VARIABLE SPACE 						POSSIBLE VALUES
		self.identifiablity_space 				= [0, 1];								# If the outcome of the previous id is GOOD, then 1; else if it is not GOOD then 0;
		self.location_space 					= ["ireland", "not_ireland"];			# Currently using 5 locations in the EU as default.
		self.chip_work_space					= [True, False];						# If 
		self.passport_space						= [True, False];
		self.passport_available_space 			= [True, False];	
		self.id_using_space						= [True, False];
		self.id_verifying_space					= [True, False];
		self.id_using_marking_space				= [True, False];
		self.markings_correct_space				= [True, False];
		self.distinctive_traits_space			= [True, False];
		self.owner_sta_space					= [True, False];
		self.good_id_space						= [True, False];
		return True;
		#DONE









	def set_universe(self, request=None):
		"""
		This function should be used to set all possible values of the global variables such as IDENTIFIABILITY keyword, identifiability symbol, and the size of this variable.

			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		self.clear_values(request);	
		self.declare_variables(request);
		return True;
		#DONE









	def clear_values(self, request=None):
		"""
		This function should be used to clear the values of the probability distribution matrix and set it to None or [[]];

			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""

		#DEFINE VARIBLES 						SET EMPTY MATRIX 
		self.identifiability_values 			= [[]];		
		self.location_values					= [[]];	
		self.chip_work_values 					= [[]];
		self.chipped_values 					= [[]];
		self.passport_values					= [[]];
		self.passport_available_values  		= [[]];
		self.id_using_values 					= [[]];
		self.id_verifying_values				= [[]];
		self.id_using_marking_values			= [[]];
		self.markings_correct_values 			= [[]];	
		self.distinctive_traits_values 			= [[]];			
		self.owner_sta_values 					= [[]];		
		self.good_id_values						= [[]];
		return True;
		#DONE








	def use_default_values(self, request=None):	
		"""
		This function should be used to set probability distribution maxtrix to default values\

			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""

		#VARIABLES 								DEFAULT PROBABILITY TENSORS
		self.identifiability_values 			= [[0.1], [0.9]];				
		self.location_values					= [[0.5], [0.5]];	
		self.chip_work_values 					= [[0.2, 0.2], [0.8, 0.8]];
		self.chipped_values 					= [[0.2, 0.2], [0.8, 0.8]];
		self.passport_values					= [[0.2, 0.2], [0.8, 0.8]];
		self.passport_available_values  		= [[0.2, 0.2], [0.8, 0.8]];
		self.id_using_values 					= [[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
		self.id_using_marking_values			= [[0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
		self.id_verifying_values				= [[0.7], [0.3]];				
		self.markings_correct_values 			= [[0.9], [0.1]];				
		self.distinctive_traits_values 			= [[0.8], [0.2]];				
		self.owner_sta_values 					= [[0.8], [0.2]];				
		self.good_id_values						= [[0.2,0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], 
												   [0.8,0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
		return True;
		#DONE









	def declare_variables(self, request=None):
		"""
		This function should be used to declare the variable size

			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		#define variables and variables size
		try:
			#VARIABLE DEFINATION    	SYMBOLICS					VARIABLE SIZE 					VARIABLE DEFINITION 	SYMBOLICS 		SET VARIABLE SIZE
			self.IDENTIFIABILITY,		self.identifiability, 		self.identifiability_size 		= "identifiability",		"V0", 		len(self.identifiability_values); 		# variable symbols are defined so that it is consistent with the mathematical presentation.
			self.LOCATION,				self.location, 				self.location_size 				= "location",				"V1", 		len(self.location_values); 				# TODO: all values to be corrected.
			self.CHIP_WORK,				self.chip_work, 			self.chip_work_size 			= "chip_work", 				"V2",		len(self.chip_work_values);				#
			self.CHIPPED,				self.chipped, 				self.chipped_size 				= "chipped",				"V3",		len(self.chipped_values);
			self.PASSPORT,				self.passport, 				self.passport_size 				= "passport",				"V4",		len(self.passport_values);
			self.PASSPORT_AVAILABLE,	self.passport_available, 	self.passport_available_size 	= "passport_available",		"V5",		len(self.passport_available_values);
			self.ID_USING,				self.id_using, 				self.id_using_size 				= "id_using",				"V6",		len(self.id_using_values);
			self.ID_VERIFYING,			self.id_verifying, 			self.id_verifying_size 			= "id_verifying",			"V7",		len(self.id_verifying_values);
			self.ID_USING_MARKING,		self.id_using_marking, 		self.id_using_marking_size 		= "id_using_marking",		"V8",		len(self.id_using_marking_values);
			self.MARKINGS_CORRECT,		self.markings_correct, 		self.markings_correct_size 		= "markings_correct",		"V9",		len(self.markings_correct_values);
			self.DISTINCTIVE_TRAITS,	self.distinctive_traits, 	self.distinctive_traits_size 	= "distinctive_traits",		"V10",		len(self.distinctive_traits_values);
			self.OWNER_STA,				self.owner_sta, 			self.owner_sta_size 			= "owner_sta",				"V11",		len(self.owner_sta_values);
			self.GOOD_ID,				self.good_id, 				self.good_id_size 				= "good_id",				"V12",		len(self.good_id_values);
		except Exception as e:
			return e
		return True;
		#DONE








	
	def update_values(self, request):
		"""
		This function should be used to update the probability distribution matrix for all the variables/nodes.

			Request Format:
				request 	=	{
					data:	{
						'variable1': values1, 
						'variable2': values2,
						... 
						'variableN': valuesN 
					}
				}

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		try:
			self.clear_values(request);	
			#DEFINE VARIABLES 						SET VALUES 
			self.identifiability_values 			= self.identifiability_values.append(request.data[self.IDENTIFIABILITY]);
			self.location_values 					= self.location_values.append(request.data[self.LOCATION]);
			self.chip_work_values 					= self.chip_work_values.append(request.data[self.CHIP_WORK]);
			self.chipped_values 					= self.chipped_values.append(request.data[self.CHIPPED]);
			self.passport_values 					= self.passport_values.append(request.data[self.PASSPORT]);
			self.passport_available_values 			= self.passport_available_values.append(request.data[self.PASSPORT_AVAILABLE]);
			self.id_using_values 					= self.id_using_values.append(request.data[self.ID_USING]);
			self.id_verifying_values 				= self.id_verifying_values.append(request.data[self.ID_VERIFYING]);
			self.id_using_marking_values 			= self.id_using_marking_values.append(request.data[self.ID_USING_MARKING]);
			self.markings_correct_values 			= self.markings_correct_values.append(request.data[self.MARKINGS_CORRECT]);
			self.distinctive_traits_values 			= self.distinctive_traits_values.append(request.data[self.DISTINCTIVE_TRAITS]);
			self.owner_sta_values 					= self.owner_sta_values.append(request.data[self.OWNER_STA]);
			self.good_id_values 					= self.good_id_values.append(request.data[self.GOOD_ID]);
			load_sizes(request);	
		except Exception as e:
			return e
		return True;						
		#DONE









	
	def load_sizes(self, request=None):
		"""
		This function should be used to load the sizes of the variables

			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				for all variables or nodes, load length or sizes of probability distribution matrix to the system.
		"""
		#this declares and initialises the variables sizes to be used
		try:
			self.identifiability_size 			= len(self.identifiability_values);
			self.location_size					= len(self.location_values);
			self.chip_work_size					= len(self.chip_work_values);
			self.chipped_size					= len(self.chipped_values);
			self.passport_size 					= len(self.passport_values);
			self.passport_available_size		= len(self.passport_available_values);
			self.id_using_size 					= len(self.id_using_values);
			self.id_verifying_size				= len(self.id_verifying_values);
			self.id_using_marking_size			= len(self.id_using_marking_values);
			self.markings_correct_size 			= len(self.markings_correct_values);
			self.distinctive_traits_size		= len(self.distinctive_traits_values);
			self.owner_sta_size					= len(self.owner_sta_values);
			self.good_id_size					= len(self.good_id_values);
		except Exception as e:
			return e
		return True;
		#DONE










	
	def set_evidences(self, request=None):
		"""
		This function should be used to define or load the parents/envidences for all variables or nodes.
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		#define variable dependencies and dependency size(evidence and evidence card)
		try:
			if type(request) == type(None):
				#EVIDENCE 								EVIDENCE CARD 							ENVIDENCE VALUES 												ENVIDENCE CARD VALUES
				self.identifiability_evidence, 		self.identifiability_evidence_card 			= None, 														None;
				self.location_evidence,				self.location_evidence_card 				= None, 														None;
				self.chip_work_evidence,			self.chip_work_evidence_card				= [self.location],												[self.location_size];
				self.chipped_evidence, 				self.chipped_evidence_card					= [self.location],												[self.location_size];
				self.passport_evidence,				self.passport_evidence_card					= [self.location],												[self.location_size];
				self.passport_available_evidence,	self.passport_available_evidence_card		= [self.passport],												[self.passport_size];
				self.id_using_evidence,				self.id_using_evidence_card					= [self.chip_work, self.chipped, self.passport_available],		[self.chip_work_size, self.chipped_size, self.passport_available_size];
				self.id_verifying_evidence,			self.id_verifying_evidence_card				= None,															None;
				self.id_using_marking_evidence,		self.id_using_marking_evidence_card			= [self.markings_correct, self.distinctive_traits, self.passport_available],			[self.markings_correct_size, self.distinctive_traits_size, self.passport_available_size];
				self.markings_correct_evidence,		self.markings_correct_evidence_card			= None,															None;
				self.distinctive_traits_evidence,	self.distinctive_traits_evidence_card		= None,															None;
				self.owner_sta_evidence,			self.owner_sta_evidence_card				= None,															None;
				self.good_id_evidence,				self.good_id_evidence_card					= [self.id_verifying, 				self.id_using, 			self.id_using_marking, 			self.owner_sta, self.identifiability],	[self.id_verifying_size, 			self.id_using_size, 	self.id_using_marking_size, 	self.owner_sta_size, self.identifiability_size];
			else:
				self.identifiability_evidence, 		self.identifiability_evidence_card 			= request.evidence[self.IDENTIFIABILITY], 						request.evidence_card[self.IDENTIFIABILITY];
				self.location_evidence,				self.location_evidence_card 				= request.evidence[self.LOCATION], 								request.evidence_card[self.LOCATION];
				self.chip_work_evidence,			self.chip_work_evidence_card				= request.evidence[self.CHIP_WORK],								request.evidence_card[self.CHIP_WORK];
				self.chipped_evidence, 				self.chipped_evidence_card					= request.evidence[self.CHIPPED],								request.evidence_card[self.CHIPPED];
				self.passport_evidence,				self.passport_evidence_card					= request.evidence[self.PASSPORT],								request.evidence_card[self.PASSPORT];
				self.passport_available_evidence,	self.passport_available_evidence_card		= request.evidence[self.PASSPORT_AVAILABLE],					request.evidence_card[self.PASSPORT_AVAILABLE];
				self.id_using_evidence,				self.id_using_evidence_card					= request.evidence[self.ID_USING],								request.evidence_card[self.ID_USING];
				self.id_verifying_evidence,			self.id_verifying_evidence_card				= request.evidence[self.ID_VERIFYING],							request.evidence_card[self.ID_VERIFYING];
				self.id_using_marking_evidence,		self.id_using_marking_evidence_card			= request.evidence[self.ID_USING_MARKING],						request.evidence_card[self.ID_USING_MARKING];
				self.markings_correct_evidence,		self.markings_correct_evidence_card			= request.evidence[self.MARKINGS_CORRECT],						request.evidence_card[self.MARKINGS_CORRECT];
				self.distinctive_traits_evidence,	self.distinctive_traits_evidence_card		= request.evidence[self.DISTINCTIVE_TRAITS],					request.evidence_card[self.DISTINCTIVE_TRAITS];
				self.owner_sta_evidence,			self.owner_sta_evidence_card				= request.evidence[self.OWNER_STA],								request.evidence_card[self.OWNER_STA];
				self.good_id_evidence,				self.good_id_evidence_card					= request.evidence[self.GOOD_ID],								request.evidence_card[self.GOOD_ID];
		except Exception as e:
			return e
		return True;
		#DONE








	
	def set_cpds(self, request=None):
		"""
		This is should be used to load up a conditional probability distritubation table from previous the 
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""

		#define node cpds: load this on start
		try:
			if type(request)==type(None) or type(request.data)==type(None):
				#	CPDs  						CPD TYPE 				VARIABLE 					VARIABLE SIZE 							VALUES 										EVIDENCE(DEPENDENCIES) 							EVIDENCE CARD (DEPENDENCY SIZE)
				self.identifiability_cpd 	= TabularCPD(variable=self.identifiability, 	variable_card=self.identifiability_size, 	values=self.identifiability_values);		#		None												None
				self.location_cpd 			= TabularCPD(variable=self.location, 			variable_card=self.location_size, 			values=self.location_values);				#		None												None
				self.chipped_cpd 			= TabularCPD(variable=self.chipped, 			variable_card=self.chipped_size, 			values=self.chipped_values, 				evidence=self.chipped_evidence, 				evidence_card=self.chipped_evidence_card);
				self.chip_work_cpd 			= TabularCPD(variable=self.chip_work, 			variable_card=self.chip_work_size, 			values=self.chip_work_values, 				evidence=self.chip_work_evidence, 				evidence_card=self.chip_work_evidence_card);
				self.passport_cpd 			= TabularCPD(variable=self.passport, 			variable_card=self.passport_size, 			values=self.passport_values, 				evidence=self.passport_evidence, 				evidence_card=self.passport_evidence_card);
				self.passport_available_cpd = TabularCPD(variable=self.passport_available,	variable_card=self.passport_available_size,	values=self.passport_available_values, 		evidence=self.passport_available_evidence, 		evidence_card=self.passport_available_evidence_card);
				self.id_using_cpd 			= TabularCPD(variable=self.id_using, 			variable_card=self.id_using_size, 			values=self.id_using_values, 				evidence=self.id_using_evidence, 				evidence_card=self.id_using_evidence_card);
				self.id_verifying_cpd 		= TabularCPD(variable=self.id_verifying, 		variable_card=self.id_verifying_size, 		values=self.id_verifying_values);			#		None												None
				self.markings_correct_cpd 	= TabularCPD(variable=self.markings_correct, 	variable_card=self.markings_correct_size, 	values=self.markings_correct_values);		#		None												None
				self.distinctive_traits_cpd = TabularCPD(variable=self.distinctive_traits, 	variable_card=self.distinctive_traits_size,	values=self.distinctive_traits_values);		#		None												None
				self.id_using_marking_cpd 	= TabularCPD(variable=self.id_using_marking, 	variable_card=self.id_using_marking_size,	values=self.id_using_marking_values, 		evidence=self.id_using_marking_evidence,		evidence_card=self.id_using_marking_evidence_card);
				self.owner_sta_cpd 			= TabularCPD(variable=self.owner_sta, 			variable_card=self.owner_sta_size, 			values=self.owner_sta_values);				#		None												None
				self.good_id_cpd 			= TabularCPD(variable=self.good_id, 			variable_card=self.good_id_size, 			values=self.good_id_values, 				evidence=self.good_id_evidence, 				evidence_card=self.good_id_evidence_card);
			else: 						
				self.identifiability_cpd 	= TabularCPD(variable=request.variables[self.IDENTIFIABILITY], 		variable_card=request.variable_card[self.IDENTIFIABILITY], 		values=request.values[self.IDENTIFIABILITY]);		#		None												None
				self.location_cpd 			= TabularCPD(variable=request.variables[self.LOCATION], 			variable_card=request.variable_card[self.LOCATION], 			values=request.values[self.LOCATION]);				#		None												None
				self.chipped_cpd 			= TabularCPD(variable=request.variables[self.CHIPPED], 				variable_card=request.variable_card[self.CHIPPED], 				values=request.values[self.CHIPPED], 				evidence=request.evidence[self.CHIPPED], 			evidence_card=request.evidence_card[self.CHIPPED]);
				self.chip_work_cpd 			= TabularCPD(variable=request.variables[self.CHIP_WORK], 			variable_card=request.variable_card[self.CHIP_WORK], 			values=request.values[self.CHIP_WORK], 				evidence=request.evidence[self.CHIP_WORK], 			evidence_card=request.evidence_card[self.CHIP_WORK]);
				self.passport_cpd 			= TabularCPD(variable=request.variables[self.PASSPORT], 			variable_card=request.variable_card[self.PASSPORT], 			values=request.values[self.PASSPORT], 				evidence=request.evidence[self.PASSPORT], 			evidence_card=request.evidence_card[self.PASSPORT]);
				self.passport_available_cpd = TabularCPD(variable=request.variables[self.PASSPORT_AVAILABLE],	variable_card=request.variable_card[self.PASSPORT_AVAILABLE],	values=request.values[self.PASSPORT_AVAILABLE], 	evidence=request.evidence[self.PASSPORT_AVAILABLE], evidence_card=request.evidence_card[self.PASSPORT_AVAILABLE]);
				self.id_using_cpd 			= TabularCPD(variable=request.variables[self.ID_USING], 			variable_card=request.variable_card[self.ID_USING], 			values=request.values[self.ID_USING], 				evidence=request.evidence[self.ID_USING], 			evidence_card=request.evidence_card[self.ID_USING]);
				self.id_verifying_cpd 		= TabularCPD(variable=request.variables[self.ID_VERIFYING], 		variable_card=request.variable_card[self.ID_VERIFYING], 		values=request.values[self.ID_VERIFYING]);			#		None												None
				self.markings_correct_cpd 	= TabularCPD(variable=request.variables[self.MARKINGS_CORRECT], 	variable_card=request.variable_card[self.MARKINGS_CORRECT], 	values=request.values[self.MARKINGS_CORRECT]);		#		None												None
				self.distinctive_traits_cpd = TabularCPD(variable=request.variables[self.DISTINCTIVE_TRAITS], 	variable_card=request.variable_card[self.DISTINCTIVE_TRAITS],	values=request.values[self.DISTINCTIVE_TRAITS]);	#		None												None
				self.id_using_marking_cpd 	= TabularCPD(variable=request.variables[self.ID_USING_MARKING], 	variable_card=request.variable_card[self.ID_USING_MARKING],		values=request.values[self.ID_USING_MARKING], 		evidence=request.evidence[self.ID_USING_MARKING],	evidence_card=request.evidence_card[self.ID_USING_MARKING]);
				self.owner_sta_cpd 			= TabularCPD(variable=request.variables[self.OWNER_STA], 			variable_card=request.variable_card[self.OWNER_STA], 			values=request.values[self.OWNER_STA]);				#		None												None
				self.good_id_cpd 			= TabularCPD(variable=request.variables[self.GOOD_ID], 				variable_card=request.variable_card[self.GOOD_ID], 				values=request.values[self.GOOD_ID], 				evidence=request.evidence[self.GOOD_ID], 			evidence_card=request.evidence_card[self.GOOD_ID]);
		except Exception as e:
			return e		
		return True;
		#DONE







	def load_cpds(self, request=None):	
		"""
		This is synonymous to self.set_cpds 
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		return self.set_cpds(request);
		#DONE







	def load_default_graph(self, request=None):	
		"""	
		This is synonymous to draw_default_graph
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		return self.draw_default_graph(request);
		#DONE








	def draw_default_graph(self, request=None):	
		"""
		This should be used to load the default Horse Identification Bayesian Belief Network graph.
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""	
		self.horse_id_graph = [			
			#VARIABLES FROM 			VARIABLES TO							#ARROW FROM 							ARROW TO
			(self.identifiability, 		self.good_id),							#identifiability 		------> 		good_id
			(self.location, 			self.chipped),							#location 				------> 		chipped
			(self.location, 			self.chip_work),						#location 				------> 		chip_work
			(self.location, 			self.passport),							#location  				------> 		passport
			(self.chipped, 				self.id_using),							#chipped 				------> 		id_using	
			(self.chip_work, 			self.id_using),							#chip_work  			------> 		id_using
			(self.passport, 			self.passport_available),				#passport 				------> 		passport_available			
			(self.passport_available, 	self.id_using),							#passport_available 	------> 		id_using
			(self.markings_correct, 	self.id_using_marking),					#markings_correct 		------> 		id_using_marking
			(self.distinctive_traits, 	self.id_using_marking),					#distinctive_traits 	------> 		id_using_marking
			(self.passport_available, 	self.id_using_marking),					#passport_available  	------>		 	id_using_marking
			(self.id_verifying, 		self.good_id),							#id_verifying  			------> 		good_id
			(self.id_using, 			self.good_id),							#id_using 				------> 		good_id
			(self.id_using_marking, 	self.good_id),							#id_using_marking 		------> 		good_id
			(self.owner_sta, 			self.good_id),							#owner_sta 				------> 		good_id
		];
		return True;
		#DONE








	def load_graph(self, request):
		"""
		This is synonymous to draw_graph
			
			Request Format:
				request =	{
					'graph': 	[
						(variable1_i, variable1_j),
						(variable2_i, variable2_j),
						...
						(variableN_i, variableN_j)
					]
				}
			
			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		return self.draw_graph(request);
		#DONE






	def draw_graph(self, request):
		"""
		This should be used to draw the causality/dependency graph of the House Identification Bayesian Belief Network model.
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		self.horse_id_graph	= request.graph;
		return True;
		#DONE








	
	def build_model(self, request=None):
		"""
		This should be used to build the Horse Identification Bayesian Belief Network model after the desired graph or network has been initialised and loaded.
			
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""

		#Build graph and load model: load on start
		#methods							METHOD CLASS 					FIRST ARG
		self.horse_id_model 				= BayesianModel(				self.horse_id_graph);
		self.load_cpds_to_model(request);
		self.horse_inference 				= VariableElimination(			self.horse_id_model); 
		return True;
		#DONE









	
	def load_cpds_to_model(self, request=None):	
		"""
		This should be used to load the Conditional Probability Distribution Tables on the Horse Identification Bayesain Belief Network model.

			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		#add nodes/CPDs to HorseID model graph: load this on start
		#add cpds to horse model
		self.horse_id_model.add_cpds(
			#SET 1							#SET 2							#SET 3
			self.identifiability_cpd, 		self.location_cpd, 				self.chip_work_cpd, 				
			self.chipped_cpd, 				self.passport_cpd, 				self.passport_available_cpd, 
			self.id_using_cpd, 				self.id_verifying_cpd, 			self.id_using_marking_cpd, 		
			self.markings_correct_cpd,		self.distinctive_traits_cpd, 	self.owner_sta_cpd, 
			self.good_id_cpd);
		return True;
		#DONE







	def load_model(self, request=None):	
		"""
		This should be used to load the the Horse Identification Bayesian Belief Network model after the graph to use have been defined.
		
			Request Format:
				request=void

			Response Format:
				response=Boolean

			Mathematical Statement:
				...
		"""
		#update model
		self.build_model(request);
		return True;
		#DONE








	def train_model(self, request):
		"""
		This should be used to train the Horse Identificiation Bayesian Belief Network.
		
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
				response = {
					time:		latest_updated_time,
					accuracy:	current_accuracy
				}


			Mathematical Statement:
				...
		"""
		"""
    	try:
    		self.current_dataframe = pd.DataFrame(request.data);
    		if type(request.graph) != type(None):
    			self.horse_id_model = BayesianModel(request.graph);
			self.horse_id_model.fit(self.current_dataframe);
			self.last_updated_time = ""; 
			self.current_accuracy 	=	self.test_model(request);
			return {time: self.last_updated_time, accuracy: self.current_accuracy}
    	except Exception as e:
    		return e
    	"""
		#NEED REVIEW





	def update_model(self, request):
		"""
		This function should be used to update the Horse ID Bayesian Belief Network model.
		
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
				response = {
					time:		latest_updated_time,
					accuracy:	current_accuracy
				}


			Mathematical Statement:
				...
		"""
		#use this to train model online.
		try:
			self.current_dataframe = pd.DataFrame(request.dataset);#TODO: concatenate instead of assignment
			if type(request.graph) != type(None):
				self.horse_id_model = BayesianModel(request.graph);
			self.horse_id_model.fit(self.current_dataframe);
			self.last_updated_time = "";
			self.current_accuracy 	=	self.test_model(request);
			ret = {'time': self.last_updated_time, 'accuracy': self.current_accuracy};
			return ret
		except Exception as e:
			return e
		#NEED REVIEW







	
	def test_model(self, request=None):
		"""
		This function should be used to test model accuracy.
		
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
		#TODO: test model based on dataframe and return test accuracy.
		# self.horse_id_model.query() 	
		return 0;
		#NEED REVIEW	








	def describe_node(self, request):
		"""
		This function should be used to descibe a node of interest. Synonymous to get_cpds
		
			Request Format:
				request={ 'node':	value }

			Mathematical Statement:
				...
		"""
		return self.get_cpds(node=request.node);
		#DONE








	def check_model(self, request=None):
		"""
		This function should be used to check the Horse ID Bayesian Belief Network model state.
		
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
				#model engine
		return self.horse_id_model.check_model();
		#DONE





	def get_nodes(self, request):						#TODO: come back and check
		"""
		This function should be used to get nodes that exist in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
				#model engine
		return self.horse_id_model.get_nodes();
		#NEED REVIEW






	def get_edges(self, request):						#come back and check
		"""
		This function should be used to get all the edges that exist in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
		return self.horse_id_model.get_edges();
		#NEED REVIEW







	def get_cpds(self, request):
		"""
		This function should be used to get all of( or a defined node ) the conditional probability distribution tables that exist in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request={'node':	value}

			Mathematical Statement:
				...
		"""
				#model engine				#request.node
		return self.horse_id_model.get_cpds(node=request.node);
		#DONE
	







	def get_cardinality(self, request):	
		"""
		This function should be used to get all of( or a defined node ) cardinality table in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request={'node':	value}

			Mathematical Statement:
				...
		"""
				#model engine						#request.node
		return self.horse_id_model.get_cardinality(node=request.node);
		#DONE
	







	def get_local_independencies(self, request):
		"""
		This function should be used to get all of( or a defined node ) cardinality table in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request={'variables':	[values]}

			Mathematical Statement:
				...
		"""
				#model engine							#request.variables
		return self.horse_id_model.local_independencies(variables=request.variables);
		#DONE








	def get_active_trail_nodes(self, request):
		"""
		This function should be used to get all of( or a defined node ) cardinality table in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request 	=	{
					'variables':		[values], 
					'observed':			values
				}

			Mathematical Statement:
				...
		"""
				#model engine						#request.variables, 			request.observed;
		return self.horse_id_model.active_trail_nodes(variables=request.variables, 	observed=request.observed)
		#DONE












	def query(self, request):
		"""
		This function should be used to query the Horse ID Bayesian Belief Network model and make inference via Variable Elimination Method.
		
			Request Format:
				request 	=	{
					'variables':			[ variable_symbols,... ], 
					'evidence':				[ (variable_symbol, variable_value),... ], 
					'elimination_order':	value
				}

			Response Format:

			Mathematical Statement:
				...
		"""
				#inference engine				#request.variables 			request.evidence 			request.elimination_order
		return self.horse_inference.query(variables=request.variables, 		evidence=request.evidence, 	elimination_order=request.elimination_order);
		#DONE










	def map_query(self, request):
		"""
		This function should be used to query the Horse ID Bayesian Belief Network model map and make inference via Variable Elimination Method.
		
			Request Format:
				request 	=	{
					'variables':			[ variable_symbols,... ], 
					'evidence':				[ (variable_symbol, variable_value),... ], 
					'elimination_order':	value
				}

			Response Format:

			Mathematical Statement:
				...
		"""
				#inference engine				#request.variables 			request.evidence 			request.elimination_order
		return self.horse_inference.map_query(variables=request.variables, 	evidence=request.evidence, 	elimination_order=request.elimination_order);
		#DONE











