from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=255, default='New Task')

    def __str__(self):
        return f'{self.name}: {self.task}'