from django.db import models
import datetime

class BlogPost(models.Model):
	owner = models.ForeignKey('auth.User', related_name='posts')
	date = models.DateField(default=datetime.date.today)
	text = models.TextField()

	def __str__(self):
		return 'Post #{}: {}'.format(self.pk, self.text if len(self.text) < 40 else self.text[:40] + '...')


class Authority(models.Model):
	user = models.ForeignKey('auth.User', related_name='author')
	blogpost = models.ForeignKey(BlogPost, related_name='blogpost')
        
	class Meta:
		verbose_name_plural = "authorities"

	def __str__(self):
		return 'Authority: {} authors post #{}'.format(self.user.username, self.blogpost.pk)
