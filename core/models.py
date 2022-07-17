from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    id_user = models.ImageField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    