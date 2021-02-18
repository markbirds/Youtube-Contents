from flask import Blueprint, render_template

api = Blueprint('api_blueprint',__name__,url_prefix='/api')

@api.route('/data')
def data():
  return {'key':'value'}
  