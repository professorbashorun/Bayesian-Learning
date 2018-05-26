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


	def put(self):
		pass



	def post(self):
		pass








class HorseIDBayesianNetworkAPI(object):

	

	class build(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.build())


		def put(self, request):
			return createSerializedResponse(bbn.build(request.data))


		def post(self, request):
			return createSerializedResponse(bbn_test.build(request.data))





	class run(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.run());


		def put(self, request):
			return createSerializedResponse(bbn.run(request.data));



		def post(self, request):
			return createSerializedResponse(bbn_test.run(request.data))
		




	class update(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.update());


		def put(self, request):
			return createSerializedResponse(bbn.update(request.data));



		def post(self, request):
			return createSerializedResponse(bbn_test.update(request.data))






	class initialise_space(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.initialise_space());


		def put(self, request):
			return createSerializedResponse(bbn.initialise_space(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.initialise_space(request.data));







	class define_universe(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.define_universe());



		def put(self, request):
			return createSerializedResponse(bbn.define_universe(request.data));



		def post(self, request):
			return createSerializedResponse(bbn_test.define_universe(request.data));






	class clear_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.clear_values());


		def put(self, request):
			return createSerializedResponse(bbn.clear_values(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.clear_values(request.data));





	class use_default_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.use_default_values());


		def put(self, request):
			return createSerializedResponse(bbn.use_default_values(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.use_default_values(request.data));





	class declare_variables(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.declare_variables());


		def put(self, request):
			return createSerializedResponse(bbn.declare_variables(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.declare_variables(request.data));





	#use this to update dataset values for cpds
	class update_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.update_values());


		def put(self, request):
			return createSerializedResponse(bbn.update_values(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.update_values(request.data));






	#this declares and initialises the variables sizes to be used
	class load_sizes(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_sizes());


		def put(self, request):
			return createSerializedResponse(bbn.load_sizes(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.load_sizes(request.data));





	#define variable dependencies and dependency size(evidence and evidence card)
	class define_evidences(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.define_evidences());


		def put(self, request):
			return createSerializedResponse(bbn.define_evidences(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.define_evidences(request.data));





	#define node cpds: load this on start
	class define_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.define_cpds());


		def put(self, request):
			return createSerializedResponse(bbn.define_cpds(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.define_cpds(request.data));






	class load_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_cps());


		def put(self, request):
			return createSerializedResponse(bbn.load_cps(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.load_cps(request.data));





	class draw_default_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.draw_default_graph());


		def put(self, request):
			return createSerializedResponse(bbn.draw_default_graph(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.draw_default_graph(request.data));




	#define set graph
	class draw_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.draw_graph());


		def put(self, request):
			return createSerializedResponse(bbn.draw_graph(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.draw_graph(request.data));




	#Build graph and load model: load on start
	class build_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.build_model());


		def put(self, request):
			return createSerializedResponse(bbn.build_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.build_model(request.data));





	#add nodes/CPDs to HorseID model graph: load this on start
	class load_cpds_to_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_cpds_to_model());


		def put(self, request):
			return createSerializedResponse(bbn.load_cpds_to_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.load_cpds_to_model(request.data));






	class load_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_model());


		def put(self, request):
			return createSerializedResponse(bbn.load_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.load_model(request.data));
			





	class load_data(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_data());

		def put(self, request):
			return createSerializedResponse(bbn.load_data(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.load_data(request.data));





	class prepare_data(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.prepare_data());


		def put(self, request):
			return createSerializedResponse(bbn.prepare_data(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.prepare_data(request.data));






	class train_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.train_model());


		def put(self, request):
			return createSerializedResponse(bbn.train_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.train_model(request.data));







	class update_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.update_model());


		def put(self, request):
			return createSerializedResponse(bbn.update_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.update_model(request.data));







	class test_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.test_model());


		def put(self, request):
			return createSerializedResponse(bbn.test_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.test_model(request.data));






	class describe_data(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.describe_data());


		def put(self, request):
			return createSerializedResponse(bbn.describe_data(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.describe_data(request.data));







	class check_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.check_model());


		def put(self, request):
			return createSerializedResponse(bbn.check_model(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.check_model(request.data));








	class get_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_cpds());


		def put(self, request):
			return createSerializedResponse(bbn.get_cpds(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.get_cpds(request.data));







	class get_cardinality(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_cardinality());


		def put(self, request):
			return createSerializedResponse(bbn.get_cardinality(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.get_cardinality(request.data));







	class get_local_independencies(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_local_independencies());


		def put(self, request):
			return createSerializedResponse(bbn.get_local_independencies(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.get_local_independencies(request.data));






	class get_active_trail_nodes(APIView):


		def get(self, request):
			return createSerializedResponse(bbn_test.get_active_trail_nodes());


		def put(self, request):
			return createSerializedResponse(bbn.get_active_trail_nodes(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.get_active_trail_nodes(request.data));







	class query(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.query());


		def put(self, request):
			return createSerializedResponse(bbn.query(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.query(request.data));








	class map_query(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.map_query());



		def put(self, request):
			return createSerializedResponse(bbn.map_query(request.data));


		def post(self, request):
			return createSerializedResponse(bbn_test.map_query(request.data));



