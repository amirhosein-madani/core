from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser , PermissionsMixin


# post_save   post_delete pre_save pre_delete 



class UserManager(BaseUserManager):
    def create_user(self, email,username,phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
     
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,password ,username , phone_number ,  email = None ,):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email = email,
            password=password,
            username = username,
            phone_number= phone_number
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser , PermissionsMixin):
    """
    custom user model 
    """
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        blank= True,
        null= True,
        unique=True,
    )
    username = models.CharField( max_length=50, unique= True)
   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default=False)
    # is_verified = models.BooleanField()
    phone_number =models.CharField(max_length=12,unique=True)
    created_date = models.DateTimeField( auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True