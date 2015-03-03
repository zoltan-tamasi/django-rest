from django.db import models

class BlogPost(models.Model):
	text = models.TextField()

