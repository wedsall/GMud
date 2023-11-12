# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mud_pb2 as mud__pb2


class MudServiceStub(object):
    """The gRPC service definition for MudService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecuteCommand = channel.unary_unary(
                '/mud.MudService/ExecuteCommand',
                request_serializer=mud__pb2.CommandRequest.SerializeToString,
                response_deserializer=mud__pb2.CommandResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/mud.MudService/Login',
                request_serializer=mud__pb2.LoginRequest.SerializeToString,
                response_deserializer=mud__pb2.LoginResponse.FromString,
                )
        self.KeepAlive = channel.unary_unary(
                '/mud.MudService/KeepAlive',
                request_serializer=mud__pb2.KeepAliveRequest.SerializeToString,
                response_deserializer=mud__pb2.KeepAliveResponse.FromString,
                )
        self.StreamMessages = channel.unary_stream(
                '/mud.MudService/StreamMessages',
                request_serializer=mud__pb2.StreamMessagesRequest.SerializeToString,
                response_deserializer=mud__pb2.StreamMessagesResponse.FromString,
                )


class MudServiceServicer(object):
    """The gRPC service definition for MudService
    """

    def ExecuteCommand(self, request, context):
        """Define an RPC method to execute a command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeepAlive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MudServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecuteCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteCommand,
                    request_deserializer=mud__pb2.CommandRequest.FromString,
                    response_serializer=mud__pb2.CommandResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=mud__pb2.LoginRequest.FromString,
                    response_serializer=mud__pb2.LoginResponse.SerializeToString,
            ),
            'KeepAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.KeepAlive,
                    request_deserializer=mud__pb2.KeepAliveRequest.FromString,
                    response_serializer=mud__pb2.KeepAliveResponse.SerializeToString,
            ),
            'StreamMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMessages,
                    request_deserializer=mud__pb2.StreamMessagesRequest.FromString,
                    response_serializer=mud__pb2.StreamMessagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mud.MudService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MudService(object):
    """The gRPC service definition for MudService
    """

    @staticmethod
    def ExecuteCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mud.MudService/ExecuteCommand',
            mud__pb2.CommandRequest.SerializeToString,
            mud__pb2.CommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mud.MudService/Login',
            mud__pb2.LoginRequest.SerializeToString,
            mud__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeepAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mud.MudService/KeepAlive',
            mud__pb2.KeepAliveRequest.SerializeToString,
            mud__pb2.KeepAliveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mud.MudService/StreamMessages',
            mud__pb2.StreamMessagesRequest.SerializeToString,
            mud__pb2.StreamMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
