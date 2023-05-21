from django.db import models

# Create your models here.

# Course(id, code, name)

class Course(models.Model):
    code = models.CharField(max_length=7)
    title = models.CharField(max_length=50)
    description = models.TextField()