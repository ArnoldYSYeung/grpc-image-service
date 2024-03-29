# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image.proto',
  package='',
  syntax='proto3',
  serialized_options=b'P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bimage.proto\"E\n\x07\x41\x42Image\x12\r\n\x05\x63olor\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\"\xb0\x01\n\x14\x41\x42ImageRotateRequest\x12\x30\n\x08rotation\x18\x01 \x01(\x0e\x32\x1e.ABImageRotateRequest.Rotation\x12\x17\n\x05image\x18\x02 \x01(\x0b\x32\x08.ABImage\"M\n\x08Rotation\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nNINETY_DEG\x10\x01\x12\x12\n\x0eONE_EIGHTY_DEG\x10\x02\x12\x13\n\x0fTWO_SEVENTY_DEG\x10\x03\"0\n\x15\x41\x42ImageRotateResponse\x12\x17\n\x05image\x18\x01 \x01(\x0b\x32\x08.ABImage\"7\n\x1c\x41\x42\x43ustomImageEndpointRequest\x12\x17\n\x05image\x18\x01 \x01(\x0b\x32\x08.ABImage\"7\n\x1d\x41\x42\x43ustomImageEndpointResponse\x12\x16\n\x0e\x63lassification\x18\x01 \x01(\t2\x90\x01\n\x0e\x41\x42ImageService\x12.\n\x0bRotateImage\x12\x15.ABImageRotateRequest\x1a\x08.ABImage\x12N\n\rRecognizeFace\x12\x1d.ABCustomImageEndpointRequest\x1a\x1e.ABCustomImageEndpointResponseB\x02P\x01\x62\x06proto3'
)



_ABIMAGEROTATEREQUEST_ROTATION = _descriptor.EnumDescriptor(
  name='Rotation',
  full_name='ABImageRotateRequest.Rotation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NINETY_DEG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONE_EIGHTY_DEG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TWO_SEVENTY_DEG', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=186,
  serialized_end=263,
)
_sym_db.RegisterEnumDescriptor(_ABIMAGEROTATEREQUEST_ROTATION)


_ABIMAGE = _descriptor.Descriptor(
  name='ABImage',
  full_name='ABImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='ABImage.color', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ABImage.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='ABImage.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='ABImage.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=15,
  serialized_end=84,
)


_ABIMAGEROTATEREQUEST = _descriptor.Descriptor(
  name='ABImageRotateRequest',
  full_name='ABImageRotateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation', full_name='ABImageRotateRequest.rotation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='ABImageRotateRequest.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ABIMAGEROTATEREQUEST_ROTATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=263,
)


_ABIMAGEROTATERESPONSE = _descriptor.Descriptor(
  name='ABImageRotateResponse',
  full_name='ABImageRotateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='ABImageRotateResponse.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=265,
  serialized_end=313,
)


_ABCUSTOMIMAGEENDPOINTREQUEST = _descriptor.Descriptor(
  name='ABCustomImageEndpointRequest',
  full_name='ABCustomImageEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='ABCustomImageEndpointRequest.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=315,
  serialized_end=370,
)


_ABCUSTOMIMAGEENDPOINTRESPONSE = _descriptor.Descriptor(
  name='ABCustomImageEndpointResponse',
  full_name='ABCustomImageEndpointResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification', full_name='ABCustomImageEndpointResponse.classification', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=372,
  serialized_end=427,
)

_ABIMAGEROTATEREQUEST.fields_by_name['rotation'].enum_type = _ABIMAGEROTATEREQUEST_ROTATION
_ABIMAGEROTATEREQUEST.fields_by_name['image'].message_type = _ABIMAGE
_ABIMAGEROTATEREQUEST_ROTATION.containing_type = _ABIMAGEROTATEREQUEST
_ABIMAGEROTATERESPONSE.fields_by_name['image'].message_type = _ABIMAGE
_ABCUSTOMIMAGEENDPOINTREQUEST.fields_by_name['image'].message_type = _ABIMAGE
DESCRIPTOR.message_types_by_name['ABImage'] = _ABIMAGE
DESCRIPTOR.message_types_by_name['ABImageRotateRequest'] = _ABIMAGEROTATEREQUEST
DESCRIPTOR.message_types_by_name['ABImageRotateResponse'] = _ABIMAGEROTATERESPONSE
DESCRIPTOR.message_types_by_name['ABCustomImageEndpointRequest'] = _ABCUSTOMIMAGEENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['ABCustomImageEndpointResponse'] = _ABCUSTOMIMAGEENDPOINTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ABImage = _reflection.GeneratedProtocolMessageType('ABImage', (_message.Message,), {
  'DESCRIPTOR' : _ABIMAGE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:ABImage)
  })
_sym_db.RegisterMessage(ABImage)

ABImageRotateRequest = _reflection.GeneratedProtocolMessageType('ABImageRotateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ABIMAGEROTATEREQUEST,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:ABImageRotateRequest)
  })
_sym_db.RegisterMessage(ABImageRotateRequest)

ABImageRotateResponse = _reflection.GeneratedProtocolMessageType('ABImageRotateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ABIMAGEROTATERESPONSE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:ABImageRotateResponse)
  })
_sym_db.RegisterMessage(ABImageRotateResponse)

ABCustomImageEndpointRequest = _reflection.GeneratedProtocolMessageType('ABCustomImageEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _ABCUSTOMIMAGEENDPOINTREQUEST,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:ABCustomImageEndpointRequest)
  })
_sym_db.RegisterMessage(ABCustomImageEndpointRequest)

ABCustomImageEndpointResponse = _reflection.GeneratedProtocolMessageType('ABCustomImageEndpointResponse', (_message.Message,), {
  'DESCRIPTOR' : _ABCUSTOMIMAGEENDPOINTRESPONSE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:ABCustomImageEndpointResponse)
  })
_sym_db.RegisterMessage(ABCustomImageEndpointResponse)


DESCRIPTOR._options = None

_ABIMAGESERVICE = _descriptor.ServiceDescriptor(
  name='ABImageService',
  full_name='ABImageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=430,
  serialized_end=574,
  methods=[
  _descriptor.MethodDescriptor(
    name='RotateImage',
    full_name='ABImageService.RotateImage',
    index=0,
    containing_service=None,
    input_type=_ABIMAGEROTATEREQUEST,
    output_type=_ABIMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RecognizeFace',
    full_name='ABImageService.RecognizeFace',
    index=1,
    containing_service=None,
    input_type=_ABCUSTOMIMAGEENDPOINTREQUEST,
    output_type=_ABCUSTOMIMAGEENDPOINTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ABIMAGESERVICE)

DESCRIPTOR.services_by_name['ABImageService'] = _ABIMAGESERVICE

# @@protoc_insertion_point(module_scope)
