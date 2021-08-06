from typing import Text
from django.db import models
from django.db.models.fields import DateField
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length = 555550,blank=False, null=False)
    image = ImageField()
    date = DateField( null=False)
       
    def __str__(self):
        return self.text

