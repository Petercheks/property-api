from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password):

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user
        

class Rol(models.Model):

    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True) 
    

class User(AbstractBaseUser, PermissionsMixin):
    
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)    
    email = models.EmailField(max_length=155, unique=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.firstname + self.lastname

    