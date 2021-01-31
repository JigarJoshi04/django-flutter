from django.shortcuts import render
from django.http import JsonResponse
from log_app.models import  LogTreeModel
from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from user_app.models import UserModel
# Create your views here.

@api_view(['GET'])
def user_based_report(request):
    trees = LogTreeModel.objects.values('logged_by_user_id','logged_tree_id').annotate(treecount = Count('logged_tree_id'))
    trees =list(trees)
    print(trees)
    user_list = []
    for i in range(0,len(trees)):
        user =  UserModel.objects.get(id = trees[i]['logged_by_user_id'])
        user_list.append(user)
    user_list = list(set(user_list))
    user_based_report = []
    for i in range(0,len(user_list)):
        user_based_report.append([user_list[i].first_name,0,0])
    

    for i in range(0,len(trees)):
        user_id = trees[i]["logged_by_user_id"]
        user = UserModel.objects.get(id = user_id)
        tree_id = trees[i]["logged_tree_id"]
        tree_count = trees[i]["treecount"]

        for j in range(0,len(user_list)):
            if(user_list[j].first_name == user.first_name):
                break
        if(tree_id == 1):
            user_based_report[j][1] = tree_count
        elif(tree_id ==2):
            user_based_report[j][2] = tree_count
    return JsonResponse({"user_based_report":list(user_based_report)})
   