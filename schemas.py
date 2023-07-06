from marshmallow import Schema, fields

class BusinessSchema(Schema):
    id: fields.Str(dump_only=True)
    businessName: fields.Str(required=True)
    phone: fields.Str(required=True)
    address: fields.Str(required=True)
    initialDate: fields.DateTime(required=True)
    declaredBilling: fields.Str(required=True)
    bankData: fields.List(fields.Nested(lambda: BankData()))

class BankData(Schema):
    agency = fields.Number(required=True)
    account = fields.Number(required=True)
    bank = fields.Str(required=True)
