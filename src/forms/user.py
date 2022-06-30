from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=35)])

    firstName = StringField('First Name', [
        validators.Length(min=3, max=25)])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirmPassword', message='Passwords must match')])

    confirmPassword = PasswordField('Repeat Password')


class LoginForm(Form):
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=35)])

    password = PasswordField('Password', [
        validators.DataRequired()])
    

