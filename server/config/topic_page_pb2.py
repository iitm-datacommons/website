# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: topic_page.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='topic_page.proto',
  package='datacommons',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10topic_page.proto\x12\x0b\x64\x61tacommons\"\xd7\x01\n\x0cPageMetadata\x12\x10\n\x08topic_id\x18\x01 \x01(\t\x12\x12\n\ntopic_name\x18\x02 \x01(\t\x12\x12\n\nplace_dcid\x18\x03 \x03(\t\x12Q\n\x15\x63ontained_place_types\x18\x04 \x03(\x0b\x32\x32.datacommons.PageMetadata.ContainedPlaceTypesEntry\x1a:\n\x18\x43ontainedPlaceTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"l\n\x0fStatVarMetadata\x12\x10\n\x08stat_var\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x0f\n\x07scaling\x18\x04 \x01(\x01\x12\x0b\n\x03log\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\"\xdf\x01\n\x0fRankingMetadata\x12\x14\n\x0cshow_highest\x18\x01 \x01(\x08\x12\x13\n\x0bshow_lowest\x18\x02 \x01(\x08\x12\x15\n\rshow_increase\x18\x03 \x01(\x08\x12\x15\n\rshow_decrease\x18\x04 \x01(\x08\x12\x16\n\x0e\x64iff_base_date\x18\x05 \x01(\t\x12\x15\n\rhighest_title\x18\x06 \x01(\t\x12\x14\n\x0clowest_title\x18\x07 \x01(\t\x12\x16\n\x0eincrease_title\x18\x08 \x01(\t\x12\x16\n\x0e\x64\x65\x63rease_title\x18\t \x01(\t\"\xa9\x03\n\x04Tile\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x04type\x18\x03 \x01(\x0e\x32\x1a.datacommons.Tile.TileType\x12\x14\n\x0cstat_var_key\x18\x04 \x03(\t\x12\x36\n\x10ranking_metadata\x18\x05 \x01(\x0b\x32\x1c.datacommons.RankingMetadata\x12I\n\x15\x63ontained_place_types\x18\x07 \x03(\x0b\x32*.datacommons.Tile.ContainedPlaceTypesEntry\x1a:\n\x18\x43ontainedPlaceTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"~\n\x08TileType\x12\r\n\tTYPE_NONE\x10\x00\x12\x08\n\x04LINE\x10\x01\x12\x07\n\x03\x42\x41R\x10\x02\x12\x07\n\x03MAP\x10\x03\x12\x0b\n\x07SCATTER\x10\x04\x12\r\n\tBIVARIATE\x10\x05\x12\x0b\n\x07RANKING\x10\x06\x12\r\n\tHIGHLIGHT\x10\x07\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x08\"z\n\x05\x42lock\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12%\n\nleft_tiles\x18\x03 \x03(\x0b\x32\x11.datacommons.Tile\x12&\n\x0bright_tiles\x18\x04 \x03(\x0b\x32\x11.datacommons.Tile\"\xef\x01\n\x08\x43\x61tegory\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x45\n\x11stat_var_metadata\x18\x04 \x03(\x0b\x32*.datacommons.Category.StatVarMetadataEntry\x12\"\n\x06\x62locks\x18\x03 \x03(\x0b\x32\x12.datacommons.Block\x1aT\n\x14StatVarMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.datacommons.StatVarMetadata:\x02\x38\x01\"i\n\x0fTopicPageConfig\x12+\n\x08metadata\x18\x01 \x01(\x0b\x32\x19.datacommons.PageMetadata\x12)\n\ncategories\x18\x02 \x03(\x0b\x32\x15.datacommons.Categoryb\x06proto3')
)



_TILE_TILETYPE = _descriptor.EnumDescriptor(
  name='TileType',
  full_name='datacommons.Tile.TileType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCATTER', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIVARIATE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANKING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGHLIGHT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=887,
  serialized_end=1013,
)
_sym_db.RegisterEnumDescriptor(_TILE_TILETYPE)


_PAGEMETADATA_CONTAINEDPLACETYPESENTRY = _descriptor.Descriptor(
  name='ContainedPlaceTypesEntry',
  full_name='datacommons.PageMetadata.ContainedPlaceTypesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='datacommons.PageMetadata.ContainedPlaceTypesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='datacommons.PageMetadata.ContainedPlaceTypesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=249,
)

_PAGEMETADATA = _descriptor.Descriptor(
  name='PageMetadata',
  full_name='datacommons.PageMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_id', full_name='datacommons.PageMetadata.topic_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic_name', full_name='datacommons.PageMetadata.topic_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='place_dcid', full_name='datacommons.PageMetadata.place_dcid', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contained_place_types', full_name='datacommons.PageMetadata.contained_place_types', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PAGEMETADATA_CONTAINEDPLACETYPESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=249,
)


_STATVARMETADATA = _descriptor.Descriptor(
  name='StatVarMetadata',
  full_name='datacommons.StatVarMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stat_var', full_name='datacommons.StatVarMetadata.stat_var', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denom', full_name='datacommons.StatVarMetadata.denom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='datacommons.StatVarMetadata.unit', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scaling', full_name='datacommons.StatVarMetadata.scaling', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='datacommons.StatVarMetadata.log', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='datacommons.StatVarMetadata.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=251,
  serialized_end=359,
)


_RANKINGMETADATA = _descriptor.Descriptor(
  name='RankingMetadata',
  full_name='datacommons.RankingMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='show_highest', full_name='datacommons.RankingMetadata.show_highest', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_lowest', full_name='datacommons.RankingMetadata.show_lowest', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_increase', full_name='datacommons.RankingMetadata.show_increase', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_decrease', full_name='datacommons.RankingMetadata.show_decrease', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diff_base_date', full_name='datacommons.RankingMetadata.diff_base_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='highest_title', full_name='datacommons.RankingMetadata.highest_title', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lowest_title', full_name='datacommons.RankingMetadata.lowest_title', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='increase_title', full_name='datacommons.RankingMetadata.increase_title', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decrease_title', full_name='datacommons.RankingMetadata.decrease_title', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=362,
  serialized_end=585,
)


_TILE_CONTAINEDPLACETYPESENTRY = _descriptor.Descriptor(
  name='ContainedPlaceTypesEntry',
  full_name='datacommons.Tile.ContainedPlaceTypesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='datacommons.Tile.ContainedPlaceTypesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='datacommons.Tile.ContainedPlaceTypesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=249,
)

_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='datacommons.Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='datacommons.Tile.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='datacommons.Tile.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='datacommons.Tile.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stat_var_key', full_name='datacommons.Tile.stat_var_key', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranking_metadata', full_name='datacommons.Tile.ranking_metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contained_place_types', full_name='datacommons.Tile.contained_place_types', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TILE_CONTAINEDPLACETYPESENTRY, ],
  enum_types=[
    _TILE_TILETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=1013,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='datacommons.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='datacommons.Block.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='datacommons.Block.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_tiles', full_name='datacommons.Block.left_tiles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_tiles', full_name='datacommons.Block.right_tiles', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1015,
  serialized_end=1137,
)


_CATEGORY_STATVARMETADATAENTRY = _descriptor.Descriptor(
  name='StatVarMetadataEntry',
  full_name='datacommons.Category.StatVarMetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='datacommons.Category.StatVarMetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='datacommons.Category.StatVarMetadataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1295,
  serialized_end=1379,
)

_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='datacommons.Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='datacommons.Category.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='datacommons.Category.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stat_var_metadata', full_name='datacommons.Category.stat_var_metadata', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='datacommons.Category.blocks', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CATEGORY_STATVARMETADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1140,
  serialized_end=1379,
)


_TOPICPAGECONFIG = _descriptor.Descriptor(
  name='TopicPageConfig',
  full_name='datacommons.TopicPageConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='datacommons.TopicPageConfig.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categories', full_name='datacommons.TopicPageConfig.categories', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1381,
  serialized_end=1486,
)

_PAGEMETADATA_CONTAINEDPLACETYPESENTRY.containing_type = _PAGEMETADATA
_PAGEMETADATA.fields_by_name['contained_place_types'].message_type = _PAGEMETADATA_CONTAINEDPLACETYPESENTRY
_TILE_CONTAINEDPLACETYPESENTRY.containing_type = _TILE
_TILE.fields_by_name['type'].enum_type = _TILE_TILETYPE
_TILE.fields_by_name['ranking_metadata'].message_type = _RANKINGMETADATA
_TILE.fields_by_name['contained_place_types'].message_type = _TILE_CONTAINEDPLACETYPESENTRY
_TILE_TILETYPE.containing_type = _TILE
_BLOCK.fields_by_name['left_tiles'].message_type = _TILE
_BLOCK.fields_by_name['right_tiles'].message_type = _TILE
_CATEGORY_STATVARMETADATAENTRY.fields_by_name['value'].message_type = _STATVARMETADATA
_CATEGORY_STATVARMETADATAENTRY.containing_type = _CATEGORY
_CATEGORY.fields_by_name['stat_var_metadata'].message_type = _CATEGORY_STATVARMETADATAENTRY
_CATEGORY.fields_by_name['blocks'].message_type = _BLOCK
_TOPICPAGECONFIG.fields_by_name['metadata'].message_type = _PAGEMETADATA
_TOPICPAGECONFIG.fields_by_name['categories'].message_type = _CATEGORY
DESCRIPTOR.message_types_by_name['PageMetadata'] = _PAGEMETADATA
DESCRIPTOR.message_types_by_name['StatVarMetadata'] = _STATVARMETADATA
DESCRIPTOR.message_types_by_name['RankingMetadata'] = _RANKINGMETADATA
DESCRIPTOR.message_types_by_name['Tile'] = _TILE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.message_types_by_name['TopicPageConfig'] = _TOPICPAGECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageMetadata = _reflection.GeneratedProtocolMessageType('PageMetadata', (_message.Message,), dict(

  ContainedPlaceTypesEntry = _reflection.GeneratedProtocolMessageType('ContainedPlaceTypesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PAGEMETADATA_CONTAINEDPLACETYPESENTRY,
    __module__ = 'topic_page_pb2'
    # @@protoc_insertion_point(class_scope:datacommons.PageMetadata.ContainedPlaceTypesEntry)
    ))
  ,
  DESCRIPTOR = _PAGEMETADATA,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.PageMetadata)
  ))
_sym_db.RegisterMessage(PageMetadata)
_sym_db.RegisterMessage(PageMetadata.ContainedPlaceTypesEntry)

StatVarMetadata = _reflection.GeneratedProtocolMessageType('StatVarMetadata', (_message.Message,), dict(
  DESCRIPTOR = _STATVARMETADATA,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.StatVarMetadata)
  ))
_sym_db.RegisterMessage(StatVarMetadata)

RankingMetadata = _reflection.GeneratedProtocolMessageType('RankingMetadata', (_message.Message,), dict(
  DESCRIPTOR = _RANKINGMETADATA,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.RankingMetadata)
  ))
_sym_db.RegisterMessage(RankingMetadata)

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), dict(

  ContainedPlaceTypesEntry = _reflection.GeneratedProtocolMessageType('ContainedPlaceTypesEntry', (_message.Message,), dict(
    DESCRIPTOR = _TILE_CONTAINEDPLACETYPESENTRY,
    __module__ = 'topic_page_pb2'
    # @@protoc_insertion_point(class_scope:datacommons.Tile.ContainedPlaceTypesEntry)
    ))
  ,
  DESCRIPTOR = _TILE,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.Tile)
  ))
_sym_db.RegisterMessage(Tile)
_sym_db.RegisterMessage(Tile.ContainedPlaceTypesEntry)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.Block)
  ))
_sym_db.RegisterMessage(Block)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), dict(

  StatVarMetadataEntry = _reflection.GeneratedProtocolMessageType('StatVarMetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _CATEGORY_STATVARMETADATAENTRY,
    __module__ = 'topic_page_pb2'
    # @@protoc_insertion_point(class_scope:datacommons.Category.StatVarMetadataEntry)
    ))
  ,
  DESCRIPTOR = _CATEGORY,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.Category)
  ))
_sym_db.RegisterMessage(Category)
_sym_db.RegisterMessage(Category.StatVarMetadataEntry)

TopicPageConfig = _reflection.GeneratedProtocolMessageType('TopicPageConfig', (_message.Message,), dict(
  DESCRIPTOR = _TOPICPAGECONFIG,
  __module__ = 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.TopicPageConfig)
  ))
_sym_db.RegisterMessage(TopicPageConfig)


_PAGEMETADATA_CONTAINEDPLACETYPESENTRY._options = None
_TILE_CONTAINEDPLACETYPESENTRY._options = None
_CATEGORY_STATVARMETADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
