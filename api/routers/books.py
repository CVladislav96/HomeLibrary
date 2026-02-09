from flask import Blueprint, jsonify, request
from database.database import new_session
from models.book import BooksORM, StatusBook
from sqlalchemy import select

books_bp = Blueprint('books', __name__)


@books_bp.route('/', methods=['GET'])
def get_books():
    pass

@books_bp.route('/create', methods=['POST'])
def create_book():
    pass

@books_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    pass

@books_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    pass

@books_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    pass

