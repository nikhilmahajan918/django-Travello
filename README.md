# Travello Web Appliaction

Travello allows a user to view & check all locations.

## Technologies I used

- Python backend
- Django web framework
- Postgres database
- Psycopg2
- HTML/CSS

## Installation

Clone this repo to your machine. If you need help with this part, GitHub has [great documentation](https://help.github.com/articles/fork-a-repo/)

if you don't have python setup in ur computer ,download it by [click here](https://www.python.org/downloads/)

Now,We need to create a virtual environment in our copy of the repository, so that the technologies you download to make Travello web appliaction work don't interfere with any other technologies you may have installed on your computer. Now, if you are not familiar with virtualenv or not have a setup install on ur computer then uh not need to worry about that.
simply paste below cmd in ur terminal.
`$ pip install virtualenvwrapper-win`
after installation, make sure you're in the `django-travello/` directory then type the following in your Terminal:

`$ virtualenv env`

Next, type `$ source env/bin/activate` to create a "bubble" around the workspace.

You will see that there is now '(env)' in front of the command line prompt: `(env) $`

It is worth mentioning the .gitignore file at this point. There are certain files that we don't want or need to commit to the repository, and the names of those files will go inside a different file called `.gitignore`. When we eventually do make our commits, git will automatically ignore the files listed inside the .gitignore file. The .gitignore file is already included in the django-travello repository you cloned -- you don't need to do anything here.

We now need to install all the libraries and technologies that appear in the file `requirements.txt`. From the `django-travello/` directory (which you should still be in), simply type the following into your Terminal:

`(env) $ pip install -r requirements.txt`

if you find a error message reagards decouple or importing config, go to `django-travello/Nikhil/settings.py`
and manually delete below code.
'from decouple import config'

if all works well,You should see a success message similar to this at the bottom of the Terminal window:

```python
Installing collected packages: Django, Decouple, psycopg2, pillow.
Successfully installed Django-3.1 decouple-3.3 psycopg2-2.6.1 pillow-7.2.0
```

You will need a SECRET_KEY for django app. obtain one from [MiniWebTool](http://www.miniwebtool.com/django-secret-key-generator/). Copy and paste the SECRET_KEY into `django-travello/Nikhil/Settings.py` like so (do not include the brackets):

## Database Setup

Download [Postgres](http://postgresapp.com/) if you don't already have it, and install it. Make sure it is running! If you're on a Mac, there will be a small black elephant in the upper right corner of your menu bar.

We can launch an interactive Postgres console in a windows Terminal. open ur windows cmd terminal , now make sure you are in right directory i.e where postgres sql is actually located in ur computer.
for windows, it is in program files so,
C:\Program Files\PostgreSQL\12\bin>psql -U postgres -h localhost
after that, they ask for password which uh manually set up for ur postgresql.

To create a user, type the following command into the Terminal. Replace 'name' with your name and typeurpasswordhere with ur password (no white spaces!):

```python
CREATE USER name with password 'typeurpasswordhere';
CREATE ROLE
```

Next, we need to create the actual database. Type the following command into the Terminal. Replace 'db_name' with the name you want to give to the database (no white spaces!) and 'name' with the name you created for yourself in the previous step.

```python
CREATE DATABASE db_name OWNER name;
CREATE DATABASE
```

Cool, now we have a database! We need to tell django-travello that it exists. Find this chunk of text in your `django-travello/Nikhil/settings.py` file, and update the placeholder database text for 'NAME' with the 'db_name' you created in the previous steps. Update 'USER' with the 'name' you created in the previous steps.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
```

Switch back to the first Terminal tab you created (make sure you're still in your virtual environment) and run `python manage.py migrate` in the Terminal. You should see a success message.

## Admin Account Setup

We're getting so close! Let's create an admin. Run this command in the Terminal and follow the prompts to enter your name, email and password:

`python manage.py createsuperuser`

## Server Setup

Woo hoo! You're now ready to run your server! Using the same Terminal tab from the steps we just completed for the admin, type the following command in your Terminal:

`(env) $ python manage.py runserver`

You can now visit the URL `http://localhost:8000`

## About the author

[LinkedIn - Nikhil Mahajan](https://www.linkedin.com/in/nikhil-mahajan-92b9631a0/ "Nikhil Mahajan's LinkedIn profile")

```

```
