import falcon
import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from falcon_autocrud.middleware import Middleware
from resources import * 
from settings import *

sqlite_db = {'drivername': 'sqlite', 'database': DATABASE_NAME}
print(URL(**sqlite_db))

# Database engine
db_engine = create_engine(DATABASE_PATH)

connection = db_engine.connect()

# falcon.API instances are callable WSGI apps

app = falcon.API()

app.add_route(BASE_URL + "user/register", UserResource(db_engine))

app.add_route(BASE_URL + "user/{id}", UserResource(db_engine))

app.add_route(BASE_URL + "user/auth", AuthenticationResource(db_engine))

app.add_route(BASE_URL + "denounce/create", DenounceResource(db_engine))

app.add_route(BASE_URL + "denounce/complete", DenounceCollectionResource(db_engine))

connection.close()
