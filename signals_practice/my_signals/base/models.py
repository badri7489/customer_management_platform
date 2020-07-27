from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name

def create_profile():
    '''
        if created:
            Profile.objects.create(user=instance)
            print('Profile Created!!')
    '''

def update_profile():
    '''
        if created == False:
            print()
            try:
                instance.profile.save()
                print("Profile Update!!")
            except:
                Profile.objects.create(user=instance)
                print('Profile created for existing user!!')

    '''
    