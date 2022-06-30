import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
  app = Flask(__name__)

  uri = os.getenv('DATABASE_URL')

  if uri.startswith("postgres://"):
      uri = uri.replace("postgres://", "postgresql://", 1)

  app.config["SQLALCHEMY_DATABASE_URI"] = uri
  app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

  db.init_app(app)

  from src.views.main import main
  from src.views.auth import auth
  app.register_blueprint(main, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')

  from src.models.user import User, Note
  db.create_all(app=app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.get_by_id(int(id))

  return app