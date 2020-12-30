from django.shortcuts import render,HttpResponse
from log_app.models import LogTreeModel
from user_app.models import UserModel

import requests
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import json
# Create your views here.
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_log(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    latitude = body["latitude"]
    longitude = body["longitude"]
    pin_code = body["pin_code"]
    tree_girth = body["tree_girth"]
    time_of_logging = body["time_of_logging"]

    user_phone_number = Token.objects.get(key=str(request.headers["Authorization"])[6:]).user
    logged_by_user = UserModel.objects.get(phone_number= user_phone_number)  
    logged_tree = TreeModel.objects.get(tree_name = body["tree_name"])
    # tree= TreeModel(tree_name =tree_name, tree_scientific_name= tree_scientific_name, tree_preciousness = tree_preciousness,added_by_user = added_by_user)
    # tree.save()

    return HttpResponse("Tree addition successful")


def get_all_trees():
    trees = LogTreeModel.objects.all()
    return trees

def get_trees_of_user(phone_number):
    trees = LogTreeModel.objects.filter(logged_by_user = phone_number)
    return trees

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_trees_location(request):
    user_phone_number = Token.objects.get(key=str(request.headers["Authorization"])[6:]).user
    user = UserModel.objects.get(phone_number = user_phone_number)

    # if(user.security_access_level == 5):
    #     all_trees = get_all_trees()
    #     return all_trees
        #return all trees
    
    # elif(user.security_access_level == 3):
    #     all_trees = get_all_trees()
    #     return all_trees
    #     # return al trees for now
    
    # else:
    #     trees_of_that_user = get_trees_of_user(user)
    #     return trees_of_that_user
        #return trees of that worker only
    
    # all_trees = get_all_trees()
    all_trees = get_trees_of_user(user)
    for i in range(0,len(all_trees)):
        print("Yhis is me")
        print(all_trees[i])
        log = LogTreeModel.objects.get(log_id = all_trees[i])
        print(log.latitude, log.longitude)
    print(all_trees)
    
    # return all_trees
    return HttpResponse("Test Successful")