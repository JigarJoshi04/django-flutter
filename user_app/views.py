from django.shortcuts import render,HttpResponse
from user_app.models import UserModel
from .serializers import convert_bytes_array_to_json
import requests
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
def create_new_user(request):
    first_name = "test",
    last_name = "002",
    email= "test002@gmail.com",
    phone_number = "893acxa964"
    security_access_level= int(3),
    password ="test002"

    user = UserModel(first_name=first_name,last_name=last_name,phone_number = phone_number,security_access_level =security_access_level,email=email,password=password)
    user.first_name = user.first_name[0]
    user.last_name = user.last_name[0]
    user.security_access_level = user.security_access_level[0]
    user.email = user.email[0]
    user.save()
    print(user.first_name)
    print(user.last_name)
    print(user.phone_number)
    print(user.email)
    print(user.password)
    print(user.security_access_level)
    print("User is saved")
    return HttpResponse("User is saved 200 code")

def login_user(request):
    phone_number = "9579088663"
    password = "jigar"

    users = UserModel.objects.get(phone_number =phone_number)
    print(users.password)
    print(password)
    if users.check_password(password):
        print("Login Success")
        url = 'http://localhost:8000/api/token/'
        data = {"phone_number":phone_number,"password":password}
        print(data)
        response = requests.post(url, data = data)
        response_json = convert_bytes_array_to_json(response.content)
        # print(response_json["access"])
        # authenticated_user =authenticate(phone_number=phone_number,password=password)
        # print(response.status_code)
        # print(response.content)
    else:
        print("Account not found")
    return HttpResponse("User is found 200 code")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_api(request):
    print(str(request.headers["Authorization"])[6:])
    user = Token.objects.get(key=str(request.headers["Authorization"])[6:]).user
    print(user)
    return HttpResponse("Test Successful")