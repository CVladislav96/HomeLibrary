from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database.config import settings
from database.database import engine
from models.book import Base
from api.routers.books import books_bp


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = settings.DEBUG

db = SQLAlchemy(app)

with app.app_context():
    Base.metadata.create_all(bind=engine)

app.register_blueprint(books_bp, url_prefix='/api/books')     



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host='0.0.0.0', port=5000)

