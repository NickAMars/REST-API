from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileMangager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile objec."""
        if not email: # check if email doesnt exist
            raise ValueError("Users must have an email address.")
        email = self.normalize_email(email) #converts the characters to lower case
        user = self.model(email=email, name=name) # create a new user profile model

        user.set_password(password) # encript the password for us
        #save user in the same database in the userprofileMangager
        user.save(using=self._db)

        return user
    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileMangager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""
        return self.name

    def get_short_name(self):
        """Used to get a users short name."""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email
class ProfileFeedItem(models.Model):
    """Profile status update."""
    #connecting the feild to the userProfile
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    #Our feed fields
    status_text = models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    #python knows how to convert or model 
    def __str__(self):
        """Return the model as a string."""
        return self.status_text
