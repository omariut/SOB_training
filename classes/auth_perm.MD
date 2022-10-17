# Django Authentication
Django provides an authentication and authorization ("permission") system, built on top of the session framework, that allows you to verify user credentials and define what actions each user is allowed to perform. The framework includes built-in models for Users and Groups (a generic way of applying permissions to more than one user at a time), permissions/flags that designate whether a user may perform a task, forms and views for logging in users, and view tools for restricting content.

### create users app
```
python manage.py startapp users

```

### Enabling authentication
```
INSTALLED_APPS = [
    # …
    'django.contrib.auth',  # Core authentication framework and its default models.
    'django.contrib.contenttypes',  # Django content type system (allows permissions to be associated with models).
    # …

MIDDLEWARE = [
    # …
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions across requests
    # …
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
    # …
```
### Creating users and groups


You already created your first user when we looked at the Django admin site in previous tutorial (this was a superuser, created with the command python manage.py createsuperuser). Our superuser is already authenticated and has all permissions, so we'll need to create a test user to represent a normal site user. We'll be using the admin site to create our locallibrary groups and website logins, as it is one of the quickest ways to do so.

### create users programmatically 

```
from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername' 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'John'
user.last_name = 'Citizen'
user.save()

```

### Setting up your authentication views
- Project URLs
```
path('accounts/', include('django.contrib.auth.urls')),
```
Navigate to the http://127.0.0.1:8000/accounts/ 


### Template directory
```
    # …
    TEMPLATES = [
      {
       # …
       'DIRS': [os.path.join(BASE_DIR, 'templates')],
       'APP_DIRS': True,
       # …

```
