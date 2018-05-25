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
from .bbn import HorseIDBayesianNetwork;
from .tests import HorseIDBayesianNetworkTest

bbn = HorseIDBayesianNetwork();
bbn_test = HorseIDBayesianNetworkTest();



def createSerializedResponse(response):
		#response = FunctionResponse.objects.all()
		#serializer = FunctionResponseSerializer(response);
		response = {"output": response};
		return Response(response);



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

	

	class build(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.build(request))


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.build())





	class run(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.run(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.run())
		




	class update(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.update(request));


		def put(self, request):
			return createSerializedResponse(bbn.update(request));



		def post(self, request):
			return createSerializedResponse(bbn_test.update())






	class initialise_space(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.initialise_space(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn.initialise_space(request));







	class define_universe(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.define_universe(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.define_universe(request));






	class clear_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.clear_values(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.clear_values(request));





	class use_default_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.use_default_values(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.use_default_values(request));





	class declare_variables(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.declare_variables(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.declare_variables(request));





	#use this to update dataset values for cpds
	class update_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.update_values(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.update_values(request));






	#this declares and initialises the variables sizes to be used
	class load_sizes(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.load_sizes(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.load_sizes(request));





	#define variable dependencies and dependency size(evidence and evidence card)
	class define_evidences(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.define_evidences(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.define_evidences(request));





	#define node cpds: load this on start
	class define_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.define_cpds(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.define_cpds(request));






	class load_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.load_cps(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.load_cps(request));





	class draw_default_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.draw_default_graph(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.draw_default_graph(request));




	#define set graph
	class draw_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.draw_graph(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn.draw_graph(request));




	#Build graph and load model: load on start
	class build_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.build_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.build_model(request));





	#add nodes/CPDs to HorseID model graph: load this on start
	class load_cpds_to_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.load_cpds_to_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.load_cpds_to_model(request));






	class load_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.load_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.load_model(request));
			





	class load_data(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.load_data(request));

		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.load_data());





	class prepare_data(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.prepare_data(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.prepare_data());






	class train_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.train_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.train_model());







	class update_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.update_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.update_model());







	class test_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.test_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.test_model());






	class describe_data(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.describe_data(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.describe_data());







	class check_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.check_model(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.check_model());








	class get_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.get_cpds(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.get_cpds());







	class get_cardinality(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.get_cardinality(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.get_cardinality());







	class get_local_independencies(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.get_local_independencies(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.get_local_independencies());






	class get_active_trail_nodes(APIView):


		def get(self, request):
			return createSerializedResponse(bbn.get_active_trail_nodes(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.get_active_trail_nodes());





	class query(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.query(request));


		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.query());






	class map_query(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.map_query(request));



		def put(self, request):
			pass


		def post(self, request):
			return createSerializedResponse(bbn_test.map_query());



