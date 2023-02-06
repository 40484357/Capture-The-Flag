from webapp import create_app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)