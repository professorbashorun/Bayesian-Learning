# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Variables
from .models import FunctionResponse
from .serializer import VariablesSerializer
from .serializer import FunctionResponseSerializer
import bbn





# variables/
class VariablesList(APIView):
	"""docstring for Variables View"""
	
	def get(self, request):
		variables = Variables.objects.all();
		serializer = VariablesSerializer(variables, many=True);
		return Response(serializer.data);


	def post(self):
		pass 





class HorseIDBayesianNetworkAPI(object):



	def createSerializedResponse(self, response):
		response = FunctionResponse.objects.all()
		serializer = FunctionResponseSerializer(response);
		return Response(serializer.data);





	class build(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.build());





	class run(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.run());
		




	class update(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.update());




	class initialise_space(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.initialise_space());





	class define_universe(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.define_universe());







	class clear_values(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.clear_values());




	class use_default_values(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.use_default_values());




	class declare_variables(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.declare_variables());





	#use this to update dataset values for cpds
	class update_values(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.update_values());






	#this declares and initialises the variables sizes to be used
	class load_sizes(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.load_sizes());





	#define variable dependencies and dependency size(evidence and evidence card)
	class define_evidences(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.define_evidences());





	#define node cpds: load this on start
	class define_cpds(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.define_cpds());




	class load_cps(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.load_cps());





	class draw_default_graph(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.draw_default_graph());





	#define set graph
	class draw_graph(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.draw_graph());





	#Build graph and load model: load on start
	class build_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.build_model());






	#add nodes/CPDs to HorseID model graph: load this on start
	class load_cpds_to_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.load_cpds_to_model());





	class load_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.load_model());





	class load_data(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.load_data());





	class prepare_data(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.prepare_data());






	class train_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.train_model());






	class update_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.update_model());





	class test_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.test_model());




	class describe_data(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.describe_data());






	class check_model(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.check_model());







	class get_cpds(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.get_cpds());







	class get_cardinality(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.get_cardinality());







	class get_local_independencies(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.get_local_independencies());







	class get_active_trail_nodes(APIView):


		def get(self, response):
			return createSerializedResponse(bbn.get_active_trail_nodes());







	class query(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.query());







	class map_query(APIView):

		def get(self, response):
			return createSerializedResponse(bbn.map_query());
