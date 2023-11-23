from marshmallow import Schema, fields
from marshmallow.validate import OneOf, Regexp, Email, Length


class ConfigSchema(Schema):
    SQLALCHEMY_DATABASE_URI = fields.String(
        required=True,
    )
