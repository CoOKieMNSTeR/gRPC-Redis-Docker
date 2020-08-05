# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'Z(github.com/monkrus/grpc-from0;grpc_from0',
  serialized_pb=b'\n\rservice.proto\x12\x05proto\"\'\n\tSetPerson\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x18\n\tGetPerson\x12\x0b\n\x03key\x18\x01 \x01(\t\"?\n\x0eServerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t2z\n\x0bGrpcService\x12\x33\n\x08RecordDB\x12\x10.proto.SetPerson\x1a\x15.proto.ServerResponse\x12\x36\n\x0bGetRecordDB\x12\x10.proto.GetPerson\x1a\x15.proto.ServerResponseB*Z(github.com/monkrus/grpc-from0;grpc_from0b\x06proto3'
)




_SETPERSON = _descriptor.Descriptor(
  name='SetPerson',
  full_name='proto.SetPerson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.SetPerson.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.SetPerson.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=63,
)


_GETPERSON = _descriptor.Descriptor(
  name='GetPerson',
  full_name='proto.GetPerson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.GetPerson.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=89,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='proto.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='proto.ServerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.ServerResponse.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.ServerResponse.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=154,
)

DESCRIPTOR.message_types_by_name['SetPerson'] = _SETPERSON
DESCRIPTOR.message_types_by_name['GetPerson'] = _GETPERSON
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetPerson = _reflection.GeneratedProtocolMessageType('SetPerson', (_message.Message,), {
  'DESCRIPTOR' : _SETPERSON,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:proto.SetPerson)
  })
_sym_db.RegisterMessage(SetPerson)

GetPerson = _reflection.GeneratedProtocolMessageType('GetPerson', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSON,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetPerson)
  })
_sym_db.RegisterMessage(GetPerson)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:proto.ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)


DESCRIPTOR._options = None

_GRPCSERVICE = _descriptor.ServiceDescriptor(
  name='GrpcService',
  full_name='proto.GrpcService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=156,
  serialized_end=278,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordDB',
    full_name='proto.GrpcService.RecordDB',
    index=0,
    containing_service=None,
    input_type=_SETPERSON,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRecordDB',
    full_name='proto.GrpcService.GetRecordDB',
    index=1,
    containing_service=None,
    input_type=_GETPERSON,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCSERVICE)

DESCRIPTOR.services_by_name['GrpcService'] = _GRPCSERVICE

# @@protoc_insertion_point(module_scope)
