#using pgmpy for probabilistic graphical modelling of Bayesian Network of HorseID
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import pandas as pd;




class HorseIDBayesianNetwork(object):

	SYSTEM={}
	SPACE='space'
	NODE='node'
	DATA='data'
	DATASET='dataset'
	GRAPH='graph'
	SIZE='size'
	CPD="cpd"
	VARIABLES='variables'
	EVIDENCE='evidence'
	EVIDENCE_CARD='evidence_card'
	ELIMINATION_ORDER='elimination_order'
	OBSERVED="observed"

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


	def start(self, request=None):
		"""
		This should be use for starting the default Horse Identification Bayesian Belief Network system. Builds and Run the default model.
			
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
		return s1 and s2 and s3 and s4 and s5 and s6 and s7;
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
			#------------------------------------------------------------------------------------------------------------
			# VARIABLE SPACE 							ALL POSSIBLE VALUES
			#------------------------------------------------------------------------------------------------------------
			self.SYSTEM[self.SPACE] = {};
			self.SYSTEM[self.SPACE][self.IDENTIFIABILITY] 				= [0, 1];								# If identifiability is good or not.
			self.SYSTEM[self.SPACE][self.LOCATION]						= ["ireland", "not_ireland"];			# Currently using 2 locations subsets. Ireland and Not-Ireland.
			self.SYSTEM[self.SPACE][self.CHIP_WORK]						= [True, False];
			self.SYSTEM[self.SPACE][self.PASSPORT]						= [True, False];
			self.SYSTEM[self.SPACE][self.PASSPORT_AVAILABLE]			= [True, False];	
			self.SYSTEM[self.SPACE][self.ID_USING]						= [True, False];
			self.SYSTEM[self.SPACE][self.ID_VERIFYING]					= [True, False];
			self.SYSTEM[self.SPACE][self.ID_USING_MARKING]				= [True, False];
			self.SYSTEM[self.SPACE][self.MARKINGS_CORRECT]				= [True, False];
			self.SYSTEM[self.SPACE][self.DISTINCTIVE_TRAITS]			= [True, False];
			self.SYSTEM[self.SPACE][self.OWNER_STA]						= [True, False];
			self.SYSTEM[self.SPACE][self.GOOD_ID]						= [True, False];
			return True
		except Exception as e:
			return e
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
			#---------------------------------------------------------------------------------
			#	DEFINE VARIBLES 								SET EMPTY MATRIX 
			#----------------------------------------------------------------------------------
			self.SYSTEM[self.DATA]={}
			self.SYSTEM[self.DATA][self.IDENTIFIABILITY] 			= [[]]				
			self.SYSTEM[self.DATA][self.LOCATION]					= [[]]
			self.SYSTEM[self.DATA][self.CHIP_WORK]					= [[]]
			self.SYSTEM[self.DATA][self.CHIPPED]					= [[]]
			self.SYSTEM[self.DATA][self.PASSPORT]					= [[]]
			self.SYSTEM[self.DATA][self.PASSPORT_AVAILABLE]  		= [[]]
			self.SYSTEM[self.DATA][self.ID_USING] 					= [[]]
			self.SYSTEM[self.DATA][self.ID_USING_MARKING]			= [[]]
			self.SYSTEM[self.DATA][self.ID_VERIFYING]				= [[]]				
			self.SYSTEM[self.DATA][self.MARKINGS_CORRECT] 			= [[]]				
			self.SYSTEM[self.DATA][self.DISTINCTIVE_TRAITS] 		= [[]]				
			self.SYSTEM[self.DATA][self.OWNER_STA] 					= [[]]				
			self.SYSTEM[self.DATA][self.good_id]					= [[]]
			return True
		except Exception as e:
			return e
		#DONE







	#feel free to come and set different default Probability Distribution Matrix manually
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
			self.SYSTEM[self.DATA]={}
			#------------------------------------------------------------------------------------------------------------
			#	VARIABLES 										DEFAULT PROBABILITY DISTRIBUTION MATRIX
			#------------------------------------------------------------------------------------------------------------
			self.SYSTEM[self.DATA][self.IDENTIFIABILITY] 				= [[0.1], [0.9]];				
			self.SYSTEM[self.DATA][self.LOCATION]						= [[0.5], [0.5]];	
			self.SYSTEM[self.DATA][self.CHIP_WORK]						= [[0.2, 0.2], [0.8, 0.8]];
			self.SYSTEM[self.DATA][self.CHIPPED]						= [[0.2, 0.2], [0.8, 0.8]];
			self.SYSTEM[self.DATA][self.PASSPORT]						= [[0.2, 0.2], [0.8, 0.8]];
			self.SYSTEM[self.DATA][self.PASSPORT_AVAILABLE]  			= [[0.2, 0.2], [0.8, 0.8]];
			self.SYSTEM[self.DATA][self.ID_USING] 						= [[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
			self.SYSTEM[self.DATA][self.ID_USING_MARKING]				= [[0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
			self.SYSTEM[self.DATA][self.ID_VERIFYING]					= [[0.7], [0.3]];				
			self.SYSTEM[self.DATA][self.MARKINGS_CORRECT] 				= [[0.9], [0.1]];				
			self.SYSTEM[self.DATA][self.DISTINCTIVE_TRAITS] 			= [[0.8], [0.2]];				
			self.SYSTEM[self.DATA][self.OWNER_STA] 						=	 [[0.8], [0.2]];				
			self.SYSTEM[self.DATA][self.good_id]						= [[0.2,0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8,0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
			return self.load_sizes(request);
		except Exception as e:
			return e
		#DONE









	def declare_variables(self, request=None):
		"""
		This function should be used to declare the variable size

			Request Format:
				request=void

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
		#define variables and variables size
		try:	
			#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			#	VARIABLE DEFINATION    	SET VARIABLE DEFINITION				VARIABLES										SET VARIABLE				SYMBOLICS 					SET SYMBOLICS 
			#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			self.SYSTEM[self.VARIABLES]={}
			self.IDENTIFIABILITY		= "identifiability";		self.SYSTEM[self.VARIABLES][self.IDENTIFIABILITY]		= self.IDENTIFIABILITY;		self.identifiability		= "identifiability" 		# variable symbols are defined so that it is consistent with the mathematical presentation.
			self.LOCATION				= "location";				self.SYSTEM[self.VARIABLES][self.LOCATION]				= self.LOCATION;			self.location 				= "location"				# TODO: all values to be corrected.
			self.CHIP_WORK				= "chip_work";				self.SYSTEM[self.VARIABLES][self.CHIP_WORK]				= self.CHIP_WORK;			self.chip_work 				= "chip_work"				#
			self.CHIPPED				= "chipped";				self.SYSTEM[self.VARIABLES][self.CHIPPED]				= self.CHIPPED;				self.chipped 				= "chipped"
			self.PASSPORT				= "passport";				self.SYSTEM[self.VARIABLES][self.PASSPORT]				= self.PASSPORT;			self.passport 				= "passport"
			self.PASSPORT_AVAILABLE		= "passport_available";		self.SYSTEM[self.VARIABLES][self.PASSPORT_AVAILABLE]	= self.PASSPORT_AVAILABLE;	self.passport_available 	= "passport_available"
			self.ID_USING				= "id_using";				self.SYSTEM[self.VARIABLES][self.ID_USING]				= self.ID_USING;			self.id_using 				= "id_using"
			self.ID_VERIFYING			= "id_verifying";			self.SYSTEM[self.VARIABLES][self.ID_VERIFYING]			= self.ID_VERIFYING;		self.id_verifying 			= "id_verifying"
			self.ID_USING_MARKING		= "id_using_marking";		self.SYSTEM[self.VARIABLES][self.ID_USING_MARKING]		= self.ID_USING_MARKING;	self.id_using_marking 		= "id_using_marking"
			self.MARKINGS_CORRECT		= "markings_correct";		self.SYSTEM[self.VARIABLES][self.MARKINGS_CORRECT]		= self.MARKINGS_CORRECT;	self.markings_correct 		= "markings_correct"
			self.DISTINCTIVE_TRAITS		= "distinctive_traits";		self.SYSTEM[self.VARIABLES][self.DISTINCTIVE_TRAITS]	= self.DISTINCTIVE_TRAITS;	self.distinctive_traits 	= "distinctive_traits"
			self.OWNER_STA				= "owner_sta";				self.SYSTEM[self.VARIABLES][self.OWNER_STA]				= self.OWNER_STA;			self.owner_sta 				= "owner_sta"
			self.GOOD_ID				= "good_id";				self.SYSTEM[self.VARIABLES][self.GOOD_ID]				= self.GOOD_ID;				self.good_id 				= "good_id"
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
			for node_name in self[self.DATA]:
				#------------------------------------------------------------------------------------------------------------
				#	DEFINE VARIABLES 						SET VALUES 
				#------------------------------------------------------------------------------------------------------------
				self.SYSTEM[self.DATA][node_name] 					= request[self.DATA][node_name];
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
				for all variables or nodes, load length or sizes of probability distribution matrix to the system.

		"""
		try:
			self.SYSTEM[self.SIZE]={};
			for key in self.SYSTEM[self.VARIABLES]:
				self.SYSTEM[self.SIZE][key] 			= len(self.SYSTEM[self.DATA][key]);
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
		#define variable dependencies and dependency size(evidence and evidence card)
		try:
			self.SYSTEM[self.EVIDENCE],		self.SYSTEM[self.EVIDENCE_CARD]		=	{},		{};
			if type(request) == type(None) or type(request[self.EVIDENCE]) == type(None) or type(request[self.EVIDENCE_CARD])==type(None):
				#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
				#EVIDENCE 												EVIDENCE CARD 													SET DEFUALT EVIDENCE VALUES CONFIG 							SET DEFAULT EVIDENCE CARD VALUES CONFIG
				#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
				self.SYSTEM[self.EVIDENCE][self.IDENTIFIABILITY], 		self.SYSTEM[self.EVIDENCE_CARD][self.IDENTIFIABILITY] 			= None, 														None;
				self.SYSTEM[self.EVIDENCE][self.LOCATION],				self.SYSTEM[self.EVIDENCE_CARD][self.LOCATION] 					= None, 														None;
				self.SYSTEM[self.EVIDENCE][self.CHIP_WORK],				self.SYSTEM[self.EVIDENCE_CARD][self.CHIP_WORK]					= [self.location],												[self.SYSTEM[self.SIZE][self.LOCATION]];
				self.SYSTEM[self.EVIDENCE][self.CHIPPED],  				self.SYSTEM[self.EVIDENCE_CARD][self.CHIPPED]					= [self.location],												[self.SYSTEM[self.SIZE][self.LOCATION]];
				self.SYSTEM[self.EVIDENCE][self.PASSPORT],				self.SYSTEM[self.EVIDENCE_CARD][self.PASSPORT]					= [self.location],												[self.SYSTEM[self.SIZE][self.LOCATION]];
				self.SYSTEM[self.EVIDENCE][self.PASSPORT_AVAILABLE],	self.SYSTEM[self.EVIDENCE_CARD][self.PASSPORT_AVAILABLE]		= [self.passport],												[self.SYSTEM[self.SIZE][self.PASSPORT]];
				self.SYSTEM[self.EVIDENCE][self.ID_USING],				self.SYSTEM[self.EVIDENCE_CARD][self.ID_USING]					= [self.chip_work, self.chipped, self.passport_available],		[self.SYSTEM[self.SIZE][self.CHIP_WORK], self.SYSTEM[self.SIZE][self.CHIPPED], self.SYSTEM[self.SIZE][self.PASSPORT_AVAILABLE]];
				self.SYSTEM[self.EVIDENCE][self.ID_VERIFYING],			self.SYSTEM[self.EVIDENCE_CARD][self.ID_VERIFYING]				= None,															None;
				self.SYSTEM[self.EVIDENCE][self.ID_USING_MARKING],		self.SYSTEM[self.EVIDENCE_CARD][self.ID_USING_MARKING]			= [self.markings_correct, self.distinctive_traits, self.passport_available],	[self.SYSTEM[self.SIZE][self.MARKINGS_CORRECT], self.SYSTEM[self.SIZE][self.DISTINCTIVE_TRAITS], self.SYSTEM[self.SIZE][self.PASSPORT_AVAILABLE]];
				self.SYSTEM[self.EVIDENCE][self.MARKINGS_CORRECT],		self.SYSTEM[self.EVIDENCE_CARD][self.MARKINGS_CORRECT]			= None,															None;
				self.SYSTEM[self.EVIDENCE][self.DISTINCTIVE_TRAITS],	self.SYSTEM[self.EVIDENCE_CARD][self.DISTINCTIVE_TRAITS]		= None,															None;
				self.SYSTEM[self.EVIDENCE][self.OWNER_STA],				self.SYSTEM[self.EVIDENCE_CARD][self.OWNER_STA]					= None,															None;
				self.SYSTEM[self.EVIDENCE][self.GOOD_ID],				self.SYSTEM[self.EVIDENCE_CARD][self.GOOD_ID]					= [self.id_verifying, self.id_using, self.id_using_marking, self.owner_sta, self.identifiability],	[self.SYSTEM[self.SIZE][self.ID_VERIFYING], self.SYSTEM[self.SIZE][self.ID_USING], self.SYSTEM[self.SIZE][self.ID_USING_MARKING], self.SYSTEM[self.SIZE][self.OWNER_STA], self.SYSTEM[self.SIZE][self.IDENTIFIABILITY]];
			else:
				for key in request[self.EVIDENCE]:
					#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					#	EVIDENCE 											EVIDENCE CARD 								SET DEFUALT EVIDENCE VALUES CONFIG 				SET DEFAULT EVIDENCE CARD VALUES CONFIG
					#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					self.SYSTEM[self.EVIDENCE][key], 					self.SYSTEM[self.EVIDENCE_CARD][key] 			= request[self.EVIDENCE][key], 					request[self.EVIDENCE_CARD][key];
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
			self.SYSTEM[self.CPD]={}
			if type(request)!=type(None) and type(request.data)!=type(None):
				s1=self.update_values(request);
				s2=self.load_sizes(request);
				s3=self.load_evidences(request); 	
				
			#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			#	CPDs  									CPD TYPE 						NODE NAMES							NODE POSSIBILITIES SIZE 								VALUES 												EVIDENCE(DEPENDENCIES) 										EVIDENCE CARD (DEPENDENCY SIZE)
			#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			self.SYSTEM[self.CPD][self.IDENTIFIABILITY] 	= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.IDENTIFIABILITY], 		variable_card=self.SYSTEM[self.SIZE][self.IDENTIFIABILITY], 	values=self.SYSTEM[self.DATA][self.IDENTIFIABILITY]);		#		None															None
			self.SYSTEM[self.CPD][self.LOCATION]			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.LOCATION], 				variable_card=self.SYSTEM[self.SIZE][self.LOCATION],			values=self.SYSTEM[self.DATA][self.LOCATION]);				#		None															None
			self.SYSTEM[self.CPD][self.CHIPPED] 			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.CHIPPED], 				variable_card=self.SYSTEM[self.SIZE][self.CHIPPED], 			values=self.SYSTEM[self.DATA][self.CHIPPED], 				evidence=self.SYSTEM[self.EVIDENCE][self.CHIPPED], 					evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.CHIPPED]);
			self.SYSTEM[self.CPD][self.CHIP_WORK] 			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.CHIP_WORK], 				variable_card=self.SYSTEM[self.SIZE][self.CHIP_WORK],			values=self.SYSTEM[self.DATA][self.CHIP_WORK], 				evidence=self.SYSTEM[self.EVIDENCE][self.CHIP_WORK], 				evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.CHIP_WORK]);
			self.SYSTEM[self.CPD][self.PASSPORT] 			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.PASSPORT], 				variable_card=self.SYSTEM[self.SIZE][self.PASSPORT],  			values=self.SYSTEM[self.DATA][self.PASSPORT], 				evidence=self.SYSTEM[self.EVIDENCE][self.PASSPORT], 				evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.PASSPORT]);
			self.SYSTEM[self.CPD][self.PASSPORT_AVAILABLE] 	= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.PASSPORT_AVAILABLE],		variable_card=self.SYSTEM[self.SIZE][self.PASSPORT_AVAILABLE], 	values=self.SYSTEM[self.DATA][self.PASSPORT_AVAILABLE], 	evidence=self.SYSTEM[self.EVIDENCE][self.PASSPORT_AVAILABLE], 		evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.PASSPORT_AVAILABLE]);
			self.SYSTEM[self.CPD][self.ID_USING] 			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.ID_USING], 				variable_card=self.SYSTEM[self.SIZE][self.ID_USING],			values=self.SYSTEM[self.DATA][self.ID_USING], 				evidence=self.SYSTEM[self.EVIDENCE][self.ID_USING], 				evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.ID_USING]);
			self.SYSTEM[self.CPD][self.ID_VERIFYING] 		= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.ID_VERIFYING], 			variable_card=self.SYSTEM[self.SIZE][self.ID_VERIFYING], 		values=self.SYSTEM[self.DATA][self.ID_VERIFYING]);			#		None															None
			self.SYSTEM[self.CPD][self.MARKINGS_CORRECT] 	= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.MARKINGS_CORRECT], 		variable_card=self.SYSTEM[self.SIZE][self.MARKINGS_CORRECT], 	values=self.SYSTEM[self.DATA][self.MARKINGS_CORRECT]);		#		None															None
			self.SYSTEM[self.CPD][self.DISTINCTIVE_TRAITS] 	= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.DISTINCTIVE_TRAITS], 	variable_card=self.SYSTEM[self.SIZE][self.DISTINCTIVE_TRAITS],	values=self.SYSTEM[self.DATA][self.DISTINCTIVE_TRAITS]);	#		None															None
			self.SYSTEM[self.CPD][self.ID_USING_MARKING] 	= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.ID_USING_MARKING], 		variable_card=self.SYSTEM[self.SIZE][self.ID_USING_MARKING], 	values=self.SYSTEM[self.DATA][self.ID_USING_MARKING], 		evidence=self.SYSTEM[self.EVIDENCE][self.ID_USING_MARKING],			evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.ID_USING_MARKING]);
			self.SYSTEM[self.CPD][self.OWNER_STA] 			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.OWNER_STA], 				variable_card=self.SYSTEM[self.SIZE][self.OWNER_STA],			values=self.SYSTEM[self.DATA][self.OWNER_STA]);				#		None															None
			self.SYSTEM[self.CPD][self.GOOD_ID] 			= TabularCPD(variable=self.SYSTEM[self.VARIABLES][self.GOOD_ID], 				variable_card=self.SYSTEM[self.SIZE][self.GOOD_ID], 			values=self.SYSTEM[self.DATA][self.GOOD_ID], 				evidence=self.SYSTEM[self.EVIDENCE][self.GOOD_ID], 					evidence_card=self.SYSTEM[self.EVIDENCE_CARD][self.GOOD_ID]);
			return s1 and s2 and s3
		except Exception as e:
			return False
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
			self.horse_id_model.add_cpds(
				#----------------------------------------------------------------------------------------------------------------------------------------------
				#	#SET 1												#SET 2												#SET 3
				#----------------------------------------------------------------------------------------------------------------------------------------------
				self.SYSTEM[self.CPD][self.IDENTIFIABILITY], 		self.SYSTEM[self.CPD][self.LOCATION], 				self.SYSTEM[self.CPD][self.CHIP_WORK], 				
				self.SYSTEM[self.CPD][self.CHIPPED], 				self.SYSTEM[self.CPD][self.PASSPORT], 				self.SYSTEM[self.CPD][self.PASSPORT_AVAILABLE], 
				self.SYSTEM[self.CPD][self.ID_USING], 				self.SYSTEM[self.CPD][self.ID_VERIFYING], 			self.SYSTEM[self.CPD][self.ID_USING_MARKING], 		
				self.SYSTEM[self.CPD][self.MARKINGS_CORRECT],		self.SYSTEM[self.CPD][self.DISTINCTIVE_TRAITS], 	self.SYSTEM[self.CPD][self.OWNER_STA], 
				self.SYSTEM[self.CPD][self.GOOD_ID]);
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
			self.current_dataframe = pd.DataFrame(request.data);
			if type(request.graph) != type(None):
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
			self.current_dataframe = pd.DataFrame(request.dataset);#TODO: concatenate instead of assignment
			if type(request.graph) != type(None):
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
			node= request[self.NODE] if request.has_key(self.NODE) else None
			#model engine							#request.node
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
			evidence 			=request[self.EVIDENCE] if request.has_key(self.EVIDENCE) else None;
			elimination_order 	=request[self.ELIMINATION_ORDER] if request.has_key(self.ELIMINATION_ORDER) else None;
					#inference engine		#request.variables 			request.evidence 		request.elimination_order
			return self.horse_inference.query(variables=variables, 		evidence=evidence, 		elimination_order=elimination_order);
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
			evidence 			=request[self.EVIDENCE] if request.has_key(self.EVIDENCE) else None;
			elimination_order 	=request[self.ELIMINATION_ORDER] if request.has_key(self.ELIMINATION_ORDER) else None;
					#inference engine		#request.variables 			request.evidence 		request.elimination_order
			return self.horse_inference.query(variables=variables, 		evidence=evidence, 		elimination_order=elimination_order);
		except Exception as e:
			return False
		#DONE











