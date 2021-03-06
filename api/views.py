# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Variables
from .models import FunctionResponse
from .serializer import VariablesSerializer
from .serializer import FunctionResponseSerializer
from .bbn import HorseIDBayesianNetwork;
from .tests import HorseIDBayesianNetworkTest
import json

bbn = HorseIDBayesianNetwork();


bbn_test = HorseIDBayesianNetworkTest();


def createSerializedResponse(function, data):
    try:
        return Response({"output": function(json.loads(data.decode('UTF-8')))});
    except Exception as e:
        return Response({"output": e}, status=status.HTTP_400_BAD_REQUEST)


class VariablesList(APIView):
    """Return a json list of variables and their values"""

    def get(self, request):

        variables = bbn.variable_values()
        return JsonResponse(variables)

class NetworkData(APIView):

    def get(self, request):

        # if calling independantly, will need to start bbn
        if bbn.start_time == None:
            bbn.start()

        nodes = bbn.get_nodes()
        edges = bbn.get_edges()
        data = {'nodes':[{"id": n, "group": 1} for n in nodes],
                'links': [ {"source": e[0], "target": e[1], "value": 1} for e in edges],
                }

        return JsonResponse(data)

class ViewNetwork(TemplateView):
    template_name = "chart.html"

class UpdateAndQuery(APIView):
    """Update with new evidence and return updated results"""

    def post(self, request):
        variables = request.data['variables']
        evidence = request.data['evidences']

        bbn.set_cpds({"variables": variables, "evidence": evidence})
        bbn.run(request)

        result = bbn.query({"variables": variables, "evidence": evidence})

        return JsonResponse(result)

class IsStarted(APIView):
    """Check to see if system has been started"""

    def get(self, request):
        result =  (bbn.start_time != None)
        return JsonResponse({'is_started': str(result)})


class HorseIDBayesianNetworkAPI(object):
    """
    The General Format for API Use:

        GET:	calls the void unit testing on the function
        POST:	calls unit testing on function with request.body as the testing data
        PUT:	calls the function with request.body as the input variable to the function

    """
    class start(APIView):

        def put(self, request):
            return createSerializedResponse(bbn.start, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.start, request.body)

        def get(self, request):
            return createSerializedResponse(bbn_test.start, None)

    class build(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.build, None)

        def put(self, request):
            return createSerializedResponse(bbn.build, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.build, request.body)

    class run(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.run, None);

        def put(self, request):
            return createSerializedResponse(bbn.run, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.run, request.body)

    class update(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.update, None);

        def put(self, request):
            return createSerializedResponse(bbn.update, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.update, request.body)

    class initialise_space(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.initialise_space, None);

        def put(self, request):
            return createSerializedResponse(bbn.initialise_space, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.initialise_space, request.body);

    class set_universe(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.set_universe, None);

        def put(self, request):
            return createSerializedResponse(bbn.set_universe, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.set_universe, request.body);

    class clear_values(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.clear_values, None);

        def put(self, request):
            return createSerializedResponse(bbn.clear_values, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.clear_values, request.body);

    class use_default_values(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.use_default_values, None);

        def put(self, request):
            return createSerializedResponse(bbn.use_default_values, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.use_default_values, request.body);

    class declare_variables(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.declare_variables, None);

        def put(self, request):
            return createSerializedResponse(bbn.declare_variables, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.declare_variables, request.body);

    class update_values(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.update_values, None)

        def put(self, request):
            return createSerializedResponse(bbn.update_values, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.update_values, request.body)

    class load_sizes(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_sizes, None);

        def put(self, request):
            return createSerializedResponse(bbn.load_sizes, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.load_sizes, request.body)

    class set_evidences(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.set_evidences, None)

        def put(self, request):
            return createSerializedResponse(bbn.set_evidences, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.set_evidences, request.body)

    class load_evidences(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_evidences, None);

        def put(self, request):
            return createSerializedResponse(bbn.load_evidences, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.load_evidences, request.body)

    class set_cpds(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.set_cpds, None);

        def put(self, request):
            return createSerializedResponse(bbn.set_cpds, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.set_cpds, request.body)

    class load_cpds(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_cpds, None);

        def put(self, request):
            return createSerializedResponse(bbn.load_cpds, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.load_cpds, request.body)

    class draw_default_graph(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.draw_default_graph, None);

        def put(self, request):
            return createSerializedResponse(bbn.draw_default_graph, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.draw_default_graph, request.body)

    class load_default_graph(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_default_graph, None);

        def put(self, request):
            return createSerializedResponse(bbn.load_default_graph, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.load_default_graph, request.body);

    class load_graph(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_graph, None);

        def put(self, request):
            return createSerializedResponse(bbn.load_graph, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.load_graph, request.body);

    class draw_graph(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.draw_graph, None)

        def put(self, request):
            return createSerializedResponse(bbn.draw_graph, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.draw_graph, request.body)

    class build_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.build_model, None);

        def put(self, request):
            return createSerializedResponse(bbn.build_model, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.build_model, request.body)

    class load_cpds_to_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_cpds_to_model, None)

        def put(self, request):
            return createSerializedResponse(bbn.load_cpds_to_model, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.load_cpds_to_model, request.body)

    class load_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.load_model, None);

        def put(self, request):
            return createSerializedResponse(bbn.load_model, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.load_model, request.body)

    class train_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn.train_model, None)

        def put(self, request):
            return createSerializedResponse(bbn.train_model, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.train_model, request.body)

    class update_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn.update_model, None);

        def put(self, request):
            return createSerializedResponse(bbn.update_model, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.update_model, request.body)

    class test_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.test_model, None)

        def put(self, request):
            return createSerializedResponse(bbn.test_model, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.test_model, request.body)

    class describe_node(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.describe_node, None);

        def put(self, request):
            return createSerializedResponse(bbn.describe_node, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.describe_node, request.body)

    class check_model(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.check_model, None);

        def put(self, request):
            return createSerializedResponse(bbn.check_model, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.check_model, request.body)

    class get_nodes(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.get_nodes, None);

        def put(self, request):
            return createSerializedResponse(bbn.get_nodes, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.get_nodes, request.body)

    class get_edges(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.get_edges, None);

        def put(self, request):
            return createSerializedResponse(bbn.get_edges, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.get_edges, request.body)

    class get_cpds(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.get_cpds, None);

        def put(self, request):
            return createSerializedResponse(bbn.get_cpds, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.get_cpds, request.body)

    class get_cardinality(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.get_cardinality, None);

        def put(self, request):
            return createSerializedResponse(bbn.get_cardinality, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.get_cardinality, request.body)

    class get_local_independencies(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.get_local_independencies, None)

        def put(self, request):
            return createSerializedResponse(bbn.get_local_independencies, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.get_local_independencies, request.body)

    class get_active_trail_nodes(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.get_active_trail_nodes, None);

        def put(self, request):
            return createSerializedResponse(bbn.get_active_trail_nodes, request.body)

        def post(self, request):
            return createSerializedResponse(bbn_test.get_active_trail_nodes, request.body)

    class query(APIView):

        def post(self, request):
            return createSerializedResponse(bbn_test.query, None);

        def put(self, request):
            return createSerializedResponse(bbn.query, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.query, request.body);

    class map_query(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.map_query, None);

        def put(self, request):
            return createSerializedResponse(bbn.map_query, request.body);

        def post(self, request):
            return createSerializedResponse(bbn_test.map_query, request.body);

    class test_all(APIView):

        def get(self, request):
            return createSerializedResponse(bbn_test.test_all, None);

        def post(self, request):
            return createSerializedResponse(bbn_test.test_all, request.body);
