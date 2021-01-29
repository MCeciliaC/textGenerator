from django.db import models
from django.utils import timezone

# Create your models here.
class Select(models.Model):
    id = models.AutoField(primary_key=True)
    orden= models.IntegerField(verbose_name="orden", null= True, blank=True)
    name= models.CharField(max_length=100)
    class Meta:
        ordering = ['orden']
    def __str__(self):
        return self.name 


class Question(models.Model):
    id = models.AutoField
    orden= models.IntegerField(verbose_name="orden", null= True, blank=True)
    title= models.CharField(max_length=200)
    text= models.TextField()
    categories= models.ForeignKey(Select, on_delete=models.CASCADE)    
    def __str__(self):
        return self.title

class Greeting(models.Model):
    id = models.AutoField
    morning=models.CharField(max_length=200)
    afternoon=models.CharField(max_length=200)
    night=models.CharField(max_length=200)
    by= models.CharField(max_length=200)

    def __str__(self):
        return 'Saludos'
