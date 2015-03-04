from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import BlogPost

class TestCase1(APITestCase):

	def test_unauthorized_access(self):        
		response = self.client.post('/api/blogposts/', {}, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestCase2(APITestCase):

	def setUp(self):
		User.objects.create(username='user1', password='user1')

	def test_authorized_access(self):
		user = User.objects.get(username='user1')
		self.client.force_authenticate(user=user)
		response = self.client.get('/api/blogposts/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

        
class TestCase3(APITestCase):
	def setUp(self):
		User.objects.create(username='user1', password='user1')        

	def test_create_and_delete_post(self):
		user = User.objects.get(username='user1')
		test_post_data = 'Test post.'

		self.client.force_authenticate(user=user)

		response = self.client.post('/api/blogposts/', { 'text' : test_post_data })
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		id = response.data.get('id')
		
		post = BlogPost.objects.get(pk=id)
		self.assertEqual(post.text, test_post_data)
		
		response = self.client.delete('/api/blogposts/{}'.format(id))
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

		


