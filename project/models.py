from django.db import models
from backend.models import CustomUser

class Project(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

class Contribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project','user')

