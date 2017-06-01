# NewBie
NewBie

## Tech stack

1. Python 3.6
1. Django 1.11

## Front-end

Front-end libraries are mananged by `npm` and compiled to static folder where Django can find the files.
`django-webpack-loader` is used for managing this generated files. Hence webpack is used we need to have nodejs 
installed in the system.

- run `npm install` to install all dependecies
- run `python manage.py collectstatic` to get files from *node_modules* to *STATIC_ROOT* from where it will get served


## Static Files

### whitenoise

- No need to configure external server to server static files
- Static files are served by whitenoise
