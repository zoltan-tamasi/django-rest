from django.db import models
import datetime

class BlogPost(models.Model):
	owner = models.ForeignKey('auth.User', related_name='posts')
	date = models.DateField(default=datetime.date.today)
	text = models.TextField()

