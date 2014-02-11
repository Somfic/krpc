# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='Orbit.proto',
  package='Orbit',
  serialized_pb='\n\x0bOrbit.proto\x12\x05Orbit\"\xc4\x01\n\tOrbitData\x12\x10\n\x08\x61poapsis\x18\x01 \x02(\x01\x12\x11\n\tperiapsis\x18\x02 \x02(\x01\x12\x14\n\x0c\x65\x63\x63\x65ntricity\x18\x03 \x02(\x01\x12\x13\n\x0binclination\x18\x04 \x02(\x01\x12 \n\x18longitudeOfAscendingNode\x18\x05 \x02(\x01\x12\x1b\n\x13\x61rgumentOfPeriapsis\x18\x06 \x02(\x01\x12\x1a\n\x12meanAnomalyAtEpoch\x18\x07 \x02(\x01\x12\x0c\n\x04\x62ody\x18\x08 \x02(\t')




_ORBITDATA = descriptor.Descriptor(
  name='OrbitData',
  full_name='Orbit.OrbitData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='apoapsis', full_name='Orbit.OrbitData.apoapsis', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='periapsis', full_name='Orbit.OrbitData.periapsis', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='eccentricity', full_name='Orbit.OrbitData.eccentricity', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inclination', full_name='Orbit.OrbitData.inclination', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='longitudeOfAscendingNode', full_name='Orbit.OrbitData.longitudeOfAscendingNode', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='argumentOfPeriapsis', full_name='Orbit.OrbitData.argumentOfPeriapsis', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='meanAnomalyAtEpoch', full_name='Orbit.OrbitData.meanAnomalyAtEpoch', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='body', full_name='Orbit.OrbitData.body', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=219,
)

DESCRIPTOR.message_types_by_name['OrbitData'] = _ORBITDATA

class OrbitData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ORBITDATA
  
  # @@protoc_insertion_point(class_scope:Orbit.OrbitData)

# @@protoc_insertion_point(module_scope)
