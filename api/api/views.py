from functools import partial
from django.shortcuts import render
from itsdangerous import Serializer
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.

# @api_view(['GET'])
# def hello_word(request):
#     return Response({'msg':'hello world'})

# @api_view(['POST'])
# def hello_word(request):
#     if request.method == "POST":
#        print(request.data)
#        return Response({'msg':'hello world post req'})


# @api_view(['GET','POST'])
# def employeeapi(request):
#     if request.method == "GET":
#       return Response({'msg':'hello world Get Method'})

#     if request.method == "POST":
#       print('request.data')
#       return Response({'msg':'hello world Post Method','data':request.data})


@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def employeeapi(request,id=None):
    if request.method == "GET": 
      # id = request.data.get('id')
      if id is not None:
        emp = Employee.objects.get(id=id)
        serialize = EmployeeSerializer(emp)
        return Response(serialize.data)

      emp = Employee.objects.all()
      serialize = EmployeeSerializer(emp, many=True)
      return Response(serialize.data)

    if request.method == "POST":  
      serializer = EmployeeSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Data Created'})
      return Response(Serializer.errors)

    if request.method == "PUT":  
      id = request.data.get('id')
      emp = Employee.objects.get(id=id)
      serializer = EmployeeSerializer(emp, data=request.data,partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Data Updated'})
      return Response(Serializer.errors)

    if request.method == "PATCH":  
      id = request.data.get('id')
      emp = Employee.objects.get(id=id)
      serializer = EmployeeSerializer(emp, data=request.data,partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Partial Data Updated'})
      return Response(Serializer.errors)
    
    if request.method == "DELETE":  
      # id = request.data.get('id')
      emp = Employee.objects.get(id=id)
      emp.delete()
      return Response({'msg':'Data Deleted'})