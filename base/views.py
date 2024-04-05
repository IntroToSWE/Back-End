import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers as djangoSerializer
from django.http import HttpResponse
from . models import *
from . serializers import *


class Loginview(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)
        # return Response(request.GET.get("email"), status=200)

    def post(self, request):
        jsonData = request.data
        email = jsonData["email"]
        password = jsonData["password"]
        output = Users.objects.filter(email=email, password=password)
        if not output:
            print("empty, no account found")
            return Response("No User Found", status=403)
        else:
            print("not empty")
            return Response("User Found", status=202)
        
class SignupView(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        print(request.data)
        userSignupSerializer = UserSignupSerializer(data=request.data)
        if userSignupSerializer.is_valid(raise_exception=True):
            userSignupSerializer.save()
            return Response("User Created", status=200)

class HomeView(APIView):
    def get(self, request):
        return Response()
    
    def post(self, request):
        return Response()
    
class PlantLibraryView(APIView):
    def get(self, request):
        output = libraryPlant.objects.all()
        jsonOutput = djangoSerializer.serialize('json', output)
        jsonOutput = json.loads(jsonOutput)
        return Response(jsonOutput)
        # return HTTPResponse(jsonOutput, content_type="text/json-comment-filtered") # might use this instead ???
    
    def post(self, request):
        return Response()

class CreatePlantView(APIView):
    def get(self, request):
        return Response()

    # to create new plant
    def post(self, request):
        plant_data = request.data
        print(plant_data)
        plant_serializer = PlantSerializer(data=plant_data)
        if plant_serializer.is_valid(raise_exception=True):
            plant_serializer.save()
            return Response("Plant created successfully", status=201)

#class UpdatePlantView(APIView):
