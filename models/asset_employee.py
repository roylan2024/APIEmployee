from db import db

class AssetEmployeeModel(db.Model):
    __tablename__ = "asset_employee"

    id = db.Column(db.Integer, primary_key = True)
    emp_id = db.Column(db.Integer, db.ForeignKey("employees.emp_id"))
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.asset_id"))

   
    # Add a new relationship to provide us with a subject and student
    employee = db.relationship('EmployeeModel', back_populates='assets_employees', overlaps="assets,employees")
    asset = db.relationship('AssetModel', back_populates='assets_employees', overlaps="employees,assets")

    