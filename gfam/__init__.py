from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

gfam_api= Flask(__name__)
db = SQLAlchemy(gfam_api)

from gfam.routes.route import mod
from gfam.routes.route1 import mod1

gfam_api.register_blueprint(mod, url_prefix='/api/v1.0')
gfam_api.register_blueprint(mod1, url_prefix='/api/v1.1')

