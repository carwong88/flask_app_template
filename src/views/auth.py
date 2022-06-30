from flask import Blueprint, render_template, request, flash, redirect, url_for
from src.forms.user import RegistrationForm, LoginForm
from src.models.user import User

from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('logout')
def logout():
  logout_user()
  return redirect(url_for('auth.login'))


@auth.route('/')
@auth.route('login', methods=['GET', 'POST'])
def login():
  form = LoginForm(request.form)

  if request.method == 'POST':
    email = form.email.data
    password = form.password.data

    user = User.is_email_exist(email)

    if user:
      if user.check_password(password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('main.index'))
      else:
        flash('Incorrect password, please try again.', category='error')
    else:
      flash('Email does not exist. Please sign up.', category='error')
      return redirect(url_for('auth.sign_up'))

  return render_template('login.html', title='Login', form=form)


@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
  form = RegistrationForm(request.form)
  print(form)

  if request.method == 'POST' and form.validate():
    email = form.email.data
    firstName = form.firstName.data
    password = form.password.data
    confirmPassword = form.confirmPassword.data

    if User.is_email_exist(email):
      flash(f'User "{email}" is already exists. Please log in instead.', 'error')
      return redirect(url_for('auth.login'))
    else: 
      user = User.new_user(email, firstName, password)
      flash('Thanks for signing up!', 'success')   
      login_user(user, remember=True) 
      return redirect(url_for('main.index'))
        
  return render_template('sign_up.html', title='Sign Up', form=form)
