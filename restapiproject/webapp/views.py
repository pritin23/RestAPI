from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeeSerializer
# Create your views here

class employeeList(APIView):
    def get(self,request):
        employee  = employees.objects.all()
        serializer = employeeSerializer(employee, many=True)
        return Response(serializer.data)
    def post(self):
        pass
