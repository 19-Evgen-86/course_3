from flask_restx import fields as flask_fields
from marshmallow import fields as marshmallow_fields

TYPE_MAPPING = {
    marshmallow_fields.Int: flask_fields.Integer,
    marshmallow_fields.Number: flask_fields.Integer,
    marshmallow_fields.String: flask_fields.String,
    marshmallow_fields.DateTime: flask_fields.DateTime,
    marshmallow_fields.Float: flask_fields.Float
}


def convert_model(schema):
    schema_fields = getattr(schema, "_declared_fields")
    converted_schema = {}

    for fields in schema_fields:
        if fields != "id":
            converted_schema[fields] = TYPE_MAPPING[type(schema_fields[fields])]

    return converted_schema
