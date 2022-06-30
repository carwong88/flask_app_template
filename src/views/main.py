from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@login_required
def index():
  return render_template('index.html', title='Home')