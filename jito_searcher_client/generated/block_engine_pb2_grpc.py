# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import block_engine_pb2 as block__engine__pb2


class BlockEngineValidatorStub(object):
    """/ Validators can connect to Block Engines to receive packets and bundles.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribePackets = channel.unary_stream(
                '/block_engine.BlockEngineValidator/SubscribePackets',
                request_serializer=block__engine__pb2.SubscribePacketsRequest.SerializeToString,
                response_deserializer=block__engine__pb2.SubscribePacketsResponse.FromString,
                )
        self.SubscribeBundles = channel.unary_stream(
                '/block_engine.BlockEngineValidator/SubscribeBundles',
                request_serializer=block__engine__pb2.SubscribeBundlesRequest.SerializeToString,
                response_deserializer=block__engine__pb2.SubscribeBundlesResponse.FromString,
                )
        self.GetBlockBuilderFeeInfo = channel.unary_unary(
                '/block_engine.BlockEngineValidator/GetBlockBuilderFeeInfo',
                request_serializer=block__engine__pb2.BlockBuilderFeeInfoRequest.SerializeToString,
                response_deserializer=block__engine__pb2.BlockBuilderFeeInfoResponse.FromString,
                )


class BlockEngineValidatorServicer(object):
    """/ Validators can connect to Block Engines to receive packets and bundles.
    """

    def SubscribePackets(self, request, context):
        """/ Validators can subscribe to the block engine to receive a stream of packets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeBundles(self, request, context):
        """/ Validators can subscribe to the block engine to receive a stream of simulated and profitable bundles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockBuilderFeeInfo(self, request, context):
        """Block builders can optionally collect fees. This returns fee information if a block builder wants to
        collect one.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BlockEngineValidatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribePackets': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribePackets,
                    request_deserializer=block__engine__pb2.SubscribePacketsRequest.FromString,
                    response_serializer=block__engine__pb2.SubscribePacketsResponse.SerializeToString,
            ),
            'SubscribeBundles': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeBundles,
                    request_deserializer=block__engine__pb2.SubscribeBundlesRequest.FromString,
                    response_serializer=block__engine__pb2.SubscribeBundlesResponse.SerializeToString,
            ),
            'GetBlockBuilderFeeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockBuilderFeeInfo,
                    request_deserializer=block__engine__pb2.BlockBuilderFeeInfoRequest.FromString,
                    response_serializer=block__engine__pb2.BlockBuilderFeeInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'block_engine.BlockEngineValidator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BlockEngineValidator(object):
    """/ Validators can connect to Block Engines to receive packets and bundles.
    """

    @staticmethod
    def SubscribePackets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/block_engine.BlockEngineValidator/SubscribePackets',
            block__engine__pb2.SubscribePacketsRequest.SerializeToString,
            block__engine__pb2.SubscribePacketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeBundles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/block_engine.BlockEngineValidator/SubscribeBundles',
            block__engine__pb2.SubscribeBundlesRequest.SerializeToString,
            block__engine__pb2.SubscribeBundlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockBuilderFeeInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/block_engine.BlockEngineValidator/GetBlockBuilderFeeInfo',
            block__engine__pb2.BlockBuilderFeeInfoRequest.SerializeToString,
            block__engine__pb2.BlockBuilderFeeInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BlockEngineRelayerStub(object):
    """/ Relayers can forward packets to Block Engines.
    / Block Engines provide an AccountsOfInterest field to only send transactions that are of interest.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeAccountsOfInterest = channel.unary_stream(
                '/block_engine.BlockEngineRelayer/SubscribeAccountsOfInterest',
                request_serializer=block__engine__pb2.AccountsOfInterestRequest.SerializeToString,
                response_deserializer=block__engine__pb2.AccountsOfInterestUpdate.FromString,
                )
        self.StartExpiringPacketStream = channel.stream_stream(
                '/block_engine.BlockEngineRelayer/StartExpiringPacketStream',
                request_serializer=block__engine__pb2.PacketBatchUpdate.SerializeToString,
                response_deserializer=block__engine__pb2.StartExpiringPacketStreamResponse.FromString,
                )


class BlockEngineRelayerServicer(object):
    """/ Relayers can forward packets to Block Engines.
    / Block Engines provide an AccountsOfInterest field to only send transactions that are of interest.
    """

    def SubscribeAccountsOfInterest(self, request, context):
        """/ The block engine feeds accounts of interest (AOI) updates to the relayer periodically.
        / For all transactions the relayer receives, it forwards transactions to the block engine which write-lock
        / any of the accounts in the AOI.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartExpiringPacketStream(self, request_iterator, context):
        """Validators can subscribe to packets from the relayer and receive a multiplexed signal that contains a mixture
        of packets and heartbeats.
        NOTE: This is a bi-directional stream due to a bug with how Envoy handles half closed client-side streams.
        The issue is being tracked here: https://github.com/envoyproxy/envoy/issues/22748. In the meantime, the
        server will stream heartbeats to clients at some reasonable cadence.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BlockEngineRelayerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeAccountsOfInterest': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeAccountsOfInterest,
                    request_deserializer=block__engine__pb2.AccountsOfInterestRequest.FromString,
                    response_serializer=block__engine__pb2.AccountsOfInterestUpdate.SerializeToString,
            ),
            'StartExpiringPacketStream': grpc.stream_stream_rpc_method_handler(
                    servicer.StartExpiringPacketStream,
                    request_deserializer=block__engine__pb2.PacketBatchUpdate.FromString,
                    response_serializer=block__engine__pb2.StartExpiringPacketStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'block_engine.BlockEngineRelayer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BlockEngineRelayer(object):
    """/ Relayers can forward packets to Block Engines.
    / Block Engines provide an AccountsOfInterest field to only send transactions that are of interest.
    """

    @staticmethod
    def SubscribeAccountsOfInterest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/block_engine.BlockEngineRelayer/SubscribeAccountsOfInterest',
            block__engine__pb2.AccountsOfInterestRequest.SerializeToString,
            block__engine__pb2.AccountsOfInterestUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartExpiringPacketStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/block_engine.BlockEngineRelayer/StartExpiringPacketStream',
            block__engine__pb2.PacketBatchUpdate.SerializeToString,
            block__engine__pb2.StartExpiringPacketStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
