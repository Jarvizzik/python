from django.db import models

class Song(models.Model):
	name = models.CharField(max_length = 15)
	author = models.CharField(max_length = 15)
	adder = models.CharField(max_length = 15,default='Anonymous')
	added_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
# Create your models here.