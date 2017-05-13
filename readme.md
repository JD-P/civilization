# Install #

## Requirements and Dependencies ##

### Requirements ###

    git

    virtualenv

### Dependencies ###

    python3

    django 1.10/1.11

## Instructions for Debian 8 ##

Run:

    apt-get install git virtualenv

Then change directories to wherever you want to host the fortforecast instance, and git clone
this repository into it:

    git clone https://github.com/JD-P/civilization

Create a python3 virtual environment somewhere associated with the fortforecast instance,
probably inside the cloned repository:

    cd civilization
    virtualenv --python=python3 venv

Activate the virtual environment so that it's self contained:

    source venv/bin/activate

Install django:

    pip3 install django

Migrate data structures:

    python3 manage.py makemigrations
    python3 manage.py migrate

Run the initialization script:

    python3 manage.py

Create a superuser:

    python3 manage.py createsuperuser

You'll be prompted for a username and password. Do take care to make these decent on a public instance.

Then to test that everything is working:

    python3 manage.py runserver

Try and login under /login and make a thread, if you can do it the system is working.

Once that's done you have to configure your webserver of choice to run a django
app with WSGI, use google to find an appropriate tutorial.