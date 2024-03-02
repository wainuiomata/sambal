from wtforms import Form, PasswordField, StringField, SubmitField, validators


class LoginForm(Form):
    host = StringField("Host", [validators.DataRequired()])
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    realm = StringField("Realm")
    login = SubmitField("Log in")
