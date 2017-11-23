# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import replicator_pb2 as replicator__pb2


class ReplicatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetInstance = channel.unary_stream(
        '/replicator.Replicator/GetInstance',
        request_serializer=replicator__pb2.Request.SerializeToString,
        response_deserializer=replicator__pb2.Response.FromString,
        )


class ReplicatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetInstance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReplicatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetInstance': grpc.unary_stream_rpc_method_handler(
          servicer.GetInstance,
          request_deserializer=replicator__pb2.Request.FromString,
          response_serializer=replicator__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'replicator.Replicator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
