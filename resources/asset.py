from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt

from db import db
from models import AssetModel
from schemas import AssetsSchema, PlainAssetSchema
from sqlalchemy.exc import SQLAlchemyError

from passlib.hash import pbkdf2_sha256


blp = Blueprint("assets", __file__, description="Operations on assets."
)