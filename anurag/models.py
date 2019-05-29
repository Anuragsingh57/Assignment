from django.db import models

# Create your models here.

class Assignment(models.Model):
    select = models.EmailField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.select
