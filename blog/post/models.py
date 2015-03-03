from django.db import models
import datetime

class BlogPost(models.Model):
	date = models.DateField(default=datetime.date.today)
	text = models.TextField()

