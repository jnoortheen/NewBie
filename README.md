# NewBie

NewBie

## Tech stack

1. Python 3.6
1. Django 1.11

## Requirements

- Install all python modules required by

```commandline
pip install -r requirements.txt
```

## Front-end

Front-end libraries are mananged by `npm` and `djnago-npm`.
- run `npm install` to install all dependecies
- run `python manage.py collectstatic` to get files from *node_modules* to *STATIC_ROOT* from where it will get served


## Static Files

### whitenoise

- No need to configure external server to server static files
- Static files are served by whitenoise

## Social Logins

- Django-AllAuth is used for providing all authentication activities including social logins
- In a new environment, we need to create a Site record from django-admin (localhost:8000 will be enough for developing ,
otherwise put the domain name)
- Create a facebook and obtain AppID and secret as usual. Also create a web plaform for the site URL
- For google app to get `ID` & `secret key` through `Google developer Console`
- Create `Social Accounts › Social applications` for both Facebook and Google in django-admin 
