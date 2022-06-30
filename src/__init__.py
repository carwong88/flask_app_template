import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
# DB_NAME = 'expense_tracker.db'

# print(os.environ['DB_USERNAME'])

def create_app():
  app = Flask(__name__)

  db_username = os.environ['DB_USERNAME']
  db_password = os.environ['DB_PASSWORD']
  db_host = os.environ['DB_HOST']
  db_database = os.environ['DB_DATABASE']
  secret_key = os.environ['FLASK_SECRET_KEY']

  app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_database}'
  app.config['SECRET_KEY'] = secret_key

  db.init_app(app)

  from .views.main import main
  from .views.auth import auth
  app.register_blueprint(main, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')

  from .models.user import User, Note
  db.create_all(app=app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.get_by_id(int(id))

  return app