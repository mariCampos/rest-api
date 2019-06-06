# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import apirest_pb2 as src_dot_apirest__pb2


class UserServiceStub(object):
  """Define the service :
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.get_user_by_id = channel.unary_unary(
        '/UserService/get_user_by_id',
        request_serializer=src_dot_apirest__pb2.Id.SerializeToString,
        response_deserializer=src_dot_apirest__pb2.User.FromString,
        )


class UserServiceServicer(object):
  """Define the service :
  """

  def get_user_by_id(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'get_user_by_id': grpc.unary_unary_rpc_method_handler(
          servicer.get_user_by_id,
          request_deserializer=src_dot_apirest__pb2.Id.FromString,
          response_serializer=src_dot_apirest__pb2.User.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
