import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers as djangoSerializer
from django.http import HttpResponse
from . models import *
from . serializers import *
from django.db import connection


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
            userID = output[0].id
            return Response(userID, status=202)
        
class SignupView(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        print(request.data)
        userSignupSerializer = UserSignupSerializer(data=request.data)
        if userSignupSerializer.is_valid(raise_exception=True):
            userSignupSerializer.save()
            return Response("User Created", status=200)
        else:
            return Response("Invalid Parameter Names (ex: first_name, last_name, email , password)", status=403)

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
        
class UserProfileView(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        jsonData = request.data
        print(jsonData)
        userID = int(jsonData["userID"])
        output = Users.objects.filter(id=userID)
        jsonOutput = djangoSerializer.serialize('json', output)
        jsonOutput = json.loads(jsonOutput)
        return Response(jsonOutput, status=200)
    
class UpdateUserProfile(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        jsonData = request.data
        userID = int(jsonData["userID"])
        if "delete" in jsonData:
            userID = jsonData["userID"]
            Users.objects.get(id=userID).delete()
            return Response("User Deleted", status=200)
        elif "update" in jsonData:
            user = Users.objects.get(id=userID)
            if "first_name" in jsonData:
                user.first_name=jsonData["first_name"]
            if "last_name" in jsonData:
                user.last_name=jsonData["last_name"]
            if "email" in jsonData:
                user.email=jsonData["email"]
            if "password" in jsonData:
                user.password=jsonData["password"]
            user.save()
            return Response("User Profile Updated", status=200)
        else:
            return Response()
        
class UserPlants(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)
    
    def post(self, request):
        jsonData = request.data
        userID = jsonData["userID"]
        userPlants = personalPlant.objects.filter(user__id__contains=userID)
        jsonData = {}
        num = 1
        for plant in userPlants:
            # userPlantsList.append(libraryPlant.objects.get(id=plant.plantID))
            if plant.plantID:
                jsonData[num] = {"plantID": plant.plantID.id,
                                 "name": plant.plantID.name,
                                 "size": plant.plantID.size,
                                 "description": plant.plantID.description,
                                 "inside": plant.plantID.inside,
                                 "water": plant.plantID.water,
                                 "sun": plant.plantID.sun,
                                 "fertilization": plant.plantID.fertilization,
                                 "soil": plant.plantID.soil,
                                 "pet": plant.plantID.pet
                                 }
                num += 1
        return Response(jsonData, status=200)
    

class UpdateUserPlants(APIView):
    def get(self, request):
        return Response("no GET method logic, but working fine", status=200)

    def post(self, request):
        jsonData = request.data
        userID = jsonData["userID"]
        plantID = jsonData["plantID"]
        alive = jsonData["alive"] # should be an interger (1 = alive, 0 = not alive)
        if "delete" in jsonData:
            if jsonData["delete"].lower() == "true":
                query = f"""DELETE FROM base_personalplant WHERE rowid = (SELECT rowid FROM base_personalplant WHERE user_id={userID} AND plantID_id={plantID} AND alive={alive} LIMIT 1);"""

                with connection.cursor() as cursor:
                    cursor.execute(query)

                return Response("User Deleted", status=200)
            else:
                return Response("Nothing Happened", status=200)
        elif "update" in jsonData:
            plant = personalPlant.objects.filter(user_id=userID, plantID_id=plantID, alive=alive)

            if plant:
                if int(alive) == 1:
                    query = f"""UPDATE base_personalplant SET alive=0 WHERE rowid = (SELECT rowid FROM base_personalplant WHERE user_id={userID} AND plantID_id={plantID} AND alive={alive} LIMIT 1);"""
                else:
                    query = f"""UPDATE base_personalplant SET alive=1 WHERE rowid = (SELECT rowid FROM base_personalplant WHERE user_id={userID} AND plantID_id={plantID} AND alive={alive} LIMIT 1);"""

                with connection.cursor() as cursor:
                    cursor.execute(query)
                return Response("Plant Updated", status=200)
            else:
                return Response("Plant Not Found")


#class UpdatePlantView(APIView):
