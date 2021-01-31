# from django.db import models

# # Create your models here.
# from django.db import models
# from user_app.models import UserModel
# from tree_app.models import TreeModel
# from uuid import uuid4

# class ReportModel(models.Model):
#     user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
#     tree_name = models.ForeignKey(TreeModel,on_delete= models.CASCADE)
#     tree_count = models.IntegerField()
    
#     class Meta:
#         verbose_name = "Log Tree Model"
        
#     def __str__(self):
#         return str(self.log_id)