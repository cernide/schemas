# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from marshmallow import Schema, fields, post_load
from marshmallow.utils import utc

from polyaxon_schemas.base import BaseConfig
from polyaxon_schemas.utils import TIME_ZONE


class DataDetailsSchema(Schema):
    state = fields.Str()
    size = fields.Float()
    uri = fields.Url()

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return DataDetailsConfig(**data)


class DataDetailsConfig(BaseConfig):
    SCHEMA = DataDetailsSchema
    IDENTIFIER = 'data_details'

    def __init__(self, state, size, uri):
        self.state = state
        self.size = size
        self.uri = uri


class DataSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    created_at = fields.DateTime()
    description = fields.Str(allow_none=True)
    details = fields.Nested(DataDetailsSchema)
    version = fields.Str(allow_none=True)
    resource_id = fields.Str(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make_data(self, data):
        return DataConfig(**data)


class DataConfig(BaseConfig):
    SCHEMA = DataSchema
    IDENTIFIER = 'data'

    def __init__(self, id, name, created_at, description, details, version=None, resource_id=None):
        self.id = id
        self.name = name
        self.created_at = self.localize_date(created_at)
        self.description = description
        self.details = details
        self.version = int(float(version)) if version else None
        self.resource_id = resource_id

    @staticmethod
    def localize_date(dt):
        if not dt.tzinfo:
            dt = utc.localize(dt)
        return dt.astimezone(TIME_ZONE)


class DatasetSchema(Schema):
    name = fields.Str()
    id = fields.Str()
    description = fields.Str(allow_none=True)
    is_public = fields.Boolean()

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return DatasetConfig(**data)


class DatasetConfig(BaseConfig):
    SCHEMA = DatasetSchema
    IDENTIFIER = 'dataset'

    def __init__(self, name, id, description, is_public):
        self.name = name
        self.id = id
        self.description = description
        self.is_public = is_public
