from rest_framework import serializers
from .models import Variables, FunctionResponse


class VariablesSerializer(serializers.ModelSerializer):
	"""docstring for VariableSerializer"""
	
	class Meta:
		model = Variables;
		fields = '__all__';




class FunctionResponseSerializer(serializers.ModelSerializer):
	"""docstring for HorseIDBayesianNetworkSerializer"""

	class Meta:
		model = FunctionResponse;
		fields = '__all__';


