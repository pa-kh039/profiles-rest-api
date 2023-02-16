from django.db import models
# the below are standard base classes that you need to use
# to override/customise the default django user models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    '''Manager for user profiles'''
    def create_user(self,email,name,password=None):
        '''create a new user profile'''
        if not email:
            raise ValueError('User must have a email address')
        email=self.normalize_email(email) #this is done to make the second half of email (after @) case insensitive
        user=self.model(email=email, name=name)
        user.set_password(password)  #we pass password like this and not as text like in above line bcoz this hashes the password and then stores it into database and gives security
        user.save(using=self._db) #here we save the user in the databse, we can mention what database this user has to be saved in[inside ()], this is specially useful when we are handling multiple databases
        return user
    
    def create_superuser(self,email,name,password):
        '''create and save a new superuser with given details'''
        user=self.create_user(email,name,password)
        user.is_superuser=True #this attribute is already there in permissionsmixin
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Database model for users iin the system'''
    email=models.EmailField(max_length=255,unique=True)
    is_active= models.BooleanField(default=True) #helpful in activating/deactivating a user
    name=models.CharField(max_length=255)
    is_staff=models.BooleanField(default=False) #bcoz staff users will have some special permissions

    objects=UserProfileManager()

    USERNAME_FIELD='email' #replaced the default username field with the email field
    REQUIRED_FIELDS=['name'] #username field was required by default, we just added the name field also in the list of required fields

    # these functions will be used by django to interact with our custom user model
    # writing them so that we can integrate our custom model with other django cmponents, though we dont really have a separate short name
    def get_full_name(self):
        '''retrieve full name of user'''
        return self.name
    
    def get_short_name(self):
        '''retrieve short name of user'''
        return self.name
    
    def __str__(self):
        '''strign representation of our user'''
        return self.email #now u will see email representing objects instaed of hexadecimal addresses

