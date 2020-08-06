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
    major = models.CharField(max_length=32)
    counter = models.IntegerField()
    type = models.CharField(max_length=32)

    class Meta:
        unique_together = ("email",)


class Article(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=32)
    context = models.CharField(max_length=10240)

    class Meta:
        unique_together = ("email","title")



admin.site.register(User)
admin.site.register(Article)
