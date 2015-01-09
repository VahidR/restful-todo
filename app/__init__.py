from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flaskext.markdown import Markdown
from flask.ext.pagedown import PageDown
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  bootstrap.init_app(app)
  moment.init_app(app)
  db.init_app(app)
  pagedown.init_app(app)

  Markdown(app)

  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
