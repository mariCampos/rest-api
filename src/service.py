from models import *
from falcon_autocrud.resource import CollectionResource, SingleResource
from resources import *
import grpc

service RouteGuide {
   
   rpc UserResource(SingleResource) returns (User) {}
}
