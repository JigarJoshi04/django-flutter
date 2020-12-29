from django.db import models
from user_app.models import UserModel

class TreeModel(models.Model):
    tree_name = models.CharField(max_length=500,blank= False, unique= True)
    tree_scientific_name = models.CharField(max_length=500,blank=True)
    tree_preciousness = models.IntegerField(default=0)
    added_by_user = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tree Model"
        
    # [self.first_name,self.last_name,self.is_active,self.is_staff,self.is_superuser,self.email,self.security_access_level,self.password]
    def __str__(self):
        return self.tree_name