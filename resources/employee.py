from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt

from db import db
from models import EmployeeModel
from schemas import EmployeeSchema, PlainEmployeeSchema
from sqlalchemy.exc import SQLAlchemyError

from passlib.hash import pbkdf2_sha256


blp = Blueprint("employees", __file__, description="Operations on employees."
)
