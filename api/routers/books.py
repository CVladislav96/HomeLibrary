from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_login import login_required

from crud.book import *
from exceptions.exceptions import BookNotFoundException
from schemas.book import *


books_bp = Blueprint("books", __name__)


@books_bp.route("/", methods=["POST"])
@login_required
def create_book():
    try:
        data = request.get_json()
        book_data = BookCreate(**data)
        book = add_book_to_db(book_data)
        return jsonify(
            {"message": "Book created successfully", "book_id": book.id}
        ), HTTPStatus.CREATED  # 201
    except BookAlreadyExistsException:
        return jsonify({"error": "Book already exists"}), HTTPStatus.CONFLICT  # 409
    except ValueError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST  # 400
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR  # 500


@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        book = get_book_by_id_from_db(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), HTTPStatus.NOT_FOUND  # 404
        book_read = BookRead.model_validate(book)
        return jsonify(book_read.model_dump()), HTTPStatus.OK  # 200
    except ValueError:
        return jsonify({"error": "Invalid book ID"}), HTTPStatus.BAD_REQUEST  # 400
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR  # 500


@books_bp.route("/", methods=["GET"])
def get_all_books():
    try:
        books = get_all_books_from_db()
        return jsonify(
            [BookRead.model_validate(book).model_dump() for book in books]
        ), HTTPStatus.OK  # 200
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR  # 500


@books_bp.route("/<int:book_id>", methods=["PUT"])
@login_required
def update_book(book_id: int):
    try:
        data = request.get_json()
        book_data = BookUpdate(**data)
        update_book = update_book_in_db(book_id=book_id, book_data=book_data)
        if update_book is None:
            return jsonify({"error": "Book not found"}), HTTPStatus.NOT_FOUND  # 404
        return jsonify(
            BookRead.model_validate(update_book).model_dump()
        ), HTTPStatus.OK  # 200
    except BookNotFoundException as e:
        return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND  # 404
    except ValueError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST  # 400
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR  # 500


@books_bp.route("/<int:book_id>", methods=["DELETE"])
@login_required
def delete_book(book_id):
    try:
        book = get_book_by_id_from_db(book_id)
        if book is None:
            raise BookNotFoundException(f"Book with ID {book_id} not found")
        delete_book_from_db(book_id)
        return jsonify(
            {"message": "Book deleted successfully"}
        ), HTTPStatus.NO_CONTENT  # 204
    except ValueError:
        return jsonify({"error": "Invalid book ID"}), HTTPStatus.BAD_REQUEST  # 400
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR  # 500
