# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16object_detection.proto\"(\n\x12UploadImageRequest\x12\x12\n\ndata_block\x18\x01 \x01(\x0c\")\n\x0e\x44\x65tectResponse\x12\x17\n\x06object\x18\x01 \x03(\x0b\x32\x07.Object\"7\n\tRectangle\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01w\x18\x03 \x01(\x05\x12\t\n\x01h\x18\x04 \x01(\x05\"I\n\x06Object\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x1d\n\trectangle\x18\x03 \x01(\x0b\x32\n.Rectangle2E\n\x0fObjectDetection\x12\x32\n\x06\x64\x65tect\x12\x13.UploadImageRequest\x1a\x0f.DetectResponse\"\x00(\x01\x62\x06proto3')
)




_UPLOADIMAGEREQUEST = _descriptor.Descriptor(
  name='UploadImageRequest',
  full_name='UploadImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_block', full_name='UploadImageRequest.data_block', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=26,
  serialized_end=66,
)


_DETECTRESPONSE = _descriptor.Descriptor(
  name='DetectResponse',
  full_name='DetectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='DetectResponse.object', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=68,
  serialized_end=109,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Rectangle.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Rectangle.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='Rectangle.w', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h', full_name='Rectangle.h', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=111,
  serialized_end=166,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Object.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Object.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rectangle', full_name='Object.rectangle', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=168,
  serialized_end=241,
)

_DETECTRESPONSE.fields_by_name['object'].message_type = _OBJECT
_OBJECT.fields_by_name['rectangle'].message_type = _RECTANGLE
DESCRIPTOR.message_types_by_name['UploadImageRequest'] = _UPLOADIMAGEREQUEST
DESCRIPTOR.message_types_by_name['DetectResponse'] = _DETECTRESPONSE
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadImageRequest = _reflection.GeneratedProtocolMessageType('UploadImageRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADIMAGEREQUEST,
  __module__ = 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:UploadImageRequest)
  ))
_sym_db.RegisterMessage(UploadImageRequest)

DetectResponse = _reflection.GeneratedProtocolMessageType('DetectResponse', (_message.Message,), dict(
  DESCRIPTOR = _DETECTRESPONSE,
  __module__ = 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:DetectResponse)
  ))
_sym_db.RegisterMessage(DetectResponse)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), dict(
  DESCRIPTOR = _RECTANGLE,
  __module__ = 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:Rectangle)
  ))
_sym_db.RegisterMessage(Rectangle)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(
  DESCRIPTOR = _OBJECT,
  __module__ = 'object_detection_pb2'
  # @@protoc_insertion_point(class_scope:Object)
  ))
_sym_db.RegisterMessage(Object)



_OBJECTDETECTION = _descriptor.ServiceDescriptor(
  name='ObjectDetection',
  full_name='ObjectDetection',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=243,
  serialized_end=312,
  methods=[
  _descriptor.MethodDescriptor(
    name='detect',
    full_name='ObjectDetection.detect',
    index=0,
    containing_service=None,
    input_type=_UPLOADIMAGEREQUEST,
    output_type=_DETECTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBJECTDETECTION)

DESCRIPTOR.services_by_name['ObjectDetection'] = _OBJECTDETECTION

# @@protoc_insertion_point(module_scope)
