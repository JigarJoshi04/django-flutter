from django.db import models
from user_app.models import UserModel
from tree_app.models import TreeModel

class LogTreeModel(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank= False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank= False)
    pin_code = models.IntegerField(blank= False)
    tree_girth = models.IntegerField()
    time_of_logging = models.DateTimeField(blank= False)

    logged_by_user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    logged_tree = models.ForeignKey(TreeModel,on_delete= models.CASCADE)

    class Meta:
        verbose_name = "Log Tree Model"
        
    # [self.first_name,self.last_name,self.is_active,self.is_staff,self.is_superuser,self.email,self.security_access_level,self.password]
    def __str__(self):
        return self.pin_code