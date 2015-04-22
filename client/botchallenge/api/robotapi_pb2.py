# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robotapi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import materials_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='robotapi.proto',
  package='robominions',
  serialized_pb=_b('\n\x0erobotapi.proto\x12\x0brobominions\x1a\x0fmaterials.proto\"\x97\x01\n\x0cRobotRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x05\x12\x33\n\x0cread_request\x18\x03 \x01(\x0b\x32\x1d.robominions.RobotReadRequest\x12\x37\n\x0e\x61\x63tion_request\x18\x04 \x01(\x0b\x32\x1f.robominions.RobotActionRequest\"-\n\nCoordinate\x12\t\n\x01x\x18\x01 \x02(\x05\x12\t\n\x01y\x18\x02 \x02(\x05\x12\t\n\x01z\x18\x03 \x02(\x05\"\xf5\x01\n\rWorldLocation\x12\x32\n\x11\x61\x62solute_location\x18\x01 \x01(\x0b\x32\x17.robominions.Coordinate\x12\x37\n\tdirection\x18\x02 \x01(\x0e\x32$.robominions.WorldLocation.Direction\"w\n\tDirection\x12\x06\n\x02UP\x10\x00\x12\x08\n\x04\x44OWN\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x03\x12\x0b\n\x07\x46ORWARD\x10\x04\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x05\x12\x08\n\x04\x45\x41ST\x10\x06\x12\x08\n\x04WEST\x10\x07\x12\t\n\x05NORTH\x10\x08\x12\t\n\x05SOUTH\x10\t\"\xe5\x02\n\x10RobotReadRequest\x12\x35\n\x11identify_material\x18\x01 \x01(\x0b\x32\x1a.robominions.WorldLocation\x12\x35\n\x16locate_material_nearby\x18\x02 \x01(\x0b\x32\x15.robominions.Material\x12\x1e\n\x16locate_nonsolid_nearby\x18\x04 \x01(\x08\x12;\n\rlocate_entity\x18\x03 \x01(\x0e\x32$.robominions.RobotReadRequest.Entity\x12\x15\n\rget_inventory\x18\x05 \x01(\x08\x12,\n\x08is_solid\x18\x06 \x01(\x0b\x32\x1a.robominions.WorldLocation\x12\"\n\x1alocate_player_target_block\x18\x07 \x01(\x08\"\x1d\n\x06\x45ntity\x12\x08\n\x04SELF\x10\x00\x12\t\n\x05OWNER\x10\x01\"\xed\x02\n\x12RobotActionRequest\x12<\n\x0emove_direction\x18\x02 \x01(\x0e\x32$.robominions.WorldLocation.Direction\x12<\n\x0eturn_direction\x18\x03 \x01(\x0e\x32$.robominions.WorldLocation.Direction\x12<\n\x0emine_direction\x18\x04 \x01(\x0e\x32$.robominions.WorldLocation.Direction\x12=\n\x0fplace_direction\x18\x05 \x01(\x0e\x32$.robominions.WorldLocation.Direction\x12-\n\x0eplace_material\x18\x06 \x01(\x0b\x32\x15.robominions.Material\x12\x14\n\x0c\x63hat_message\x18\x07 \x01(\t\x12\x19\n\x11is_public_message\x18\x08 \x01(\x08\"A\n\x10LocationResponse\x12-\n\tlocations\x18\x01 \x03(\x0b\x32\x1a.robominions.WorldLocation\"Q\n\x11InventoryResponse\x12(\n\tmaterials\x18\x01 \x03(\x0b\x32\x15.robominions.Material\x12\x12\n\x06\x63ounts\x18\x02 \x03(\x05\x42\x02\x10\x01\"\xa1\x02\n\rRobotResponse\x12\x0b\n\x03key\x18\x03 \x01(\x05\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x30\n\rerror_message\x18\x02 \x01(\x0b\x32\x19.robominions.ErrorMessage\x12\x38\n\x11location_response\x18\x04 \x01(\x0b\x32\x1d.robominions.LocationResponse\x12\x30\n\x11material_response\x18\x05 \x01(\x0b\x32\x15.robominions.Material\x12:\n\x12inventory_response\x18\x06 \x01(\x0b\x32\x1e.robominions.InventoryResponse\x12\x18\n\x10\x62oolean_response\x18\x07 \x01(\x08\"\xc2\x03\n\x0c\x45rrorMessage\x12\x30\n\x06reason\x18\x01 \x01(\x0e\x32 .robominions.ErrorMessage.Reason\x12\x30\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32 .robominions.ErrorMessage.Action\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xfe\x01\n\x06Reason\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cSERVER_ERROR\x10\x01\x12\x16\n\x12UNREADABLE_REQUEST\x10\x02\x12\x13\n\x0fINVALID_REQUEST\x10\x03\x12\x13\n\x0f\x42LOCK_COLLISION\x10\x04\x12\x14\n\x10OUTSIDE_OF_WORLD\x10\x05\x12\x18\n\x14ROBOT_DOES_NOT_EXIST\x10\x06\x12\x1a\n\x16\x42LOCK_IS_NOT_REACHABLE\x10\x07\x12\x18\n\x14\x42LOCK_IS_NOT_VISIBLE\x10\x08\x12\x13\n\x0fNOT_IMPLEMENTED\x10\t\x12\x18\n\x14OWNER_DOES_NOT_EXIST\x10\n\"<\n\x06\x41\x63tion\x12\x0f\n\x0b\x46\x41IL_ACTION\x10\x00\x12\x10\n\x0cRETRY_ACTION\x10\x01\x12\x0f\n\x0b\x45XIT_CLIENT\x10\x02\x42*\n\x1e\x61u.id.katharos.robominions.apiB\x08RobotApi')
  ,
  dependencies=[materials_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_WORLDLOCATION_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='robominions.WorldLocation.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORWARD', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACKWARD', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EAST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEST', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORTH', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUTH', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=376,
  serialized_end=495,
)
_sym_db.RegisterEnumDescriptor(_WORLDLOCATION_DIRECTION)

_ROBOTREADREQUEST_ENTITY = _descriptor.EnumDescriptor(
  name='Entity',
  full_name='robominions.RobotReadRequest.Entity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SELF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OWNER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=826,
  serialized_end=855,
)
_sym_db.RegisterEnumDescriptor(_ROBOTREADREQUEST_ENTITY)

_ERRORMESSAGE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='robominions.ErrorMessage.Reason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREADABLE_REQUEST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK_COLLISION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTSIDE_OF_WORLD', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_DOES_NOT_EXIST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK_IS_NOT_REACHABLE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK_IS_NOT_VISIBLE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IMPLEMENTED', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OWNER_DOES_NOT_EXIST', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1802,
  serialized_end=2056,
)
_sym_db.RegisterEnumDescriptor(_ERRORMESSAGE_REASON)

_ERRORMESSAGE_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='robominions.ErrorMessage.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAIL_ACTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY_ACTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT_CLIENT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2058,
  serialized_end=2118,
)
_sym_db.RegisterEnumDescriptor(_ERRORMESSAGE_ACTION)


_ROBOTREQUEST = _descriptor.Descriptor(
  name='RobotRequest',
  full_name='robominions.RobotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='robominions.RobotRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='robominions.RobotRequest.key', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_request', full_name='robominions.RobotRequest.read_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_request', full_name='robominions.RobotRequest.action_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=200,
)


_COORDINATE = _descriptor.Descriptor(
  name='Coordinate',
  full_name='robominions.Coordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='robominions.Coordinate.x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='robominions.Coordinate.y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='robominions.Coordinate.z', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=247,
)


_WORLDLOCATION = _descriptor.Descriptor(
  name='WorldLocation',
  full_name='robominions.WorldLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='absolute_location', full_name='robominions.WorldLocation.absolute_location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='robominions.WorldLocation.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WORLDLOCATION_DIRECTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=495,
)


_ROBOTREADREQUEST = _descriptor.Descriptor(
  name='RobotReadRequest',
  full_name='robominions.RobotReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identify_material', full_name='robominions.RobotReadRequest.identify_material', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locate_material_nearby', full_name='robominions.RobotReadRequest.locate_material_nearby', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locate_nonsolid_nearby', full_name='robominions.RobotReadRequest.locate_nonsolid_nearby', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locate_entity', full_name='robominions.RobotReadRequest.locate_entity', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_inventory', full_name='robominions.RobotReadRequest.get_inventory', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_solid', full_name='robominions.RobotReadRequest.is_solid', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locate_player_target_block', full_name='robominions.RobotReadRequest.locate_player_target_block', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROBOTREADREQUEST_ENTITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=855,
)


_ROBOTACTIONREQUEST = _descriptor.Descriptor(
  name='RobotActionRequest',
  full_name='robominions.RobotActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='move_direction', full_name='robominions.RobotActionRequest.move_direction', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turn_direction', full_name='robominions.RobotActionRequest.turn_direction', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mine_direction', full_name='robominions.RobotActionRequest.mine_direction', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place_direction', full_name='robominions.RobotActionRequest.place_direction', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place_material', full_name='robominions.RobotActionRequest.place_material', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chat_message', full_name='robominions.RobotActionRequest.chat_message', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_public_message', full_name='robominions.RobotActionRequest.is_public_message', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=1223,
)


_LOCATIONRESPONSE = _descriptor.Descriptor(
  name='LocationResponse',
  full_name='robominions.LocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations', full_name='robominions.LocationResponse.locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  oneofs=[
  ],
  serialized_start=1225,
  serialized_end=1290,
)


_INVENTORYRESPONSE = _descriptor.Descriptor(
  name='InventoryResponse',
  full_name='robominions.InventoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='materials', full_name='robominions.InventoryResponse.materials', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counts', full_name='robominions.InventoryResponse.counts', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1292,
  serialized_end=1373,
)


_ROBOTRESPONSE = _descriptor.Descriptor(
  name='RobotResponse',
  full_name='robominions.RobotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='robominions.RobotResponse.key', index=0,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='robominions.RobotResponse.success', index=1,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='robominions.RobotResponse.error_message', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_response', full_name='robominions.RobotResponse.location_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='material_response', full_name='robominions.RobotResponse.material_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_response', full_name='robominions.RobotResponse.inventory_response', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_response', full_name='robominions.RobotResponse.boolean_response', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  oneofs=[
  ],
  serialized_start=1376,
  serialized_end=1665,
)


_ERRORMESSAGE = _descriptor.Descriptor(
  name='ErrorMessage',
  full_name='robominions.ErrorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='robominions.ErrorMessage.reason', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='robominions.ErrorMessage.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='robominions.ErrorMessage.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERRORMESSAGE_REASON,
    _ERRORMESSAGE_ACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1668,
  serialized_end=2118,
)

_ROBOTREQUEST.fields_by_name['read_request'].message_type = _ROBOTREADREQUEST
_ROBOTREQUEST.fields_by_name['action_request'].message_type = _ROBOTACTIONREQUEST
_WORLDLOCATION.fields_by_name['absolute_location'].message_type = _COORDINATE
_WORLDLOCATION.fields_by_name['direction'].enum_type = _WORLDLOCATION_DIRECTION
_WORLDLOCATION_DIRECTION.containing_type = _WORLDLOCATION
_ROBOTREADREQUEST.fields_by_name['identify_material'].message_type = _WORLDLOCATION
_ROBOTREADREQUEST.fields_by_name['locate_material_nearby'].message_type = materials_pb2._MATERIAL
_ROBOTREADREQUEST.fields_by_name['locate_entity'].enum_type = _ROBOTREADREQUEST_ENTITY
_ROBOTREADREQUEST.fields_by_name['is_solid'].message_type = _WORLDLOCATION
_ROBOTREADREQUEST_ENTITY.containing_type = _ROBOTREADREQUEST
_ROBOTACTIONREQUEST.fields_by_name['move_direction'].enum_type = _WORLDLOCATION_DIRECTION
_ROBOTACTIONREQUEST.fields_by_name['turn_direction'].enum_type = _WORLDLOCATION_DIRECTION
_ROBOTACTIONREQUEST.fields_by_name['mine_direction'].enum_type = _WORLDLOCATION_DIRECTION
_ROBOTACTIONREQUEST.fields_by_name['place_direction'].enum_type = _WORLDLOCATION_DIRECTION
_ROBOTACTIONREQUEST.fields_by_name['place_material'].message_type = materials_pb2._MATERIAL
_LOCATIONRESPONSE.fields_by_name['locations'].message_type = _WORLDLOCATION
_INVENTORYRESPONSE.fields_by_name['materials'].message_type = materials_pb2._MATERIAL
_ROBOTRESPONSE.fields_by_name['error_message'].message_type = _ERRORMESSAGE
_ROBOTRESPONSE.fields_by_name['location_response'].message_type = _LOCATIONRESPONSE
_ROBOTRESPONSE.fields_by_name['material_response'].message_type = materials_pb2._MATERIAL
_ROBOTRESPONSE.fields_by_name['inventory_response'].message_type = _INVENTORYRESPONSE
_ERRORMESSAGE.fields_by_name['reason'].enum_type = _ERRORMESSAGE_REASON
_ERRORMESSAGE.fields_by_name['action'].enum_type = _ERRORMESSAGE_ACTION
_ERRORMESSAGE_REASON.containing_type = _ERRORMESSAGE
_ERRORMESSAGE_ACTION.containing_type = _ERRORMESSAGE
DESCRIPTOR.message_types_by_name['RobotRequest'] = _ROBOTREQUEST
DESCRIPTOR.message_types_by_name['Coordinate'] = _COORDINATE
DESCRIPTOR.message_types_by_name['WorldLocation'] = _WORLDLOCATION
DESCRIPTOR.message_types_by_name['RobotReadRequest'] = _ROBOTREADREQUEST
DESCRIPTOR.message_types_by_name['RobotActionRequest'] = _ROBOTACTIONREQUEST
DESCRIPTOR.message_types_by_name['LocationResponse'] = _LOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['InventoryResponse'] = _INVENTORYRESPONSE
DESCRIPTOR.message_types_by_name['RobotResponse'] = _ROBOTRESPONSE
DESCRIPTOR.message_types_by_name['ErrorMessage'] = _ERRORMESSAGE

RobotRequest = _reflection.GeneratedProtocolMessageType('RobotRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTREQUEST,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.RobotRequest)
  ))
_sym_db.RegisterMessage(RobotRequest)

Coordinate = _reflection.GeneratedProtocolMessageType('Coordinate', (_message.Message,), dict(
  DESCRIPTOR = _COORDINATE,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.Coordinate)
  ))
_sym_db.RegisterMessage(Coordinate)

WorldLocation = _reflection.GeneratedProtocolMessageType('WorldLocation', (_message.Message,), dict(
  DESCRIPTOR = _WORLDLOCATION,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.WorldLocation)
  ))
_sym_db.RegisterMessage(WorldLocation)

RobotReadRequest = _reflection.GeneratedProtocolMessageType('RobotReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTREADREQUEST,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.RobotReadRequest)
  ))
_sym_db.RegisterMessage(RobotReadRequest)

RobotActionRequest = _reflection.GeneratedProtocolMessageType('RobotActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTACTIONREQUEST,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.RobotActionRequest)
  ))
_sym_db.RegisterMessage(RobotActionRequest)

LocationResponse = _reflection.GeneratedProtocolMessageType('LocationResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOCATIONRESPONSE,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.LocationResponse)
  ))
_sym_db.RegisterMessage(LocationResponse)

InventoryResponse = _reflection.GeneratedProtocolMessageType('InventoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYRESPONSE,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.InventoryResponse)
  ))
_sym_db.RegisterMessage(InventoryResponse)

RobotResponse = _reflection.GeneratedProtocolMessageType('RobotResponse', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTRESPONSE,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.RobotResponse)
  ))
_sym_db.RegisterMessage(RobotResponse)

ErrorMessage = _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), dict(
  DESCRIPTOR = _ERRORMESSAGE,
  __module__ = 'robotapi_pb2'
  # @@protoc_insertion_point(class_scope:robominions.ErrorMessage)
  ))
_sym_db.RegisterMessage(ErrorMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036au.id.katharos.robominions.apiB\010RobotApi'))
_INVENTORYRESPONSE.fields_by_name['counts'].has_options = True
_INVENTORYRESPONSE.fields_by_name['counts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
