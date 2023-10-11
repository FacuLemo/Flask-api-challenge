from app import ma
from marshmallow import fields


class UserBasicSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email= fields.String()
    password= fields.String()
    image=fields.Integer()

"""
class PaisBasicSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()

class ProvinciaBasicSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    pais_obj= fields.Nested(PaisBasicSchema, exclude=('id',)) #para no tener el pais id 2 vece
    pais = fields.Integer(dump_only=True)

class LocalidadBasicSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    provincia_obj= fields.Nested(ProvinciaBasicSchema, exclude=('id',)) #para no tener el pais id 2 vece
    provincia = fields.Integer(dump_only=True)
    """