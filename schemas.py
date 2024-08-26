from marshmallow import Schema,fields



class PlainEmployeeSchema(Schema):
    emp_id = fields.Int(dump_only=True)
    fname = fields.Str(required=True)
    mname = fields.Str(required=False)
    lname = fields.Str(required=True)
    office = fields.Str(required=True)
    designation = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    date_hired = fields.Str(required=True)
    status = fields.Str(required=True)
    
    
class EmployeeLoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PlainAssetSchema(Schema):
    asset_id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    asset_type = fields.Str(required=True)
    description = fields.Str(required=True)
    serial =fields.Str(required=True)
    delivery_type =fields.Str(required=True)
    date_received =fields.Str(required=True)
    price = fields.Float(required=True)
    status =fields.Str(required=True)
    
class EmployeeSchema(Schema):
    assets = fields.List(fields.Nested(PlainAssetSchema()),dump_only=True) 
    
class AssetsSchema(Schema):
    employees = fields.List(fields.Nested(PlainEmployeeSchema()),dump_only=True) 
    


class AssetandEmployeeSchema(Schema):
    message = fields.Str()
    employee = fields.Nested(EmployeeSchema())
    asset = fields.Nested(AssetsSchema())    
    

    