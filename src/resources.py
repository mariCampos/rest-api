from falcon_autocrud.resource import CollectionResource, SingleResource
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
from sqlalchemy import MetaData, select
from sqlalchemy.orm import sessionmaker
from models import *
from settings import *
from authentication import *

import grpc
import apirest_pb2_grpc
import apirest_pb2

import sqlite3
import falcon
import json


Base = declarative_base()
engine = create_engine(DATABASE_PATH)


class UserCollectionResource(CollectionResource):
    model = User


class UserResource(SingleResource):

    model = User
    methods = ['POST', 'GET']

    def on_get(self, req, resp, id):
        connection = engine.connect()
        output = {}

         # create session
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        try:

            row = session.query(User).filter(User.id == id).first()

            output = {
                "Name": row.Name,
                "Email": row.Email
            }
            resp.status = falcon.HTTP_200

        except SQLAlchemyError as e:
            output = {
                "status": "Bad Request"
            }
            resp.status = falcon.HTTP_400 
        finally:
            session.close()
        
        connection.close()
        resp.body = json.dumps(output)


        

    def on_post(self, req, resp):
        connection = engine.connect()

        data = json.loads(req.stream.read())

        output = {}

        if data:
            name = data['name']
            email = data['email']
            password = data['password']

            connection.execute("INSERT INTO user (name, email, password) VALUES (?, ?, ?)", (name, email, password))

            output = {
                "status": "OK"
            }
            resp.status = falcon.HTTP_200
        else:
            output = {
                "status": "Bad Request"
            }
            resp.status = falcon.HTTP_400 
        connection.close()
        
        resp.body = json.dumps(output)


class AuthenticationResource(SingleResource):
    model = User

    def on_post(self, req, resp):
        connection = engine.connect()

        data = json.loads(req.stream.read())

        email = data['email']
        password = data['password']

        output = {}

        result = connection.execute('SELECT * FROM user WHERE Email=?', email).fetchone()
        
        if result:
            if password == result.Password:
                output = {
                    "status": "OK",
                    "token": generate_token(result.id)
                }
                resp.status = falcon.HTTP_200
            else:
                output = {
                    "status": "Bad Request"
                }
                resp.status = falcon.HTTP_400
        else:
            output = {
                    "status": "Not Found"
                }
            resp.status = falcon.HTTP_404
        
        connection.close()
        
        resp.body = json.dumps(output)
        

class DenounceCollectionResource(CollectionResource):
    model = Denounce
    methods = ['GET']

    def on_get(self, req, resp):
        connection = engine.connect()
        output = {}
        denounces = []

        channel = grpc.insecure_channel('localhost:8000')

        result = connection.execute('SELECT * FROM denounce')

        if result:
            for _d in result:
                

                denounce = {
                    "denounce_id": _d.id,
                    "user_id": _d.Id_user,
                    "email": "",
                    "bus_number": _d.Bus_number,
                    "lat": _d.Lat,
                    "lon": _d.Lon
                }

                denounces.append(denounce)

            output = {
                "status": "OK",
                "denounces": denounces
            }
            resp.status = falcon.HTTP_200
        else:
            output = {
                    "status": "Bad Request"
                }
            resp.status = falcon.HTTP_400
        
        connection.close()
        resp.body = json.dumps(output)



class DenounceResource(SingleResource):
    model = Denounce
    methods = ['POST', 'PUT']

    def on_post(self, req, resp):
        connection = engine.connect()

        data = json.loads(req.stream.read())

        output = {}

        if data:
            lat = data['lat']
            lon = data['lon']
            bus_number = data['bus_number']

            result = connection.execute("INSERT INTO denounce (lat, lon, bus_number) VALUES (?, ?, ?)", (lat, lon, bus_number)).lastrowid

            output = {
                "status": "OK",
                "denounce_id": result
            }
            resp.status = falcon.HTTP_200
        else:
            output = {
                "status": "Bad Request"
            }
            resp.status = falcon.HTTP_400 
        connection.close()
        
        resp.body = json.dumps(output)
    
    def on_put(self, req, resp):
        connection = engine.connect()
        output = {}

        data = json.loads(req.stream.read())
        auth = req.auth[7:]

        decoded = decode_token(auth)

        # Elements to be updated
        id_user = decoded.get('id')
        description = data['description']
        id_denounce = data['id_denounce']

       # create session
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        try:

            row = session.query(Denounce).filter(Denounce.id == id_denounce).first()

            row.Description = description
            row.Id_user = id_user

            session.commit()

            output = {
                "status": "OK",
                "denounce_id": id_denounce
            }
            resp.status = falcon.HTTP_200

        except SQLAlchemyError as e:
            output = {
                "status": "Bad Request"
            }
            resp.status = falcon.HTTP_400 
        finally:
            session.close()
        
        connection.close()
        resp.body = json.dumps(output)

       


