from flask import Blueprint, render_template

site = Blueprint('site_blueprint',__name__)

@site.route('/')
def index():
  return render_template('index.html')