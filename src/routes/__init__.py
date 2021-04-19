from flask import Blueprint

hello = Blueprint('routes', __name__)

from . import routes
