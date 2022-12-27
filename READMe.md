# Django Class Based Views

The sample project for how to use CBV in django framework.

#

# How to Run Project

## Download Codes

```
git clone https://github.com/dori-dev/django-cbv.git
```

```
cd django-cbv
```

## Build Virtual Environment

```
python -m venv env
```

```
source env/bin/activate
```

## Install Project Requirements

```
pip install -r requirements.txt
```

## Change Directory to SRC

```
cd src
```

## Migrate Models

```
python manage.py makemigrations app
python manage.py makemigrations auth
```

```
python manage.py migrate
```

## Add Super User

```
python manage.py createsuperuser
```

## Run Project

```
python manage.py runserver
```

#

# Open On Browser

Admin Page: [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)<br>

### Authentication

Register: [127.0.0.1:8000/auth/register](http://127.0.0.1:8000/auth/register/)<br>
Login: [127.0.0.1:8000/auth/login](http://127.0.0.1:8000/auth/login/)<br>
Logout: [127.0.0.1:8000/auth/logout](http://127.0.0.1:8000/auth/logout/)<br>
Reset Password: [127.0.0.1:8000/auth/reset-password](http://127.0.0.1:8000/auth/reset-password/)<br>

#

### User

User List: [127.0.0.1:8000/users](http://127.0.0.1:8000/users/)<br>
User Detail: [127.0.0.1:8000/auth/user/pk](http://127.0.0.1:8000/auth/user/1/)<br>
User Detail Redirect: [127.0.0.1:8000/auth/user](http://127.0.0.1:8000/auth/user/)<br>
Edit User: [127.0.0.1:8000/auth/user-edit/pk](http://127.0.0.1:8000/auth/user-edit/1/)<br>
Users In Group: [127.0.0.1:8000/users-in-group](http://127.0.0.1:8000/users-in-group/)<br>
Users In Group: [127.0.0.1:8000/users-in-group/group_name](http://127.0.0.1:8000/users-in-group/group_name/)<br>

#

### Group

Group List: [127.0.0.1:8000/groups](http://127.0.0.1:8000/groups/)<br>
Group Detail: [127.0.0.1:8000/group/pk](http://127.0.0.1:8000/group/1/)<br>
Create Group: [127.0.0.1:8000/create-group](http://127.0.0.1:8000/create-group/)<br>
Group Form: [127.0.0.1:8000/group-form](http://127.0.0.1:8000/group-form/)<br>
Update Group: [127.0.0.1:8000/update-group/pk](http://127.0.0.1:8000/update-group/1/)<br>

#

# Links

Download Source Code: [Click Here](https://github.com/dori-dev/django-cbv/archive/refs/heads/master.zip)

My Github Account: [Click Here](https://github.com/dori-dev/)
