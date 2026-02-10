from flask import Flask, jsonify
from database.config import settings
from models import Base
from database.database import engine, new_session
from models.book import BooksORM
from api.routers.books import books_bp
from utils.database import wait_for_database

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = settings.DEBUG

if not wait_for_database():
    raise Exception("Database is not available")

with app.app_context():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")

app.register_blueprint(books_bp, url_prefix='/api/books')     



@app.route('/')
def index():
    return jsonify({'message': 'HomeLibrary API is running'})

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host='0.0.0.0', port=5000)

