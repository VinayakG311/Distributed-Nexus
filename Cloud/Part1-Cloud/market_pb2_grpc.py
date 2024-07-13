# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import market_pb2 as market__pb2


class MarketStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerSeller = channel.unary_unary(
                '/Market/registerSeller',
                request_serializer=market__pb2.registerSellerReq.SerializeToString,
                response_deserializer=market__pb2.registerSellerRes.FromString,
                )
        self.sellItem = channel.unary_unary(
                '/Market/sellItem',
                request_serializer=market__pb2.sellItemReq.SerializeToString,
                response_deserializer=market__pb2.sellItemRes.FromString,
                )
        self.addProduct = channel.unary_unary(
                '/Market/addProduct',
                request_serializer=market__pb2.Product.SerializeToString,
                response_deserializer=market__pb2.void.FromString,
                )
        self.updateProduct = channel.unary_unary(
                '/Market/updateProduct',
                request_serializer=market__pb2.UpdateItemReq.SerializeToString,
                response_deserializer=market__pb2.UpdateItemRes.FromString,
                )
        self.deleteProduct = channel.unary_unary(
                '/Market/deleteProduct',
                request_serializer=market__pb2.DeleteItemReq.SerializeToString,
                response_deserializer=market__pb2.DeleteItemRes.FromString,
                )
        self.viewProduct = channel.unary_unary(
                '/Market/viewProduct',
                request_serializer=market__pb2.void.SerializeToString,
                response_deserializer=market__pb2.Product.FromString,
                )
        self.searchProduct = channel.unary_unary(
                '/Market/searchProduct',
                request_serializer=market__pb2.SearchReq.SerializeToString,
                response_deserializer=market__pb2.Products.FromString,
                )
        self.addRating = channel.unary_unary(
                '/Market/addRating',
                request_serializer=market__pb2.Rate_an_item.SerializeToString,
                response_deserializer=market__pb2.UpdateItemRes.FromString,
                )
        self.displayProducts = channel.unary_unary(
                '/Market/displayProducts',
                request_serializer=market__pb2.Seller.SerializeToString,
                response_deserializer=market__pb2.Products.FromString,
                )
        self.buyProduct = channel.unary_unary(
                '/Market/buyProduct',
                request_serializer=market__pb2.BuyItemReq.SerializeToString,
                response_deserializer=market__pb2.BuyItemRes.FromString,
                )
        self.addtoWishlist = channel.unary_unary(
                '/Market/addtoWishlist',
                request_serializer=market__pb2.WishListReq.SerializeToString,
                response_deserializer=market__pb2.WishListRes.FromString,
                )
        self.NotifyBuyer = channel.unary_unary(
                '/Market/NotifyBuyer',
                request_serializer=market__pb2.NotificationReq.SerializeToString,
                response_deserializer=market__pb2.NotificationRes.FromString,
                )
        self.NotifySeller = channel.unary_unary(
                '/Market/NotifySeller',
                request_serializer=market__pb2.NotificationReq.SerializeToString,
                response_deserializer=market__pb2.NotificationRes.FromString,
                )


class MarketServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registerSeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sellItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def viewProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def searchProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def displayProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buyProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addtoWishlist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyBuyer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifySeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registerSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.registerSeller,
                    request_deserializer=market__pb2.registerSellerReq.FromString,
                    response_serializer=market__pb2.registerSellerRes.SerializeToString,
            ),
            'sellItem': grpc.unary_unary_rpc_method_handler(
                    servicer.sellItem,
                    request_deserializer=market__pb2.sellItemReq.FromString,
                    response_serializer=market__pb2.sellItemRes.SerializeToString,
            ),
            'addProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.addProduct,
                    request_deserializer=market__pb2.Product.FromString,
                    response_serializer=market__pb2.void.SerializeToString,
            ),
            'updateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.updateProduct,
                    request_deserializer=market__pb2.UpdateItemReq.FromString,
                    response_serializer=market__pb2.UpdateItemRes.SerializeToString,
            ),
            'deleteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteProduct,
                    request_deserializer=market__pb2.DeleteItemReq.FromString,
                    response_serializer=market__pb2.DeleteItemRes.SerializeToString,
            ),
            'viewProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.viewProduct,
                    request_deserializer=market__pb2.void.FromString,
                    response_serializer=market__pb2.Product.SerializeToString,
            ),
            'searchProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.searchProduct,
                    request_deserializer=market__pb2.SearchReq.FromString,
                    response_serializer=market__pb2.Products.SerializeToString,
            ),
            'addRating': grpc.unary_unary_rpc_method_handler(
                    servicer.addRating,
                    request_deserializer=market__pb2.Rate_an_item.FromString,
                    response_serializer=market__pb2.UpdateItemRes.SerializeToString,
            ),
            'displayProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.displayProducts,
                    request_deserializer=market__pb2.Seller.FromString,
                    response_serializer=market__pb2.Products.SerializeToString,
            ),
            'buyProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.buyProduct,
                    request_deserializer=market__pb2.BuyItemReq.FromString,
                    response_serializer=market__pb2.BuyItemRes.SerializeToString,
            ),
            'addtoWishlist': grpc.unary_unary_rpc_method_handler(
                    servicer.addtoWishlist,
                    request_deserializer=market__pb2.WishListReq.FromString,
                    response_serializer=market__pb2.WishListRes.SerializeToString,
            ),
            'NotifyBuyer': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyBuyer,
                    request_deserializer=market__pb2.NotificationReq.FromString,
                    response_serializer=market__pb2.NotificationRes.SerializeToString,
            ),
            'NotifySeller': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifySeller,
                    request_deserializer=market__pb2.NotificationReq.FromString,
                    response_serializer=market__pb2.NotificationRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Market', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Market(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registerSeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/registerSeller',
            market__pb2.registerSellerReq.SerializeToString,
            market__pb2.registerSellerRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sellItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/sellItem',
            market__pb2.sellItemReq.SerializeToString,
            market__pb2.sellItemRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/addProduct',
            market__pb2.Product.SerializeToString,
            market__pb2.void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/updateProduct',
            market__pb2.UpdateItemReq.SerializeToString,
            market__pb2.UpdateItemRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/deleteProduct',
            market__pb2.DeleteItemReq.SerializeToString,
            market__pb2.DeleteItemRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def viewProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/viewProduct',
            market__pb2.void.SerializeToString,
            market__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def searchProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/searchProduct',
            market__pb2.SearchReq.SerializeToString,
            market__pb2.Products.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/addRating',
            market__pb2.Rate_an_item.SerializeToString,
            market__pb2.UpdateItemRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def displayProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/displayProducts',
            market__pb2.Seller.SerializeToString,
            market__pb2.Products.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buyProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/buyProduct',
            market__pb2.BuyItemReq.SerializeToString,
            market__pb2.BuyItemRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addtoWishlist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/addtoWishlist',
            market__pb2.WishListReq.SerializeToString,
            market__pb2.WishListRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyBuyer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/NotifyBuyer',
            market__pb2.NotificationReq.SerializeToString,
            market__pb2.NotificationRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifySeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Market/NotifySeller',
            market__pb2.NotificationReq.SerializeToString,
            market__pb2.NotificationRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)