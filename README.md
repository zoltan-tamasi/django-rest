Django-rest
-----------
A very simple RESTful API example built with django and django-rest-framework.

Description
-----------
This API handles blogposts and users associated with them. 

Users can create new posts, view all posts, and modify or delete their own posts using the API endpoint: '/api/blogposts'.

Users cannot modify or delete posts they don't own.

The admin/superuser can create or delete users and change ownership of blogposts.

Every action requires authentication. Tokens can be requested with a valid username and password from the endpoint: '/api/token'.

Running the app
-------------------
 * install dependencies
```
    pip install -r requirements.txt
```
 * clear database
```
    python manage.py flush
```
 * create superuser
```
    python manage.py createsuperuser
```

 * run the test server
```
    python manage.py runserver
```
 * login with created superuser's name and password, start adding users
