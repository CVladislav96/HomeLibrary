from flask import Flask, jsonify, send_from_directory
from auth import google_auth
from database.config import settings
from models import Base
from database.database import engine, new_session
from models.book import BooksORM
from api.routers.books import books_bp
from utils.database import wait_for_database
from flask_login import LoginManager, current_user, login_required
from auth.routes import auth_bp
from auth.login_manager import init_login_manager
from auth.google_auth import init_oauth
import os

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = settings.DEBUG
app.config['GOOGLE_CLIENT_ID'] = settings.GOOGLE_CLIENT_ID
app.config['GOOGLE_CLIENT_SECRET'] = settings.GOOGLE_CLIENT_SECRET
app.config['SECRET_KEY'] = settings.SECRET_KEY

login_manager = init_login_manager(app)
google_auth = init_oauth(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

if not wait_for_database():
    raise Exception("Database is not available")

with app.app_context():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")

app.register_blueprint(books_bp, url_prefix='/api/books')     


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/profile')
@login_required
def profile():
    from flask import render_template
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host='0.0.0.0', port=5000)

