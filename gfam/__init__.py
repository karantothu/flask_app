from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from gfam import config

gfam_api = Flask(__name__)
gfam_api.config.from_object(config.Config)
db = SQLAlchemy(gfam_api)

from gfam.routes.route import mod
gfam_api.register_blueprint(mod)

