from functools import wraps
from flask import request, jsonify, abort
import os

from app.accounts.models.hotel import *
from app.accounts.models.user import *

from app.accounts.dao import user_dao, hotel_dao

from app.accounts import accounts