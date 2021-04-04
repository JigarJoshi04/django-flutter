from django.shortcuts import render, HttpResponse
from log_app.models import LogTreeModel
from user_app.models import UserModel
from tree_app.models import TreeModel
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_new_log(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    tree_name = body["tree_name"]
    latitude = body["latitude"]
    longitude = body["longitude"]
    pin_code = body["pin_code"]
    tree_girth = body["tree_girth"]
    time_of_logging = body["time_of_logging"]

    user_phone_number = Token.objects.get(key=str(request.headers["Authorization"])[6:]).user
    logged_by_user = UserModel.objects.get(phone_number=user_phone_number)
    logged_tree = TreeModel.objects.filter(tree_name=body["tree_name"]).first()
    loggedtree = LogTreeModel(
        latitude=latitude,
        longitude=longitude,
        pin_code=pin_code,
        tree_girth=tree_girth,
        time_of_logging=time_of_logging,
        logged_by_user=logged_by_user,
        logged_tree=logged_tree,
    )
    loggedtree.save()

    return HttpResponse("Tree addition successful")


def get_all_trees():
    trees = LogTreeModel.objects.all()
    return trees


def get_trees_of_user(phone_number):
    trees = LogTreeModel.objects.filter(logged_by_user=phone_number)
    return trees


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_trees_location(request):
    user_phone_number = Token.objects.get(key=str(request.headers["Authorization"])[6:]).user
    user = UserModel.objects.get(phone_number=user_phone_number)

    if user.security_access_level == 5:
        all_trees = get_all_trees()

    elif user.security_access_level == 3:
        all_trees = get_all_trees()
        # return al trees for now

    else:
        all_trees = get_trees_of_user(user)

    # all_trees = get_all_trees()
    trees_list = []
    for i in range(0, len(all_trees)):
        log = LogTreeModel.objects.get(log_id=all_trees[i])
        trees_list.append([log.latitude, log.longitude, str(log.logged_tree)])
    print(trees_list)

    return JsonResponse({"trees_list": trees_list})
    # return HttpResponse("Test Successful")