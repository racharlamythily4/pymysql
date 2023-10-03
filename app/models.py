from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    url=models.URLField()