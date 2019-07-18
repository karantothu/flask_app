from flask import Flask, redirect, url_for

gfam_api= Flask(__name__)

from gfam.routes.route import mod
from gfam.routes.dbroute import mod1

gfam_api.register_blueprint(mod, url_prefix='/api/v1.0')
gfam_api.register_blueprint(mod1, url_prefix='/api/v1.1')

