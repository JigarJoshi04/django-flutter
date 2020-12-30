from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
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
from .models import LogTreeModel
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