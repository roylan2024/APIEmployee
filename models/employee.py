from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employees"

    emp_id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    mname = db.Column(db.String(80), unique=False, nullable=True)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    office =db.Column(db.String(255),nullable=False)
    designation =db.Column(db.String(80), nullable=False)
    date_hired = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(80),nullable=False)

    # Define a many-many relationship with subjects
    assets = db.relationship("AssetModel", back_populates="employees", secondary="asset_employee", cascade='all, delete')
    assets_employees = db.relationship('AssetEmployeeModel', back_populates='employee', overlaps="assets,employees")