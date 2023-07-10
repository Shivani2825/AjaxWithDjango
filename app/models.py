from django.db import models

class Person(models.Model):
    fname=models.CharField(max_length = 150)
    lname=models.CharField(max_length = 150)

    def __str__(self):
        return self.fname
    