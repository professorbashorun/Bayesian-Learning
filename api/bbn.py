#using pgmpy for probabilistic graphical modelling of Bayesian Network of HorseID
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import urllib2 as url;
import pandas as pd;




class HorseIDBayesianNetwork(object):


	def build(self):

		self.initialise_space();
		self.define_universe();
		self.use_default_values();
		self.declare_variables();
		self.define_evidences();
		self.define_cpds();
		self.draw_default_graph();
		return True;




	def run(self):
		self.load_model();
		return True;





	def update(self, dataframe):
		self.update_model();
		return True;






	def initialise_space(self):
		
		# VARIABLE SPACE 						POSSIBLE VALUES
		self.identifiablity_space 				= [0, 1];														# If the outcome of the previous id is GOOD, then 1; else if it is not GOOD then 0;
		self.location_space 					= ["ireland", "england", "united state", "poland", "whales"];	# Currently using 5 locations in the EU as default.
		self.chip_work_space					= [True, False];												# If 
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





	def define_universe(self):
		self.clear_values();
		self.declare_variables();
		self.universe = set([
			#SET 1									SET 2						SELF 3
			self.identifiability_values, 		self.location_values, 			self.chip_work_values, 
			self.chipped_values, 				self.passport_values, 			self.passport_available_values, 
			self.id_using_values, 				self.id_verifying_values, 		self.id_using_marking_size, 
			self.markings_correct_values,		self.distinctive_traits_values,	self.owner_sta_values,
			self.good_id_values
		]);
		return True;






	def clear_values(self):

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






	#define variables' conditional probability distribution values
	"""
		
	"""
	def use_default_values(self):
		#VARIABLES 								DEFAULT PROBABILITY TENSORS
		self.dentifiability_values 				= [[0.1], [0.9]];				
		self.location_values					= [[0.5], [0.5]];	
		self.chip_work_values 					= [[0.2, 0.2], [0.8, 0.8]];
		self.chipped_values 					= [[0.2, 0.2], [0.8, 0.8]];
		self.passport_values					= [[0.2, 0.2], [0.8, 0.8]];
		self.passport_available_values  		= [[0.8, 0.2], [0.2, 0.8]];
		self.id_using_values 					= [[0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
		self.id_verifying_values				= [[0.7], [0.3]];				
		self.id_using_marking_values			= [[0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], [0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
		self.markings_correct_values 			= [[0.9], [0.1]];				
		self.distinctive_traits_values 			= [[0.8], [0.2]];				
		self.owner_sta_values 					= [[0.8], [0.2]];				
		self.good_id_values						= [[0.2,0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2, 0.2, 0.2 , 0.2, 0.2, 0.2 , 0.2], 
												   [0.8,0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8, 0.8, 0.8 , 0.8, 0.8, 0.8 , 0.8]];
		return True;







	def declare_variables(self):
		#define variables and variables size

		#VARIABLE DEFINATION    	SYMBOLICS					VARIABLE SIZE 					VARIABLE DEFINITION 	SYMBOLICS 		SET VARIABLE SIZE
		self.IDENTIFIABILITY,		self.identifiability, 		self.identifiability_size 		= "indentifiabilty",		"V0", 		len(self.identifiability_values); 		# variable symbols are defined so that it is consistent with the mathematical presentation.
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
		return True;





	#use this to update dataset values for cpds
	def update_values(self, dataframe):

		self.clear_values();
		#DEFINE VARIBLES 						SET VALUES 
		self.identifiability_values 			= self.identifiability_values.append(dataframe[PREVIOUS_ID]);
		self.location_values 					= self.location_values.append(dataframe[LOCATION]);
		self.chip_work_values 					= self.chip_work_values.append(dataframe[CHIP_WORK]);
		self.chipped_values 					= self.chipped_values.append(dataframe[CHIPPED]);
		self.passport_values 					= self.passport_values.append(dataframe[PASSPORT]);
		self.passport_available_values 			= self.passport_available_values.append(dataframe[PASSPORT_AVAILABLE]);
		self.id_using_values 					= self.id_using_values.append(dataframe[ID_USING]);
		self.id_verifying_values 				= self.id_verifying_values.append(dataframe[ID_VERIFYING]);
		self.id_using_marking_values 			= self.id_using_marking_values.append(dataframe[ID_USING_MARKING]);
		self.markings_correct_values 			= self.markings_correct_values.append(dataframe[MARKINGS_CORRECT]);
		self.distinctive_traits_values 			= self.distinctive_traits_values.append(dataframe[DISTINCTIVE_TRAITS]);
		self.owner_sta_values 					= self.owner_sta_values.append(dataframe[OWNER_STA]);
		self.good_id_values 					= self.good_id_values.append(dataframe[GOOD_ID]);
		return load_sizes();







	#this declares and initialises the variables sizes to be used
	def load_sizes(self):

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
		return True;








	#define variable dependencies and dependency size(evidence and evidence card)
	def define_evidences(self):

		#EVIDENCE 								EVIDENCE CARD 						EVIDEDENCE VALUE 											ENVIDENCE CARD VALUES
		self.identifiability_evidence, 		self.identifiability_evidence_card 			= None, 													None;
		self.location_evidence,				self.location_evidence_card 				= None, 													None;
		self.chip_work_evidence,			self.chip_work_evidence_card				= [self.location],											[self.location_size];
		self.chipped_evidence, 				self.chipped_evidence_card					= [self.location],											[self.location_size];
		self.passport_evidence,				self.passport_evidence_card					= [self.location],											[self.location_size];
		self.passport_available_evidence,	self.passport_available_evidence_card		= [self.passport],											[self.passport_size];
		self.id_using_evidence,				self.id_using_evidence_card					= [self.chip_work, self.chipped, self.passport_available],	[self.chip_work_size, self.chipped_size, self.passport_available_size];
		self.id_verifying_evidence,			self.id_verifying_evidence_card				= None,														None;
		self.id_using_marking_evidence,		self.id_using_marking_evidence_card			= [markings_correct, distinctive_traits],					[markings_correct_size, distinctive_traits_size];
		self.markings_correct_evidence,		self.markings_correct_evidence_card			= None,														None;
		self.distinctive_traits_evidence,	self.distinctive_traits_evidence_card		= None,														None;
		self.owner_sta_evidence,			self.owner_sta_evidence_card				= None,														None;
		self.good_id_evidence,				self.good_id_evidence_card					= [self.id_verifying, 				self.id_using, 			self.id_using_marking, 			self.owner_sta, self.identifiability],	[self.id_verifying_size, 			self.id_using_size, 	self.id_using_marking_size, 	self.owner_sta_size, self.identifiability_size];
		return True;








	#define node cpds: load this on start
	def define_cpds(self):

		#	CPDs  					CPD TYPE 				VARIABLE 					VARIABLE SIZE 							VALUES 								EVIDENCE(DEPENDENCIES) 					EVIDENCE CARD (DEPENDENCY SIZE)
		self.identifiability_cpd 	= TabularCPD(variable=self.identifiability, 	variable_card=self.identifiability_size, 	values=self.identifiability_values);
		self.location_cpd 			= TabularCPD(variable=self.location, 			variable_card=self.location_size, 			values=self.location_values);
		self.chipped_cpd 			= TabularCPD(variable=self.chipped, 			variable_card=self.chipped_size, 			values=self.chipped_values, 				evidence=self.chipped_evidence, 				evidence_card=self.chipped_evidence_card);
		self.chip_work_cpd 			= TabularCPD(variable=self.chip_work, 			variable_card=self.chip_work_size, 			values=self.chip_work_values, 				evidence=self.chip_work_evidence, 				evidence_card=self.chip_work_evidence_card);
		self.passport_cpd 			= TabularCPD(variable=self.passport, 			variable_card=self.self.passport_size, 		values=self.self.passport_values, 			evidence=self.passport_evidence, 				evidence_card=self.passport_evidence_card);
		self.passport_available_cpd = TabularCPD(variable=self.passport_available,	variable_card=self.passport_available_size,	values=self.passport_available_values, 		evidence=self.passport_available_evidence, 		evidence_card=self.passport_available_evidence_card);
		self.id_using_cpd 			= TabularCPD(variable=self.id_using, 			variable_card=self.id_using_size, 			values=self.id_using_values, 				evidence=self.id_using_evidence, 				evidence_card=self.id_using_evidence_card);
		self.id_verifying_cpd 		= TabularCPD(variable=self.id_verifying, 		variable_card=self.id_verifying_size, 		values=self.id_verifying_values);
		self.markings_correct_cpd 	= TabularCPD(variable=self.markings_correct, 	variable_card=self.markings_correct_size, 	values=self.markings_correct_values);
		self.distinctive_traits_cpd = TabularCPD(variable=self.distinctive_traits, 	variable_card=self.distinctive_traits_size,	values=self.distinctive_traits_values);
		self.id_using_marking_cpd 	= TabularCPD(variable=self.id_using_marking, 	variable_card=self.id_using_marking_size,	values=self.id_using_marking_values, 		evidence=self.id_using_marking_evidence,		evidence_card=self.id_using_marking_evidence_card);
		self.owner_sta_cpd 			= TabularCPD(variable=self.owner_sta, 			variable_card=self.owner_sta_size, 			values=self.owner_sta_values);
		self.good_id_cpd 			= TabularCPD(variable=self.good_id, 			variable_card=self.good_id_size, 			values=self.good_id_values, 				evidence=self.good_id_evidence, 				evidence_card=self.good_id_evidence_card);
		return True;



	def load_cps(self):
		return self.define_cpds()







	def draw_default_graph(self):
		#define causuality/dependency graph.	
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





	#define set graph
	def draw_graph(self, graph):
		self.horse_id_graph	= graph;
		return True;





	#Build graph and load model: load on start
	def build_model(self):
		#methods							METHOD CLASS 					FIRST ARG
		self.horse_id_model 				= BayesianModel(				self.horse_id_graph);
		self.horse_inference 				= VariableElimination(			self.horse_id_model); 
		return self.add_cpds_to_model();








	#add nodes/CPDs to HorseID model graph: load this on start
	def load_cpds_to_model(self):
		#add cpds to horse model
		self.horse_id_model.add_cpds(
			#SET 1							#SET 2							#SET 3
			self.identifiability_cpd, 		self.location_cpd, 				self.chip_work_cpd, 				
			self.chipped_cpd, 				self.passport_cpd, 				self.passport_available_cpd, 
			self.id_using_cpd, 				self.id_verifying_cpd, 			self.id_using_marking_cpd, 		
			self.markings_correct,			self.distinctive_traits_cpd, 	self.owner_sta_cpd, 			
			self.good_id_cpd);
		return True;





	def load_model():
		#update model
		self.build_model();
		#load cpds to model
		self.load_cpds_to_model();







	# TODO: OBTAIN DATA HERE
	#use this to extract database into dataframe values as required by the model
	def load_data(self, url):

		#	TODO: extract database in dataframe, cross_validate data, and return training dataframe and test dataframe;
		#	all necessary counting processes is done in this function.
		raw_data = url.urlopen(self.url);
		self.dataframe = prepare_data(raw_data);








	#TODO SCRUB DATA HERE
	def prepare_data(self, raw_data):

		#	check the current data format.
		raw_dataframe = pd.Dataframe(raw_data);
		dataframe = pd.Dataframe(columns=[
			#SET 1								SET 2								SET 3
			self.IDENTIFIABILITY, 				self.LOCATION, 						self.CHIP_WORK, 
			self.CHIPPED,		 				self.PASSPORT, 						self.PASSPORT_AVAILABLE, 
			self.ID_USING, 						self.ID_VERIFYING, 					self.ID_USING_MARKING, 
			self.MARKINGS_CORRECT, 				self.DISTINCTIVE_TRAITS, 			self.OWNER_STA, 
			self.GOOD_ID]);
		return dataframe;










	#use this to train model. Takes in pandas dataframe as input to train the model based on define graph as define above
	def train_model(self, dataframe, graph=None):

		# Cross validate dataset
		test_length = 0.1*len(dataframe);
		test_dataframe, dataframe = dataframe[:test_length], dataframe[test_length:];
		self.update_values(dataframe);
		self.load_cpds();
		#draw graph
		if graph == None:
			self.draw_default_graph();
		else:
			self.draw_graph(graph);
		self.load_model();
		self.last_updated_time = "";
		self.current_accuracy 	=	self.test_model(test_dataframe);
		return {time: self.last_updated_time, accuracy: self.current_accuracy}







	#use this to train model online. Takes in pandas dataframe.
	def update_model(self, dataframe, graph=None):

		# Cross validate dataset
		test_length = 0.1*len(dataframe);
		test_dataframe, dataframe = dataframe[:test_length], dataframe[test_length:];
		self.update_values(dataframe);
		self.load_cpds();
		#draw graph
		if graph == None:
			self.draw_default_graph();
		else:
			self.draw_graph(graph);
		self.load_model();
		self.last_updated_time = "";
		self.current_accuracy 	=	self.test_model(test_dataframe);
		return {time: self.last_updated_time, accuracy: self.current_accuracy}








	#use this to test model accuracy. Takes in pandas test dataframe.
	def test_model(self, dataframe):
		# TODO: test model based on dataframe and return test accuracy.
		# self.horse_id_model.query() 	
		return 0;	




	def describe_data(self):
		return self.get_cpds();






	def check_model(self):
		return self.horse_id_model.check_model();







	def get_cpds(self, node=None):
		return self.horse_id_model.get_cpds(node);







	def get_cardinality(self, node=None):
		return self.horse_id_model.get_cardinality(node);







	def get_local_independencies(self):
		return self.horse_id_model.local_independencies();







	def get_active_trail_nodes(self, node, observed=None):
		return self.horse_id_model.active_trail_nodes(node, observed=observed)







	def query(self, nodes):
		return self.horse_inference.query(nodes);







	def map_query(self, nodes, evidence=None):
		return self.horse_inference.map_query(nodes, evidence=evidence);











