from django.db import models

from datetime import datetime

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=500)

