from src import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


class Note(db.Model):
  __tablename__ = 'notes'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  data = db.Column(db.String(10000))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  
class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  notes = db.relationship('Note')

  def check_password(self, password):
    print(f'HELLO::::{self.password, password}')

    if check_password_hash(self.password, password):
      print(f'HELLO::::{check_password_hash(self.password, password)}')
      return True
    else:
      return False


  @staticmethod
  def is_email_exist(email):
    ''' Returns either User object or None '''
    return User.query.filter_by(email=email).first()


  @staticmethod
  def new_user(email, firstName, password):
    user = User(email=email, 
                first_name=firstName,
                password=generate_password_hash(password, method='sha256'))
    try:
      db.session.add(user)
      db.session.commit()
    except IntegrityError:
      raise UserAlreadyExistsInDatabase

    return user

  
  @staticmethod
  def login(email, password):
    return User.query.filter_by(email=email, )

  
  @staticmethod
  def get_by_id(id):
    return User.query.get(id)