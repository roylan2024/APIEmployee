from db import db

class AssetModel(db.Model):
    __tablename__ = "assets"

    asset_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    asset_type = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String,nullable=False)
    serial_number = db.Column(db.String(200), unique=True, nullable=False)
    type_of_delivery = db.Column(db.String(80),nullable=False)
    date_recieved =db.Column(db.String(200),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    status = db.Column(db.String(50),nullable=False)

    # Define a many-many relationship with students
    employees = db.relationship("EmployeetModel", back_populates="assets", secondary="asset_employee", cascade='all, delete')

    assets_employees = db.relationship('AssetEmployeeModel', back_populates='asset', overlaps="employees,assets")

    