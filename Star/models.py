from django.contrib import admin
from django.db import models

class Star(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    birthday = models.DateField(verbose_name="生日")
    area = models.TextField(verbose_name="描述")
    hot = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Picture(models.Model):
    star = models.ForeignKey(to=Star, on_delete=models.CASCADE)
    description = models.CharField(max_length=8)
    picture = models.ImageField(upload_to="images")

class Tstar(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    birthday = models.DateField()
    detail = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField()
    content = models.TextField()
    picture = models.ImageField(upload_to="images")
    label = models.CharField(max_length=16)

class ValidCode(models.Model):
    code = models.CharField(max_length=32)
    yield_time = models.FloatField()
    email = models.CharField(max_length=32)


class KidPic(models.Model):
    picture = models.ImageField(upload_to="images")
    star_name = models.CharField(max_length=32)
# Create your models here.
