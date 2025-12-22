from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

