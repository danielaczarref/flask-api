from marshmallow import Schema, fields

class CompanySchema(Schema):
    id                  = fields.Int(dump_only=True)
    companyName         = fields.Str(required=True)
    phone               = fields.Str(required=True)
    address             = fields.Str(required=True)
    registrationDate    = fields.Date(required=True)
    billing             = fields.Str(required=True)
    bankAccs            = fields.List(fields.Nested(lambda: BankAccSchema()))

class CompanyUpdateSchema(Schema):
    companyName         = fields.Str(required=True)
    phone               = fields.Str(required=True)
    address             = fields.Str(required=True)
    registrationDate    = fields.Date(required=True)
    billing             = fields.Str(required=True)

class BankAccSchema(Schema):
    id                  = fields.Int(dump_only=True)
    acc                 = fields.Int(required=True)
    agency              = fields.Int(required=True)
    bank                = fields.Str(required=True)
    company_id          = fields.Int(required=True)

