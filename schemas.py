from marshmallow import Schema, fields

class BusinessSchema(Schema):
    id = fields.Int(dump_only=True)
    businessName = fields.Str(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)
    registrationDate = fields.Date(required=True)
    billing = fields.Str(required=True)
    bankAccs = fields.List(fields.Nested(lambda: BankData()))


class BankData(Schema):
    id = fields.Int(dump_only=True)
    acc = fields.Int(required=True)
    agency = fields.Int(required=True)
    bank = fields.Str(required=True)
    business_id = fields.Int(required=True)

