#using pgmpy for probabilistic graphical modelling of Bayesian Network of HorseID
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import pandas as pd;




class HorseIDBayesianNetwork(object):
	"""
	The general workflow is:

		STEP 1		BUILD THE __SYSTEM
			I.		initialise space
			II.		set universe
			III.	use default values / set new values
			IV.		set evidences or causal nodes properties
			V.		set Conditional Probability Distribution Table
			VI.		draw default Horse Identification BBN Graph / draw new Horse Identification BBN Graph.
		STEP 2		RUN THE __SYSTEM
			I.		load model
		STEP 3		PERFORM INFERENCE, ANALYSIS, AND MODIFICATION TASKS
			I.		update model
			II.		or call any other function.



		General Request Object Format:
	request =	
	{	
		'data':	
		{
			#for all nodes, do
				'node_name': [ value1, value2, value3, ... ],
		}, 
		'dataset':	
		{
			#for all nodes, do
				'node_name': [ value1, value2, value3, ... ],
		}, 
		'graph': 
		[
			#for all edges, do
				('from node_name', 'to node_name')
		],
		'node'		:			'value',
		'variables'	:			{variable1: values, variable2: values, ... variableN: values},
		'values': 
		{
			#for all nodes, do
				node_name :	'node's Probablity Distribution Matrix value',
		}
		'observed'	:			'values',
		'evidence: 
		{
			#for all nodes, do
				node.node_name :	'evidence_value',
		},
		evidence_card: 
		{
			#for all nodes, do
				node.node_name :	'evidence_card_value',
		}
		'elimination_order':	[values]
	}



		General Response Object Format:
			response=Boolean
			response= 
			{
				time:		latest_updated_time,
				accuracy:	current_accuracy
			}

	"""

	#constants
	SPACES='spaces'
	NODE='node'
	DATA='data'
	DATASET='dataset'
	GRAPH='graph'
	SIZES='sizes'
	CPDS="cpds"
	VARIABLES='variables'
	EVIDENCES='evidences'
	EVIDENCE_CARDS='evidence_cards'
	ELIMINATION_ORDER='elimination_order'
	OBSERVED="observed"



	#variable states
	__SYSTEM={}					#System
	last_updated_time = None;	#Datetime
	





	def start(self, request=None):
		"""
		This should be use for starting the default Horse Identification Bayesian Belief Network __SYSTEM. Builds and Run the default model.
			
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/start --data $request
				OR
				model.start(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				....
		"""
		s1=self.build(request);
		s2=self.run(request);
		return s1 and s2;





	def build(self, request=None):
		"""
		This should be use for building the default Horse Identification Bayesian Belief Network graph globally. Starting from initialisation of the variables to drawing the graph.
			
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/build --data $request
				OR
				model.build(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				....
		"""
		s1=self.declare_variables(request);	
		s2=self.initialise_space(request);
		s3=self.set_universe(request);
		s4=self.use_default_values(request);
		s5=self.set_evidences(request);
		s6=self.set_cpds(request);
		s7=self.draw_default_graph(request);
		return s1 and s2 and s3 and s4 and s7;
		#DONE







	def run(self, request=None):
		"""
		This function should be used for loading and running a Bayesian Belief Network on an already built Horse Identification Bayesian Belief Network
			
			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/run --data $request
				OR
				model.run(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		return self.load_model(request);
		#DONE







	def update(self, request):
		"""
		This function should be used for loading and running a Bayesian Belief Network on an already built Horse Identification Bayesian Belief Network
			
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

				curl -X PUT http://bbn.horseid.com/model/update --data $request
				OR
				model.update(request);


			Response Format:
				response=False OR
				response=
				{
					time:		latest_updated_time,
					accuracy:	current_accuracy
				}

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

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/initialise_space --data $request
				OR
				model.initialise_space(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			self.__SYSTEM[self.SPACES] = {};
			spaces = self.__SYSTEM[self.SPACES];
			#------------------------------------------------------------------------------------------------------------
			# VARIABLE SPACE 							ALL POSSIBLE VALUES
			#------------------------------------------------------------------------------------------------------------
			spaces[self.IDENTIFIABILITY] 				= [0, 1];								# If identifiability is good or not.
			spaces[self.LOCATION]						= ["ireland", "not_ireland"];			# Currently using 2 locations subsets. Ireland and Not-Ireland.
			spaces[self.CHIP_WORK]						= [True, False];
			spaces[self.PASSPORT]						= [True, False];
			spaces[self.PASSPORT_AVAILABLE]				= [True, False];	
			spaces[self.ID_USING]						= [True, False];
			spaces[self.ID_VERIFYING]					= [True, False];
			spaces[self.ID_USING_MARKING]				= [True, False];
			spaces[self.MARKINGS_CORRECT]				= [True, False];
			spaces[self.DISTINCTIVE_TRAITS]				= [True, False];
			spaces[self.OWNER_STA]						= [True, False];
			spaces[self.GOOD_ID]						= [True, False];
			return True
		except Exception as e:
			return False
		#DONE









	def set_universe(self, request=None):
		"""
		This function should be used to set all possible values of the global variables such as IDENTIFIABILITY keyword, identifiability symbol, and the size of this variable.

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/set_universe --data $request
				OR
				model.set_universe(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		s1=self.clear_values(request);	
		s2=self.declare_variables(request);
		return s1 and s2;
		#NEED REVIEW









	def clear_values(self, request=None):
		"""
		This function should be used to clear the values of the probability distribution matrix and set it to None or [[]];

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/clear_values --data $request
				OR
				model.clear_values(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			self.__SYSTEM[self.DATA]={}
			data=self.__SYSTEM[self.DATA]
			#---------------------------------------------------------------------------------
			#	DEFINE VARIBLES 					SET EMPTY MATRIX 
			#----------------------------------------------------------------------------------
			data[self.IDENTIFIABILITY] 				= [[]]				
			data[self.LOCATION]						= [[]]
			data[self.CHIP_WORK]					= [[]]
			data[self.CHIPPED]						= [[]]
			data[self.PASSPORT]						= [[]]
			data[self.PASSPORT_AVAILABLE]  			= [[]]
			data[self.ID_USING] 					= [[]]
			data[self.ID_USING_MARKING]				= [[]]
			data[self.ID_VERIFYING]					= [[]]				
			data[self.MARKINGS_CORRECT] 			= [[]]				
			data[self.DISTINCTIVE_TRAITS] 			= [[]]				
			data[self.OWNER_STA] 					= [[]]				
			data[self.good_id]						= [[]]
			return True
		except Exception as e:
			return False
		#DONE






	
	def use_default_values(self, request=None):	
		"""
		This function should be used to set probability distribution maxtrix to default values\

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/use_default_values --data $request
				model.use_defualt_values(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			self.__SYSTEM[self.DATA]={}
			data=self.__SYSTEM[self.DATA]
			#------------------------------------------------------------------------------------------------------------
			#	VARIABLES 								DEFAULT PROBABILITY DISTRIBUTION MATRIX
			#------------------------------------------------------------------------------------------------------------
			data[self.IDENTIFIABILITY] 					= [[0.1], [0.9]];				
			data[self.LOCATION]							= [[0.5], [0.5]];	
			data[self.CHIP_WORK]						= [[0.2, 0.2], [0.8, 0.8]];
			data[self.CHIPPED]							= [[0.2, 0.2], [0.8, 0.8]];
			data[self.PASSPORT]							= [[0.2, 0.2], [0.8, 0.8]];
			data[self.PASSPORT_AVAILABLE]  				= [[0.2, 0.2], [0.8, 0.8]];
			data[self.ID_USING] 						= [[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
			data[self.ID_USING_MARKING]					= [[0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
			data[self.ID_VERIFYING]						= [[0.7], [0.3]];				
			data[self.MARKINGS_CORRECT] 				= [[0.9], [0.1]];				
			data[self.DISTINCTIVE_TRAITS] 				= [[0.8], [0.2]];				
			data[self.OWNER_STA] 						= [[0.8], [0.2]];				
			data[self.good_id]							= [[0.2,0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8,0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
			return self.load_sizes(request);
		except Exception as e:
			return False
		#DONE







	def set_data(self, request=None):
		"""
		This function should be used to set probability distribution maxtrix\

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/set_data --data $request
				model.set_data(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			if request!= None:
				self.__SYSTEM[self.DATA]=request[self.DATA];
				return self.load_sizes(request);
			else:
				return use_defualt_values(request);
		except Exception as e:
			return False;










	def get_data(self, request=None):
		"""
		This function should be used to Get probability distribution maxtrix\

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/get_data --data $request
				model.get_data(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		return self.__SYSTEM[self.DATA];












	def set_values(self, request=None):
		"""
		This function should be used to Get probability distribution maxtrix. Synonym to get_data function.

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/set_values --data $request
				model.set_values(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		return self.set_data(request);













	def get_values(self, request=None):
		"""
		This function should be used to Get probability distribution maxtrix. Synonym to get_data function.

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/get_values --data $request
				model.get_values(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		return self.get_data(request);









	def declare_variables(self, request=None):
		"""
		This function should be used to declare the variable size

			Request Format:
				request=void

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/declare_variables --data $request
				model.declare_variables(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		#define variables and variables size
		try:	
			self.__SYSTEM[self.VARIABLES]={}
			variables=self.__SYSTEM[self.VARIABLES]
			#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			#	VARIABLE DEFINATION    	SET VARIABLE DEFINITION				VARIABLES						SET VARIABLE				SYMBOLICS 					SET SYMBOLICS 
			#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			self.IDENTIFIABILITY		= "identifiability";		variables[self.IDENTIFIABILITY]			= self.IDENTIFIABILITY;		self.identifiability		= "identifiability" 		# variable symbols are defined so that it is consistent with the mathematical presentation.
			self.LOCATION				= "location";				variables[self.LOCATION]				= self.LOCATION;			self.location 				= "location"				# TODO: all values to be corrected.
			self.CHIP_WORK				= "chip_work";				variables[self.CHIP_WORK]				= self.CHIP_WORK;			self.chip_work 				= "chip_work"				#
			self.CHIPPED				= "chipped";				variables[self.CHIPPED]					= self.CHIPPED;				self.chipped 				= "chipped"
			self.PASSPORT				= "passport";				variables[self.PASSPORT]				= self.PASSPORT;			self.passport 				= "passport"
			self.PASSPORT_AVAILABLE		= "passport_available";		variables[self.PASSPORT_AVAILABLE]		= self.PASSPORT_AVAILABLE;	self.passport_available 	= "passport_available"
			self.ID_USING				= "id_using";				variables[self.ID_USING]				= self.ID_USING;			self.id_using 				= "id_using"
			self.ID_VERIFYING			= "id_verifying";			variables[self.ID_VERIFYING]			= self.ID_VERIFYING;		self.id_verifying 			= "id_verifying"
			self.ID_USING_MARKING		= "id_using_marking";		variables[self.ID_USING_MARKING]		= self.ID_USING_MARKING;	self.id_using_marking 		= "id_using_marking"
			self.MARKINGS_CORRECT		= "markings_correct";		variables[self.MARKINGS_CORRECT]		= self.MARKINGS_CORRECT;	self.markings_correct 		= "markings_correct"
			self.DISTINCTIVE_TRAITS		= "distinctive_traits";		variables[self.DISTINCTIVE_TRAITS]		= self.DISTINCTIVE_TRAITS;	self.distinctive_traits 	= "distinctive_traits"
			self.OWNER_STA				= "owner_sta";				variables[self.OWNER_STA]				= self.OWNER_STA;			self.owner_sta 				= "owner_sta"
			self.GOOD_ID				= "good_id";				variables[self.GOOD_ID]					= self.GOOD_ID;				self.good_id 				= "good_id"
			return True;
		except Exception as e:
			return False
		#DONE








	
	def update_values(self, request):
		"""
		This function should be used to update the probability distribution matrix for all the variables/nodes.

			Request Format:
				request=
				{
					'data'	:
					{
						#for all nodes, do
							'node_name'		:	'probabilty distribution matrix value'
					}
				}

			Usage Format:
				request=
				{
					data:	
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
					}
				}

				curl -X PUT http://bbn.horseid.com/model/update_values --data $request
				OR
				model.update_values(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 


			Mathematical Statement:
				...

		"""
		try:
			s1=self.clear_values(request);
			self.__SYSTEM[self.DATA] = request[self.DATA]
			s2=load_sizes(request);
			return s1 and s2;	
		except Exception as e:
			return False;						
		#DONE









	
	def load_sizes(self, request=None):
		"""
		This function should be used to load the sizes of the variables

			Request Format:
				request=void

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/load_sizes --data $request
				OR
				model.load_sizes(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				for all variables or nodes, load length or sizes of probability distribution matrix to the __SYSTEM.

		"""
		try:
			self.__SYSTEM[self.SIZES]={};
			for key in self.__SYSTEM[self.VARIABLES]:
				self.__SYSTEM[self.SIZES][key] 			= len(self.__SYSTEM[self.DATA][key]);
			return True
		except Exception as e:
			return False
		#DONE










	
	def set_evidences(self, request=None):
		"""
		This function should be used to define or load the parents/evidences for all nodes.
			
			Request Format:
				request=
				{
					evidence: 
					{
						#for all nodes, do:
							node.node_name :	'evidence_value',
					},
					evidence_card: 
					{
						#for all nodes, do:
							node.node_name :	'evidence_card_value',
					}
				}

			Usage Format:

				request=
				{
					'evidence':
					{
						'self.IDENTIFIABILTY'			: 	'evidence_value',
						'self.LOCATION'		 			: 	'location_value',
						'self.CHIP_WORK'	 			:	'chip_work_value',
						'self.PASSPORT'		 			: 	'passport_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_value',
						'self.ID_USING'					:	'id_using_value',
						'self.ID_VERIFYING'				:	'id_verifying_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_value',
						'self.OWNER_STA'				:	'owner_sta_value',
						'self.GOOD_ID'					:	'good_id_value'
					},
					'evidence_card':
					{
						'self.IDENTIFIABILTY'			: 	'evidence_card_value',
						'self.LOCATION'		 			: 	'location_card_value',
						'self.CHIP_WORK'	 			:	'chip_work_card_value',
						'self.PASSPORT'		 			: 	'passport_card_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_card_value',
						'self.ID_USING'					:	'id_using_card_value',
						'self.ID_VERIFYING'				:	'id_verifying_card_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_card_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_card_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_card_value',
						'self.OWNER_STA'				:	'owner_sta_card_value',
						'self.GOOD_ID'					:	'good_id_card_value'
					}
				}

				curl -X PUT http://bbn.horseid.com/model/set_evidences --data $request
				OR
				model.set_evidences(request);


			Response Format:
				response=Boolean
				OR
				response=
				{
					output:	Boolean
				}
				Returns true if it works, else it returns false. Check your request format. 

		"""
		try:
			self.__SYSTEM[self.EVIDENCES]={};				self.__SYSTEM[self.EVIDENCE_CARDS]={};
			evidences=self.__SYSTEM[self.EVIDENCES];		evidence_cards=self.__SYSTEM[self.EVIDENCE_CARDS];		sizes=self.__SYSTEM[self.SIZES];
			if request.has_key(self.EVIDENCES) and request.has_key(self.EVIDENCE_CARDS):
				for key in request[self.EVIDENCES]:
					#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					#	EVIDENCE 						EVIDENCE CARD 								SET DEFUALT EVIDENCE VALUES CONFIG 				SET DEFAULT EVIDENCE CARD VALUES CONFIG
					#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					evidences[key], 					evidence_cards[key] 						= request[self.EVIDENCE][key], 					request[self.EVIDENCE_CARD][key];
			else:
				#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
				#	EVIDENCE 							EVIDENCE CARD 									SET DEFAULT EVIDENCE VALUES CONFIG 								SET DEFAULT EVIDENCE CARD VALUES CONFIG
				#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
				evidences[self.IDENTIFIABILITY], 		evidence_cards[self.IDENTIFIABILITY] 			= None, 														None;
				evidences[self.LOCATION],				evidence_cards[self.LOCATION] 					= None, 														None;
				evidences[self.CHIP_WORK],				evidence_cards[self.CHIP_WORK]					= [self.location],												[sizes[self.LOCATION]];
				evidences[self.CHIPPED],  				evidence_cards[self.CHIPPED]					= [self.location],												[sizes[self.LOCATION]];
				evidences[self.PASSPORT],				evidence_cards[self.PASSPORT]					= [self.location],												[sizes[self.LOCATION]];
				evidences[self.PASSPORT_AVAILABLE],		evidence_cards[self.PASSPORT_AVAILABLE]			= [self.passport],												[sizes[self.PASSPORT]];
				evidences[self.ID_USING],				evidence_cards[self.ID_USING]					= [self.chip_work, self.chipped, self.passport_available],		[sizes[self.CHIP_WORK], sizes[self.CHIPPED], sizes[self.PASSPORT_AVAILABLE]];
				evidences[self.ID_VERIFYING],			evidence_cards[self.ID_VERIFYING]				= None,															None;
				evidences[self.ID_USING_MARKING],		evidence_cards[self.ID_USING_MARKING]			= [self.markings_correct, self.distinctive_traits, self.passport_available],	[sizes[self.MARKINGS_CORRECT], sizes[self.DISTINCTIVE_TRAITS], sizes[self.PASSPORT_AVAILABLE]];
				evidences[self.MARKINGS_CORRECT],		evidence_cards[self.MARKINGS_CORRECT]			= None,															None;
				evidences[self.DISTINCTIVE_TRAITS],		evidence_cards[self.DISTINCTIVE_TRAITS]			= None,															None;
				evidences[self.OWNER_STA],				evidence_cards[self.OWNER_STA]					= None,															None;
				evidences[self.GOOD_ID],				evidence_cards[self.GOOD_ID]					= [self.id_verifying, self.id_using, self.id_using_marking, self.owner_sta, self.identifiability],	[sizes[self.ID_VERIFYING], sizes[self.ID_USING], sizes[self.ID_USING_MARKING], sizes[self.OWNER_STA], sizes[self.IDENTIFIABILITY]];
			return True
		except Exception as e:
			return False
		#DONE







	def load_evidences(self, request=None):
		"""
		This function should be used to define or load the parents/evidences for all nodes.
			
			Request Format:
				request=
				{
					evidence: 
					{
						#for all nodes, do:
							node.node_name :	'evidence_value',
					},
					evidence_card: 
					{
						#for all nodes, do:
							node.node_name :	'evidence_card_value',
					}
				}

			Usage Format:

				request=
				{
					'evidence':
					{
						'self.IDENTIFIABILTY'			: 	'evidence_value',
						'self.LOCATION'		 			: 	'location_value',
						'self.CHIP_WORK'	 			:	'chip_work_value',
						'self.PASSPORT'		 			: 	'passport_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_value',
						'self.ID_USING'					:	'id_using_value',
						'self.ID_VERIFYING'				:	'id_verifying_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_value',
						'self.OWNER_STA'				:	'owner_sta_value',
						'self.GOOD_ID'					:	'good_id_value'
					},
					'evidence_card':
					{
						'self.IDENTIFIABILTY'			: 	'evidence_card_value',
						'self.LOCATION'		 			: 	'location_card_value',
						'self.CHIP_WORK'	 			:	'chip_work_card_value',
						'self.PASSPORT'		 			: 	'passport_card_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_card_value',
						'self.ID_USING'					:	'id_using_card_value',
						'self.ID_VERIFYING'				:	'id_verifying_card_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_card_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_card_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_card_value',
						'self.OWNER_STA'				:	'owner_sta_card_value',
						'self.GOOD_ID'					:	'good_id_card_value'
					}
				}

				curl -X PUT http://bbn.horseid.com/model/load_evidences --data $request
				OR
				model.load_evidences(request);


			Response Format:
				response=Boolean
				OR
				response=
				{
					output:	Boolean
				}
				Returns true if it works, else it returns false. Check your request format. 

		"""
		return self.set_evidences(request);
		#DONE








	
	def set_cpds(self, request=None):
		"""
		This is should be used to load up a conditional probability distritubation table from the current state of the HorseIDBayesianNetwork
			
			Request Format:
				request=
				{
					'variable_value': 
					{
						#for all nodes, do:
							node_name :	'node's probablity distribution matrix value',
					},
					evidence: 
					{
						#for all nodes, do:
							node_name :	'evidence_value',
					},
					evidence_card: 
					{
						#for all nodes, do:
							node_name :	'evidence_card_value',
					}
				}

			Usage Format:

				request=
				{
					'variable_value':
						#NODES 								#PROBABILITY DISTRIBUTION MATRIX
					{
						'self.IDENTIFIABILTY'			: 	'evidence_value',
						'self.LOCATION'		 			: 	'location_value',
						'self.CHIP_WORK'	 			:	'chip_work_value',
						'self.PASSPORT'		 			: 	'passport_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_value',
						'self.ID_USING'					:	'id_using_value',
						'self.ID_VERIFYING'				:	'id_verifying_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_value',
						'self.OWNER_STA'				:	'owner_sta_value',
						'self.GOOD_ID'					:	'good_id_value'
					},
					'evidence':
						#NODES 								#EVIDENCE VALUE
					{
						'self.IDENTIFIABILTY'			: 	'identifiabilt_value',
						'self.LOCATION'		 			: 	'location_value',
						'self.CHIP_WORK'	 			:	'chip_work_value',
						'self.PASSPORT'		 			: 	'passport_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_value',
						'self.ID_USING'					:	'id_using_value',
						'self.ID_VERIFYING'				:	'id_verifying_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_value',
						'self.OWNER_STA'				:	'owner_sta_value',
						'self.GOOD_ID'					:	'good_id_value'
					},
					'evidence_card':
						#NODES 								#EVIDENCE CARD VALUE
					{
						'self.IDENTIFIABILTY'			: 	'evidence_card_value',
						'self.LOCATION'		 			: 	'location_card_value',
						'self.CHIP_WORK'	 			:	'chip_work_card_value',
						'self.PASSPORT'		 			: 	'passport_card_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_card_value',
						'self.ID_USING'					:	'id_using_card_value',
						'self.ID_VERIFYING'				:	'id_verifying_card_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_card_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_card_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_card_value',
						'self.OWNER_STA'				:	'owner_sta_card_value',
						'self.GOOD_ID'					:	'good_id_card_value'
					}
				}

				curl -X PUT http://bbn.horseid.com/model/set_cpds --data $request
				OR
				model.set_cpds(request);


			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			s1,	s2,	s3	=	True,True, True;
			self.__SYSTEM[self.CPDS]={}
			#---------------------------------------------------------------------------------------------------------------------------------------------------
			#	SET 1										SET 2											SET 3
			#---------------------------------------------------------------------------------------------------------------------------------------------------
			cpds=self.__SYSTEM[self.CPDS];				variables=self.__SYSTEM[self.VARIABLES];			evidences=self.__SYSTEM[self.EVIDENCES];
			sizes=self.__SYSTEM[self.SIZES];			data=self.__SYSTEM[self.DATA];					evidence_cards=self.__SYSTEM[self.EVIDENCE_CARDS];
			#---------------------------------------------------------------------------------------------------------------------------------------------------
			if request!=None and request.has_key(self.DATA):
				s1=self.update_values(request);
				s2=self.load_sizes(request);
				s3=self.load_evidences(request); 	
			#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			#	CPDs  						CPD TYPE 					NODE NAMES							NODE POSSIBILITIES SIZE 								VALUES/DATA 							EVIDENCE(DEPENDENCIES) 										EVIDENCE CARD (DEPENDENCY SIZE)
			#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			cpds[self.IDENTIFIABILITY] 		= TabularCPD(variable=variables[self.IDENTIFIABILITY], 			variable_card=sizes[self.IDENTIFIABILITY], 		values=data[self.IDENTIFIABILITY]);			#		None															None
			cpds[self.LOCATION]				= TabularCPD(variable=variables[self.LOCATION], 				variable_card=sizes[self.LOCATION],				values=data[self.LOCATION]);				#		None															None
			cpds[self.CHIPPED] 				= TabularCPD(variable=variables[self.CHIPPED], 					variable_card=sizes[self.CHIPPED], 				values=data[self.CHIPPED], 					evidence=evidences[self.CHIPPED], 					evidence_card=evidence_cards[self.CHIPPED]);
			cpds[self.CHIP_WORK] 			= TabularCPD(variable=variables[self.CHIP_WORK], 				variable_card=sizes[self.CHIP_WORK],			values=data[self.CHIP_WORK], 				evidence=evidences[self.CHIP_WORK], 				evidence_card=evidence_cards[self.CHIP_WORK]);
			cpds[self.PASSPORT] 			= TabularCPD(variable=variables[self.PASSPORT], 				variable_card=sizes[self.PASSPORT],  			values=data[self.PASSPORT], 				evidence=evidences[self.PASSPORT], 					evidence_card=evidence_cards[self.PASSPORT]);
			cpds[self.PASSPORT_AVAILABLE] 	= TabularCPD(variable=variables[self.PASSPORT_AVAILABLE],		variable_card=sizes[self.PASSPORT_AVAILABLE], 	values=data[self.PASSPORT_AVAILABLE], 		evidence=evidences[self.PASSPORT_AVAILABLE], 		evidence_card=evidence_cards[self.PASSPORT_AVAILABLE]);
			cpds[self.ID_USING] 			= TabularCPD(variable=variables[self.ID_USING], 				variable_card=sizes[self.ID_USING],				values=data[self.ID_USING], 				evidence=evidences[self.ID_USING], 					evidence_card=evidence_cards[self.ID_USING]);
			cpds[self.ID_VERIFYING] 		= TabularCPD(variable=variables[self.ID_VERIFYING], 			variable_card=sizes[self.ID_VERIFYING], 		values=data[self.ID_VERIFYING]);			#		None															None
			cpds[self.MARKINGS_CORRECT] 	= TabularCPD(variable=variables[self.MARKINGS_CORRECT], 		variable_card=sizes[self.MARKINGS_CORRECT], 	values=data[self.MARKINGS_CORRECT]);		#		None															None
			cpds[self.DISTINCTIVE_TRAITS] 	= TabularCPD(variable=variables[self.DISTINCTIVE_TRAITS], 		variable_card=sizes[self.DISTINCTIVE_TRAITS],	values=data[self.DISTINCTIVE_TRAITS]);		#		None															None
			cpds[self.ID_USING_MARKING] 	= TabularCPD(variable=variables[self.ID_USING_MARKING], 		variable_card=sizes[self.ID_USING_MARKING], 	values=data[self.ID_USING_MARKING], 		evidence=evidences[self.ID_USING_MARKING],			evidence_card=evidence_cards[self.ID_USING_MARKING]);
			cpds[self.OWNER_STA] 			= TabularCPD(variable=variables[self.OWNER_STA], 				variable_card=sizes[self.OWNER_STA],			values=data[self.OWNER_STA]);				#		None															None
			cpds[self.GOOD_ID] 				= TabularCPD(variable=variables[self.GOOD_ID], 					variable_card=sizes[self.GOOD_ID], 				values=data[self.GOOD_ID], 					evidence=evidences[self.GOOD_ID], 					evidence_card=evidence_cards[self.GOOD_ID]);
			return s1 and s2 and s3
		except Exception as e:
			raise e;
		#DONE







	def load_cpds(self, request=None):	
		"""
		This is synonymous to self.set_cpds 
			
			Request Format:
				request=
				{
					'variable_value': 
					{
						#for all nodes, do:
							node_name :	'node's probablity distribution matrix value',
					},
					evidence: 
					{
						#for all nodes, do:
							node_name :	'evidence_value',
					},
					evidence_card: 
					{
						#for all nodes, do:
							node_name :	'evidence_card_value',
					}
				}

			Usage Format:

				request=
				{
					#for example
					'variable_value':
						#NODES 								#PROBABILITY DISTRIBUTION MATRIX
					{
						'self.IDENTIFIABILTY'			: 	'evidence_value',
						'self.LOCATION'		 			: 	'location_value',
						'self.CHIP_WORK'	 			:	'chip_work_value',
						'self.PASSPORT'		 			: 	'passport_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_value',
						'self.ID_USING'					:	'id_using_value',
						'self.ID_VERIFYING'				:	'id_verifying_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_value',
						'self.OWNER_STA'				:	'owner_sta_value',
						'self.GOOD_ID'					:	'good_id_value'
					},
					'evidence':
						#NODES 								#EVIDENCE VALUES
					{
						'self.IDENTIFIABILTY'			: 	'identifiabilt_value',
						'self.LOCATION'		 			: 	'location_value',
						'self.CHIP_WORK'	 			:	'chip_work_value',
						'self.PASSPORT'		 			: 	'passport_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_value',
						'self.ID_USING'					:	'id_using_value',
						'self.ID_VERIFYING'				:	'id_verifying_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_value',
						'self.OWNER_STA'				:	'owner_sta_value',
						'self.GOOD_ID'					:	'good_id_value'
					},
					'evidence_card':
						#NODES 								#EVIDENCE CARD VALUES
					{
						'self.IDENTIFIABILTY'			: 	'evidence_card_value',
						'self.LOCATION'		 			: 	'location_card_value',
						'self.CHIP_WORK'	 			:	'chip_work_card_value',
						'self.PASSPORT'		 			: 	'passport_card_value',
						'self.PASSPORT_AVALAIBLE'		:	'passport_available_card_value',
						'self.ID_USING'					:	'id_using_card_value',
						'self.ID_VERIFYING'				:	'id_verifying_card_value',
						'self.ID_USING_MARKING'			:	'id_using_marking_card_value',
						'self.MARKINGS_CORRECT'			:	'markings_correct_card_value',
						'self.DISTINCTIVE_TRAITS'		:	'distinctive_traits_card_value',
						'self.OWNER_STA'				:	'owner_sta_card_value',
						'self.GOOD_ID'					:	'good_id_card_value'
					}
				}

				curl -X PUT http://bbn.horseid.com/model/set_evidences --data $request
				OR
				model.set_evidences(request);


			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

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

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/load_sizes --data $request
				model.load_sizes(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

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

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/draw_default_graph --data $request
				OR
				model.draw_defualt_graph(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""	
		try:
			self.horse_id_graph = [
				#--------------------------------------------------------------------------------------------------------------------------------------------		
				#EDGE FROM NODE 			EDGE TO	NODE							#ARROW FROM 							ARROW TO
				#--------------------------------------------------------------------------------------------------------------------------------------------
				(self.IDENTIFIABILITY, 		self.GOOD_ID),							#identifiability 		------> 		good_id
				(self.LOCATION, 			self.CHIPPED),							#location 				------> 		chipped
				(self.LOCATION, 			self.CHIP_WORK),						#location 				------> 		chip_work
				(self.LOCATION, 			self.PASSPORT),							#location  				------> 		passport
				(self.CHIPPED, 				self.ID_USING),							#chipped 				------> 		id_using	
				(self.CHIP_WORK, 			self.ID_USING),							#chip_work  			------> 		id_using
				(self.PASSPORT, 			self.PASSPORT_AVAILABLE),				#passport 				------> 		passport_available			
				(self.PASSPORT_AVAILABLE, 	self.ID_USING),							#passport_available 	------> 		id_using
				(self.MARKINGS_CORRECT, 	self.ID_USING_MARKING),					#markings_correct 		------> 		id_using_marking
				(self.DISTINCTIVE_TRAITS, 	self.ID_USING_MARKING),					#distinctive_traits 	------> 		id_using_marking
				(self.PASSPORT_AVAILABLE, 	self.ID_USING_MARKING),					#passport_available  	------>		 	id_using_marking
				(self.ID_VERIFYING, 		self.GOOD_ID),							#id_verifying  			------> 		good_id
				(self.ID_USING, 			self.GOOD_ID),							#id_using 				------> 		good_id
				(self.ID_USING_MARKING, 	self.GOOD_ID),							#id_using_marking 		------> 		good_id
				(self.OWNER_STA, 			self.GOOD_ID),							#owner_sta 				------> 		good_id
			];
			return True;
		except Exception as e:
			return False;
		#DONE








	def load_graph(self, request):
		"""
		This is synonymous to draw_graph
			
			Request Format:
				request =	{
					'graph': 	
					[
						#for all edges, do
							(edge.from.node_name, 	edge.to.node_name),
					]
				}


			Usage Format:
				request =	{
					'graph': 	
					[
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
					]
				}
				curl -X PUT http://bbn.horseid.com/model/load_graph --data $request
				OR
				model.load_graph(request);
			
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
				request=
				{
					'graph': 
					[
						#for all edges, do
							('from node_name', 'to node_name')
					]
				}
				curl -X PUT http://bbn.horseid.com/model/draw_graph --data $request
				OR
				model.draw_graph(request);


			Usage Format:
				request=
				{
					'graph':	
					[
						#exmaple graph
						#	EDGE FROM NODE					EDGE TO NODE
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
					]
				}
				curl -X PUT http://bbn.horseid.com/model/draw_graph --data $request
				OR
				model.draw_graph(request);


			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. If false, check your request format. 


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


			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/build_model --data $request
				OR
				model.build_model(request);


			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 


			Mathematical Statement:
				...
		"""

		#Build graph and load model: load on start
		try:
			#------------------------------------------------------------------------------------------------------------
			#		methods							METHOD CLASS 					FIRST ARG
			#-------------------------------------------------------------------------------------------------------------------
			self.horse_id_model 				= BayesianModel(				self.horse_id_graph);
			self.load_cpds_to_model(request);
			self.horse_inference 				= VariableElimination(			self.horse_id_model); 
			return True
		except Exception as e:
			return False
		#DONE









	
	def load_cpds_to_model(self, request=None):	
		"""
		This should be used to load the Conditional Probability Distribution Tables on the Horse Identification Bayesain Belief Network model.

			Request Format:
				request=void


			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/load_cpds_to_model --data $request
				OR
				model.load_cpds_to_model(request);


			Response Format:
				response=Boolean
				Returns true if it works, else it returns false. Check your request format. 


			Mathematical Statement:
				...
		"""
		try:
			cpds = self.__SYSTEM[self.CPDS];
			self.horse_id_model.add_cpds(
				#--------------------------------------------------------------------------------------------------------------
				#	SET 1								SET 2								SET 3
				#--------------------------------------------------------------------------------------------------------------
				cpds[self.IDENTIFIABILITY], 		cpds[self.LOCATION], 				cpds[self.CHIP_WORK], 				
				cpds[self.CHIPPED], 				cpds[self.PASSPORT], 				cpds[self.PASSPORT_AVAILABLE], 
				cpds[self.ID_USING], 				cpds[self.ID_VERIFYING], 			cpds[self.ID_USING_MARKING], 		
				cpds[self.MARKINGS_CORRECT],		cpds[self.DISTINCTIVE_TRAITS], 		cpds[self.OWNER_STA], 
				cpds[self.GOOD_ID]);
			return True
		except Exception as e:
			return False
		#DONE







	def load_model(self, request=None):	
		"""
		This should be used to load the the Horse Identification Bayesian Belief Network model after the graph to use have been defined.
		
			Request Format:
				request=void
			
			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/load_model --data $request
				OR
				model.load_model(request);

			Response Format:
				[response=Boolean]
				Returns True if it works, else it returns False. If False, check your request format. 


			Mathematical Statement:
				...
		"""
		return self.build_model(request);
		#DONE








	def train_model(self, request):
		"""
		This should be used to train the Horse Identificiation Bayesian Belief Network.
		
			Request Format:
				request= 
				{ 
					dataset:	
					{
						#for all nodes, do
							'node.node_name'			: 	[datasets value],
					},
					'graph': 
					[
						#for all edges, do
							(edge.from.node_name	, 	edge.to.node_name)
					]
				}

				curl -X PUT http://bbn.horseid.com/model/train_model --data $request
				OR
				model.train_model(request);


			Usage Format:
				request = 
				{ 
					dataset:	
					{
						'self.IDENTIFIABILTY'			: 	[[],[],[],..],
						'self.LOCATION'		 			: 	[[],[],[],..],
						'self.CHIP_WORK'	 			:	[[],[],[],..],
						'self.PASSPORT'		 			: 	[[],[],[],..],
						'self.PASSPORT_AVALAIBLE'		:	[[],[],[],..],
						'self.ID_USING'					:	[[],[],[],..],
						'self.ID_VERIFYING'				:	[[],[],[],..],
						'self.ID_USING_MARKING'			:	[[],[],[],..],
						'self.MARKINGS_CORRECT'			:	[[],[],[],..],
						'self.DISTINCTIVE_TRAITS'		:	[[],[],[],..],
						'self.OWNER_STA'				:	[[],[],[],..],
						'self.GOOD_ID'					:	[[],[],[],..]
					},
					'graph': 
					[
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
						('self.GOOD_ID'					,	self.OWNER_STA)
					]
				}
				curl -X PUT http://bbn.horseid.com/model/train_model --data $request
				OR
				model.train_model(request);


			Response Format:
				response=False 
				OR
				response=
				{
					time:		latest_updated_time,
					accuracy:	current_accuracy
				}


			Mathematical Statement:
				...
		"""
		try:
			self.current_dataframe = pd.DataFrame(request['dataset']);
			if request[self.GRAPH]!=None:
				self.horse_id_model = BayesianModel(request.graph);
			self.horse_id_model.fit(self.current_dataframe);
			self.last_updated_time = "";
			self.current_accuracy =	self.test_model(request);
			return {time: self.last_updated_time, accuracy: self.current_accuracy}
		except Exception as e:
			return False;
		#NEED REVIEW









	def update_model(self, request):
		"""
		This function should be used to update the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request= 
				{ 
					dataset:	
					{
						#for all nodes, do
							node.node_name			: 	value,
					},
					'graph': 
					[
						#for all edges, do
							(edge.from.node_name	, 	edge.to.node_name)
					]
				}


			Usage Format:
				request = 
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
					'graph': 
					[
						#example graph
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
						('self.GOOD_ID'					,	self.OWNER_STA)
					]
				}
				curl -X PUT http://bbn.horseid.com/model/update_model --data $request
				OR
				model.update_model(request);


			Response Format:
				response=False 
				OR
				response=
				{
					time:		latest_updated_time,
					accuracy:	current_accuracy
				}


			Mathematical Statement:
				...
		"""
		#use this to train model online.
		try:
			self.current_dataframe = pd.DataFrame(request['dataset']);#TODO: concatenate instead of assignment
			if request[self.GRAPH]!=None:
				self.horse_id_model = BayesianModel(request.graph);
			self.horse_id_model.fit(self.current_dataframe);
			self.last_updated_time = "";
			self.current_accuracy 	=	self.test_model(request);
			return {'time': self.last_updated_time, 'accuracy': self.current_accuracy};
		except Exception as e:
			return False
		#NEED REVIEW







	
	def test_model(self, request=None):
		"""
		This function should be used to test model accuracy.
		
			Request Format:
				request= 
				{ 
					dataset:	
					{
						#for all nodes, do
							'node.node_name'			: 	value,
					}
				}


			Usage Format:
				request = 
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
					}
				}
				curl -X PUT http://bbn.horseid.com/model/test_model --data $request
				OR
				model.test_model(request);


			Response Format:
				response=False 
				OR
				response=
				{
					time:		latest_updated_time,
					accuracy:	current_accuracy
				}


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
				request=
				{ 	
					'node':	['value'] 
				}


			Usage Format:
				request=
				{ 	
					#example
					'node':	'self.IDENTIFIABILITY' 
				}
				curl -X PUT http://bbn.horseid.com/model/describe_node --data $request
				OR
				model.describe_node(request);


			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 


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

			Usage Format:
				request=None;
				curl -X PUT http://bbn.horseid.com/model/check_model --data $request
				model.check_model(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			return self.horse_id_model.check_model();
		except Exception as e:
			return False;
		#DONE





	def get_nodes(self, request=None):						#TODO: come back and check
		"""
		This function should be used to get nodes that exist in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
		try:
			return self.horse_id_model.nodes;
		except Exception as e:
			return False
		#DONE






	def get_edges(self, request=None):						#come back and check
		"""
		This function should be used to get all the edges that exist in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request=void

			Mathematical Statement:
				...
		"""
		try:
			return self.horse_id_model.edges;
		except Exception as e:
			return False
		#DONE







	def get_cpds(self, request):
		"""
		This function should be used to get all of( or a defined node ) the conditional probability distribution tables that exist in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request=
				{
					'node':	value
				}

			Usage Format:
				request=
				{
					'node':	value
				}
				curl -X PUT http://bbn.horseid.com/model/get_cpds --data $request
				OR
				model.get_cpds(request);

			Response Format:
				response=Boolean
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			node= request[self.NODE] if request.has_key(self.NODE) else None
					#model engine			#request.node
			return self.horse_id_model.get_cpds(node=node);
		except Exception as e:
			return False
		#DONE
	







	def get_cardinality(self, request):	
		"""
		This function should be used to get all of( or a defined node ) cardinality table in the Horse ID Bayesian Belief Network model.
			
			Request Format:
				request=
				{
					'node':	value
				}

			Usage Format:
				request=
				{
					#example
					'node':	self.IDENTIFIABLITY
				}
				curl -X PUT http://bbn.horseid.com/model/get_cardinality --data $request
				OR
				model.get_cardinality(request);

			Response Format:
				response=Boolean
				Returns true if it works, else it returns false. Check your request format. 

			Mathematical Statement:
				...
		"""
		try:
			node=request[self.NODE] if request.has_key(self.NODE) else None
			return self.horse_id_model.get_cardinality(node=node);
		except Exception as e:
			return False
		#DONE
	







	def get_local_independencies(self, request):
		"""
		This function should be used to get all of( or a defined node ) local independencies in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request=
				{
					'variables':	[node_names, ... ]
				}

			Usage Format:
				request=
				{
					#example
					'variables':	[self.IDENTIFIABLITY, self.CHIP_WORK]
				}
				curl -X PUT http://bbn.horseid.com/model/get_local_independencies --data $request
				OR
				model.get_local_independencies(request);

			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 
				...
		"""
		try:
			variables= request[self.VARIABLES] if request.has_key(self.VARIABLES) else None
			#model engine							#request.variables
			return self.horse_id_model.local_independencies(variables=request.variables);
		except Exception as e:
			return False
		#DONE








	def get_active_trail_nodes(self, request):
		"""
		This function should be used to get all of( or a defined node ) active trail nodes in the Horse ID Bayesian Belief Network model.
		
			Request Format:
				request 	=	{
					'variables':		[values], 
					'observed':			values
				}


			Usage Format:
				request=
				{
					#for example
					'variables':	[self.IDENTIFIABLITY, self.CHIP_WORK],
					'observed':		self.PASSPORT
				}
				curl -X PUT http://bbn.horseid.com/model/get_active_trail_nodes --data $request
				OR
				model.get_active_trail_nodes(request);


			Response Format:
				[response=Boolean]
				Returns true if it works, else it returns false. Check your request format. 


			Mathematical Statement:
				...
		"""
		try:
			variables = request[self.VARIABLES] if request.has_key(self.VARIABLES) else None
			observerd = request[self.OBSERVED] if request.has_key(self.OBSERVED) else None
				#model engine						#request.variables, 	request.observed;
			return self.horse_id_model.active_trail_nodes(variables=variables, 	observed=observed)
		except Exception as e:
			return False;
		#DONE












	def query(self, request):
		"""
		This function should be used to query the Horse ID Bayesian Belief Network model and make inference via Variable Elimination Method.
		
			Request Format:
				request=	
				{
					'variables':	
					[ 
						variable_symbols,... 

					], 
					'evidence':	
					[ 
						(node_name, evidence_value)
					], 
					'elimination_order':	value
				}

			Usage Format:
				request=	
				{
					'variables':	
					[ 
						#for example
						variable_symbols,... 

					], 
					'evidence':	
					[ 
						#for example
						(node_name, evidence_value)
					], 
					#for example
					'elimination_order':	value
				}
				curl -X PUT http://bbn.horseid.com/model/query --data $request
				OR
				model.query(request);

			Response Format:

			Mathematical Statement:
		"""
		try:
			variables 			=request[self.VARIABLES] if request.has_key(self.VARIABLES) else None;
			evidences 			=request[self.EVIDENCES] if request.has_key(self.EVIDENCE) else None;
			elimination_order 	=request[self.ELIMINATION_ORDER] if request.has_key(self.ELIMINATION_ORDER) else None;
					#inference engine		#request.variables 			request.evidence 		request.elimination_order
			return self.horse_inference.query(variables=variables, 		evidence=evidences, 		elimination_order=elimination_order);
		except Exception as e:
			return False
		#DONE










	def map_query(self, request):
		"""
		This function should be used to query the Horse ID Bayesian Belief Network model map and make inference via Variable Elimination Method.
		
			Request Format:
				request=	
				{
					'variables':	
					[ 
						variable_symbols,... 

					], 
					'evidence':	
					[ 
						(node_name, evidence_value)
					], 
					'elimination_order':	value
				}

			Usage Format:
				request=	
				{
					'variables':	
					[ 
						#for example
						variable_symbols,... 

					], 
					'evidence':	
					[ 
						#for example
						(node_name, evidence_value)
					], 
					'elimination_order':	value
				}
				curl -X PUT http://bbn.horseid.com/model/map_query --data $request
				OR
				model.map_query(request);

			Response Format:

			Mathematical Statement:
				...
		"""
		try:
			variables 			=request[self.VARIABLES] if request.has_key(self.VARIABLES) else None;
			evidences 			=request[self.EVIDENCES] if request.has_key(self.EVIDENCES) else None;
			elimination_order 	=request[self.ELIMINATION_ORDER] if request.has_key(self.ELIMINATION_ORDER) else None;
					#inference engine		#request.variables 			request.evidence 		request.elimination_order
			return self.horse_inference.query(variables=variables, 		evidence=evidences, 		elimination_order=elimination_order);
		except Exception as e:
			return False
		#DONE











