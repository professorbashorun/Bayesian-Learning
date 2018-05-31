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






def createSerializedResponse(function, data):
	try:
		return Response({"output": function(data)});
	except Exception as e:
		return Response({"output": e}, status=status.HTTP_400_BAD_REQUEST)








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
	"""
	The General Format for API Use:

		GET:	calls the void unit testing on the function
		POST:	calls unit testing on function with request.data as the testing data
		PUT:	calls the function with request.data as the input variable to the function

	"""



	class start(APIView):

		def put(self, request):
			return createSerializedResponse(bbn.start, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.start,	request.data)
			

		def get(self, request):
			return createSerializedResponse(bbn_test.start, None)




	class build(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.build,	None)


		def put(self, request):
			return createSerializedResponse(bbn.build,	request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.build,	request.data)





	class run(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.run, None);


		def put(self, request):
			return createSerializedResponse(bbn.run,request.data);



		def post(self, request):
			return createSerializedResponse(bbn_test.run, request.data)
		




	class update(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.update, None);


		def put(self, request):
			return createSerializedResponse(bbn.update, request.data);



		def post(self, request):
			return createSerializedResponse(bbn_test.update, request.data)






	class initialise_space(APIView):


		def get(self, request):
			return createSerializedResponse(bbn_test.initialise_space, None);


		def put(self, request):
			return createSerializedResponse(bbn.initialise_space, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.initialise_space, request.data);







	class set_universe(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.set_universe, None);



		def put(self, request):
			return createSerializedResponse(bbn.set_universe, request.data);



		def post(self, request):
			return createSerializedResponse(bbn_test.set_universe, request.data);






	class clear_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.clear_values, None);


		def put(self, request):
			return createSerializedResponse(bbn.clear_values, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.clear_values, request.data);







	class use_default_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.use_default_values, None);


		def put(self, request):
			return createSerializedResponse(bbn.use_default_values, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.use_default_values, request.data);







	class declare_variables(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.declare_variables, None);


		def put(self, request):
			return createSerializedResponse(bbn.declare_variables, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.declare_variables, request.data);







	class update_values(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.update_values, None)


		def put(self, request):
			return createSerializedResponse(bbn.update_values, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.update_values, request.data)







	class load_sizes(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_sizes, None);


		def put(self, request):
			return createSerializedResponse(bbn.load_sizes,request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.load_sizes, request.data)







	class set_evidences(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.set_evidences, None)


		def put(self, request):
			return createSerializedResponse(bbn.set_evidences, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.set_evidences, request.data)



	class load_evidences(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_evidences, None);


		def put(self, request):
			return createSerializedResponse(bbn.load_evidences, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.load_evidences, request.data)






	class set_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.set_cpds, None);


		def put(self, request):
			return createSerializedResponse(bbn.set_cpds, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.set_cpds, request.data)







	class load_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_cpds, None);


		def put(self, request):
			return createSerializedResponse(bbn.load_cpds, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.load_cpds, request.data)







	class draw_default_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.draw_default_graph, None);


		def put(self, request):
			return createSerializedResponse(bbn.draw_default_graph, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.draw_default_graph, request.data)



	class load_default_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_default_graph, None);


		def put(self, request):
			return createSerializedResponse(bbn.load_default_graph, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.load_default_graph, request.data);







	class load_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_graph, None);


		def put(self, request):
			return createSerializedResponse(bbn.load_graph, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.load_graph, request.data);









	class draw_graph(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.draw_graph, None)


		def put(self, request):
			return createSerializedResponse(bbn.draw_graph, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.draw_graph, request.data)








	class build_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.build_model, None);


		def put(self, request):
			return createSerializedResponse(bbn.build_model, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.build_model, request.data)










	class load_cpds_to_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_cpds_to_model, None)


		def put(self, request):
			return createSerializedResponse(bbn.load_cpds_to_model, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.load_cpds_to_model, request.data)










	class load_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.load_model, None);


		def put(self, request):
			return createSerializedResponse(bbn.load_model, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.load_model, request.data)










	class train_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.train_model, None)


		def put(self, request):
			return createSerializedResponse(bbn.train_model, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.train_model, request.data)












	class update_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn.update_model, None);


		def put(self, request):
			return createSerializedResponse(bbn.update_model, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.update_model, request.data)







	class test_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.test_model, None)


		def put(self, request):
			return createSerializedResponse(bbn.test_model, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.test_model, request.data)










	class describe_node(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.describe_node, None);


		def put(self, request):
			return createSerializedResponse(bbn.describe_node, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.describe_node, request.data)











	class check_model(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.check_model, None);


		def put(self, request):
			return createSerializedResponse(bbn.check_model, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.check_model, request.data)




	class get_nodes(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_nodes, None);


		def put(self, request):
			return createSerializedResponse(bbn.get_nodes, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.get_nodes, request.data)






	class get_edges(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_edges, None);


		def put(self, request):
			return createSerializedResponse(bbn.get_edges, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.get_edges, request.data)







	class get_cpds(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_cpds, None);


		def put(self, request):
			return createSerializedResponse(bbn.get_cpds, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.get_cpds, request.data)










	class get_cardinality(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_cardinality, None);


		def put(self, request):
			return createSerializedResponse(bbn.get_cardinality, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.get_cardinality, request.data)










	class get_local_independencies(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.get_local_independencies, None)


		def put(self, request):
			return createSerializedResponse(bbn.get_local_independencies, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.get_local_independencies, request.data)










	class get_active_trail_nodes(APIView):


		def get(self, request):
			return createSerializedResponse(bbn_test.get_active_trail_nodes, None);


		def put(self, request):
			return createSerializedResponse(bbn.get_active_trail_nodes, request.data)


		def post(self, request):
			return createSerializedResponse(bbn_test.get_active_trail_nodes, request.data)











	class query(APIView):

		def post(self, request):
			return createSerializedResponse(bbn_test.query,	None);


		def put(self, request):
			return createSerializedResponse(bbn.query, request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.query,	request.data);












	class map_query(APIView):


		def get(self, request):
			return createSerializedResponse(bbn_test.map_query,	None);


		def put(self, request):
			return createSerializedResponse(bbn.map_query,	request.data);


		def post(self, request):
			return createSerializedResponse(bbn_test.map_query,	request.data);







	class test_all(APIView):

		def get(self, request):
			return createSerializedResponse(bbn_test.test_all,	None);


		def post(self, request):
			return createSerializedResponse(bbn_test.test_all,	request.data);



