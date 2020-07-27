from django.contrib import admin
from django.db import models

# Create your models here.

from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=10)
    school = models.CharField(max_length=32)
    marjor = models.CharField(max_length=32)
    counte = models.IntegerField()
    type = models.CharField(max_length=32)

    class Meta:
        unique_together = ("email",)


admin.site.register(User)
