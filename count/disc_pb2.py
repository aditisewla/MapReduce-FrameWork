# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: disc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndisc.proto\x12\x04\x64isc\x1a\x1fgoogle/protobuf/timestamp.proto\"\x06\n\x04void\"3\n\x03red\x12\x0f\n\x07mappers\x18\x01 \x03(\t\x12\x0e\n\x06no_red\x18\x02 \x01(\x05\x12\x0b\n\x03mod\x18\x03 \x01(\x05\"\x10\n\x03str\x12\t\n\x01s\x18\x01 \x01(\t\"5\n\x15StringInt32Dictionary\x12\x0e\n\x06values\x18\x01 \x03(\x05\x12\x0c\n\x04keys\x18\x02 \x03(\t\"\x16\n\x04list\x12\x0e\n\x06values\x18\x01 \x03(\x05\"1\n\nlistoflist\x12\x15\n\x01l\x18\x01 \x03(\x0b\x32\n.disc.list\x12\x0c\n\x04keys\x18\x02 \x03(\t2l\n\x16RegisterReplicaService\x12\x30\n\x06mapper\x12\t.disc.str\x1a\x1b.disc.StringInt32Dictionary\x12 \n\x07reducer\x12\t.disc.red\x1a\n.disc.voidb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'disc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VOID._serialized_start=53
  _VOID._serialized_end=59
  _RED._serialized_start=61
  _RED._serialized_end=112
  _STR._serialized_start=114
  _STR._serialized_end=130
  _STRINGINT32DICTIONARY._serialized_start=132
  _STRINGINT32DICTIONARY._serialized_end=185
  _LIST._serialized_start=187
  _LIST._serialized_end=209
  _LISTOFLIST._serialized_start=211
  _LISTOFLIST._serialized_end=260
  _REGISTERREPLICASERVICE._serialized_start=262
  _REGISTERREPLICASERVICE._serialized_end=370
# @@protoc_insertion_point(module_scope)
