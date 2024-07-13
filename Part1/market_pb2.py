# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarket.proto\"\x06\n\x04void\"T\n\x05\x42uyer\x12\x0c\n\x04UUID\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x1a\n\x08wishlist\x18\x03 \x03(\x0b\x32\x08.Product\x12\x10\n\x08notif_ip\x18\x04 \x01(\t\"U\n\x06Seller\x12\x0c\n\x04UUID\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x1a\n\x08products\x18\x03 \x03(\x0b\x32\x08.Product\x12\x10\n\x08notif_ip\x18\x04 \x01(\t\"#\n\x07Sellers\x12\x18\n\x07sellers\x18\x01 \x03(\x0b\x32\x07.Seller\"D\n\x0cRate_an_item\x12\x13\n\x0bProductUUID\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"\xfb\x01\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x16\n\x0eseller_address\x18\x05 \x01(\t\x12\x13\n\x0bseller_UUID\x18\x06 \x01(\t\x12\x14\n\x0cProduct_UUID\x18\x07 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x08 \x01(\t\x12\x17\n\x06seller\x18\t \x01(\x0b\x32\x07.Seller\x12\x0e\n\x06rating\x18\n \x01(\x02\x12\x14\n\x0crating_count\x18\x0b \x01(\x05\x12\x18\n\x08wishlist\x18\x0c \x03(\x0b\x32\x06.Buyer\"&\n\x08Products\x12\x1a\n\x08products\x18\x01 \x03(\x0b\x32\x08.Product\"D\n\x11registerSellerReq\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x10\n\x08notif_ip\x18\x03 \x01(\t\",\n\x11registerSellerRes\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\"\xa7\x01\n\x0bsellItemReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rsellerAddress\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x02\x12\x12\n\nsellerUUID\x18\x06 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x07 \x01(\t\x12\x17\n\x06seller\x18\x08 \x01(\x0b\x32\x07.Seller\"K\n\x0bsellItemRes\x12\x13\n\x0bproductUUID\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x17\n\x06seller\x18\x03 \x01(\x0b\x32\x07.Seller\"\xa1\x01\n\rUpdateItemReq\x12\x14\n\x0cProduct_UUID\x18\x01 \x01(\t\x12\x13\n\x0bseller_UUID\x18\x02 \x01(\t\x12\x16\n\x0eseller_address\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x05\x12\x10\n\x08quantity\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x17\n\x06seller\x18\x07 \x01(\x0b\x32\x07.Seller\"4\n\rUpdateItemRes\x12\x13\n\x0bproductUUID\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"R\n\rDeleteItemReq\x12\x14\n\x0cProduct_UUID\x18\x01 \x01(\t\x12\x13\n\x0bseller_UUID\x18\x02 \x01(\t\x12\x16\n\x0eseller_address\x18\x03 \x01(\t\"4\n\rDeleteItemRes\x12\x13\n\x0bproductUUID\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"S\n\x0bWishListReq\x12\x13\n\x0bproductUUID\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08notif_ip\x18\x03 \x01(\t\x12\x0c\n\x04uuid\x18\x04 \x01(\t\"2\n\x0bWishListRes\x12\x13\n\x0bproductUUID\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"@\n\nBuyItemReq\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"1\n\nBuyItemRes\x12\x13\n\x0bproductUUID\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"0\n\tSearchReq\x12\x11\n\titem_name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"B\n\x0fNotificationReq\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04UUID\x18\x02 \x01(\t\x12\x10\n\x08notif_ip\x18\x03 \x01(\t\"\"\n\x0fNotificationRes\x12\x0f\n\x07message\x18\x01 \x01(\t*\"\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01*3\n\x08\x43\x61tegory\x12\x0e\n\nELECTRONIC\x10\x00\x12\x0b\n\x07\x46\x41SHION\x10\x01\x12\n\n\x06OTHERS\x10\x02\x32\xdc\x04\n\x06Market\x12:\n\x0eregisterSeller\x12\x12.registerSellerReq\x1a\x12.registerSellerRes\"\x00\x12(\n\x08sellItem\x12\x0c.sellItemReq\x1a\x0c.sellItemRes\"\x00\x12\x1f\n\naddProduct\x12\x08.Product\x1a\x05.void\"\x00\x12\x31\n\rupdateProduct\x12\x0e.UpdateItemReq\x1a\x0e.UpdateItemRes\"\x00\x12\x31\n\rdeleteProduct\x12\x0e.DeleteItemReq\x1a\x0e.DeleteItemRes\"\x00\x12 \n\x0bviewProduct\x12\x05.void\x1a\x08.Product\"\x00\x12(\n\rsearchProduct\x12\n.SearchReq\x1a\t.Products\"\x00\x12,\n\taddRating\x12\r.Rate_an_item\x1a\x0e.UpdateItemRes\"\x00\x12\'\n\x0f\x64isplayProducts\x12\x07.Seller\x1a\t.Products\"\x00\x12(\n\nbuyProduct\x12\x0b.BuyItemReq\x1a\x0b.BuyItemRes\"\x00\x12-\n\raddtoWishlist\x12\x0c.WishListReq\x1a\x0c.WishListRes\"\x00\x12\x33\n\x0bNotifyBuyer\x12\x10.NotificationReq\x1a\x10.NotificationRes\"\x00\x12\x34\n\x0cNotifySeller\x12\x10.NotificationReq\x1a\x10.NotificationRes\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STATUS']._serialized_start=1725
  _globals['_STATUS']._serialized_end=1759
  _globals['_CATEGORY']._serialized_start=1761
  _globals['_CATEGORY']._serialized_end=1812
  _globals['_VOID']._serialized_start=16
  _globals['_VOID']._serialized_end=22
  _globals['_BUYER']._serialized_start=24
  _globals['_BUYER']._serialized_end=108
  _globals['_SELLER']._serialized_start=110
  _globals['_SELLER']._serialized_end=195
  _globals['_SELLERS']._serialized_start=197
  _globals['_SELLERS']._serialized_end=232
  _globals['_RATE_AN_ITEM']._serialized_start=234
  _globals['_RATE_AN_ITEM']._serialized_end=302
  _globals['_PRODUCT']._serialized_start=305
  _globals['_PRODUCT']._serialized_end=556
  _globals['_PRODUCTS']._serialized_start=558
  _globals['_PRODUCTS']._serialized_end=596
  _globals['_REGISTERSELLERREQ']._serialized_start=598
  _globals['_REGISTERSELLERREQ']._serialized_end=666
  _globals['_REGISTERSELLERRES']._serialized_start=668
  _globals['_REGISTERSELLERRES']._serialized_end=712
  _globals['_SELLITEMREQ']._serialized_start=715
  _globals['_SELLITEMREQ']._serialized_end=882
  _globals['_SELLITEMRES']._serialized_start=884
  _globals['_SELLITEMRES']._serialized_end=959
  _globals['_UPDATEITEMREQ']._serialized_start=962
  _globals['_UPDATEITEMREQ']._serialized_end=1123
  _globals['_UPDATEITEMRES']._serialized_start=1125
  _globals['_UPDATEITEMRES']._serialized_end=1177
  _globals['_DELETEITEMREQ']._serialized_start=1179
  _globals['_DELETEITEMREQ']._serialized_end=1261
  _globals['_DELETEITEMRES']._serialized_start=1263
  _globals['_DELETEITEMRES']._serialized_end=1315
  _globals['_WISHLISTREQ']._serialized_start=1317
  _globals['_WISHLISTREQ']._serialized_end=1400
  _globals['_WISHLISTRES']._serialized_start=1402
  _globals['_WISHLISTRES']._serialized_end=1452
  _globals['_BUYITEMREQ']._serialized_start=1454
  _globals['_BUYITEMREQ']._serialized_end=1518
  _globals['_BUYITEMRES']._serialized_start=1520
  _globals['_BUYITEMRES']._serialized_end=1569
  _globals['_SEARCHREQ']._serialized_start=1571
  _globals['_SEARCHREQ']._serialized_end=1619
  _globals['_NOTIFICATIONREQ']._serialized_start=1621
  _globals['_NOTIFICATIONREQ']._serialized_end=1687
  _globals['_NOTIFICATIONRES']._serialized_start=1689
  _globals['_NOTIFICATIONRES']._serialized_end=1723
  _globals['_MARKET']._serialized_start=1815
  _globals['_MARKET']._serialized_end=2419
# @@protoc_insertion_point(module_scope)
