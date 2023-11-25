from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    

class Recipe(models.Model):
    id =  models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='recipe_photos/', null=True, blank=True)