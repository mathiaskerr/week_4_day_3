from flask import Flask, render_template, request, redirect
from repositories import book_repository
from repositories import author_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def tasks():
    books = book_repository.select_all()
    return render_template('books/index.html', all_books = books)

@books_blueprint.route("/book/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("/books/new.html", all_authors = authors)

@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form['title']
    author_id = request.form["author_id"]
    genre = request.form['genre']
    author = author_repository.select(author_id)
    book = Book(title, author, genre)
    book_repository.save(book)
    return redirect(("/books"))

@books_blueprint.route("/book/<id>", methods=["GET"])
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", show_book = book)

@books_blueprint.route("/book/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
    # deleting only the top entry on webpage

@books_blueprint.route("/book/<id>/edit", methods= ["GET"])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", task = task, all_authors = authors)