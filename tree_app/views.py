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
from .models import TreeModel
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_tree(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    tree_name = body["tree_name"]
    tree_scientific_name = body["tree_scientific_name"]
    tree_preciousness= int(body["tree_preciousness"])
    
    user_phone_number = Token.objects.get(key=str(request.headers["Authorization"])[6:]).user
    user_who_added_tree = UserModel.objects.get(phone_number= user_phone_number)  
    added_by_user = user_who_added_tree
    
    tree= TreeModel(tree_name =tree_name, tree_scientific_name= tree_scientific_name, tree_preciousness = tree_preciousness,added_by_user = added_by_user)
    tree.save()
    return HttpResponse("Tree addition successful")