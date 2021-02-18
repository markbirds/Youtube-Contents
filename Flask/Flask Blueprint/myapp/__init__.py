from flask import Flask
from .site.routes import site
from .api.routes import api

def create_app():
  app = Flask(__name__)

  app.register_blueprint(site)
  app.register_blueprint(api)
  return app