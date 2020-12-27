from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
   
    def create_user(self, first_name,last_name,phone_number,email, password, is_staff =False, is_superuser = False , is_active =True,security_access_level = 0):
        
        
        if not email:
            raise ValueError(_('The Email must be set'))


        # email = self.normalize_email(email)
        user = self.model(first_name= first_name, last_name = last_name, phone_number= phone_number,email=email,security_access_level=security_access_level, is_staff= is_staff, is_superuser = is_superuser,is_active =is_active)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name,last_name,phone_number,email, security_access_level, password,is_staff =False, is_superuser = True , is_active =True):
        """
        Create and save a SuperUser with the given email and password.
        """
        is_staff = True
        is_superuser = True
        is_active = True
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(first_name= first_name, last_name = last_name, phone_number= phone_number,email=email,security_access_level=security_access_level, password = password, is_staff= is_staff, is_superuser=is_superuser, is_active= is_active)