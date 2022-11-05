from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ArithmeticSerializer
from arithmetic_operator.models import Arithmetic
from rest_framework import status
from rest_framework.response import Response
import json




@api_view(['POST'])
def operation(request):
  
    serializer = ArithmeticSerializer(data=request.data, many=False) # catch the post data and assign it to serializer variable
    
    if serializer.is_valid(): # check whether the data is valid
        x = serializer.validated_data['x'] # retrieve the value of x from post data and assign it to x
        y = serializer.validated_data['y'] # retrieve the value of y from post data and assign it to y
        operation_type = serializer.validated_data['operation_type'] # retrieve the value of operation_type from post data and assign it to operation_type
        if operation_type == 'addition':
            result = x + y
        elif operation_type == 'subtraction':
            result = x - y
        elif operation_type == 'multiplication':
            result = x * y
        else:
            return Response("The operation type is not valid")
        
        resposnse_object = {"slackUsername":"Algamawiy", "result":result, 'operation_type':operation_type}
        serializer.save() # save the post data
        return Response(resposnse_object, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)