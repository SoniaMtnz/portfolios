from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
# from flask_bootstrap import Bootstrap5
# from flask_ckeditor import CKEditor
# from flask_gravatar import Gravatar
# from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
# from forms import CreatePostForm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

