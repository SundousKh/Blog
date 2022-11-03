#from django.db import models

# Create your models here.
from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()