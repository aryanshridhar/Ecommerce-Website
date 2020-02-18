from django.db import models
from django.contrib.auth.models import User
import os 

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg' , upload_to='Ecommerce/images')

    def __str__(self):
        return self.user.username

    def filename(self):
        return os.path.basename(self.image.name)


    