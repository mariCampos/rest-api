# rest-api
API using Falcon framework and JWT Authentication

Python version: 3.6
Database: sqlite3

This project is an API based in two models: User and Denounce

You could create an user and authenticate this user. 
Also, you can register a new violence denounce in a bus, adding lat, lon and id_bus.

# Install

Install a virtualenv using the command:
```
pip3 install virtualenv
```
Then, create a virtualenv for this project:
```
python3 -m venv
```

After that, install the libs:
```
pip3 install -r requirements.txt
```

# Running the application

1. Create a wsgi file called uwsgi.ini with yours configurations
2. Create a Key Pair to JWT Authentication

Run the next command to start the app:

```
uwsgi uwsgi.ini
```
