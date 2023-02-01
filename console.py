import pdb
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

# book_repository.delete_all()
# author_repository.delete_all()

author_1 = Author("Brandon Sanderson")
book_1 = Book("Mistborn", author_1, "High Fantasy")
author_2 = Author("Randolf lam")
book_2 = Book ("Python is Life", author_2, "computers")


author_repository.save(author_1)
author_repository.save(author_2)
# result = author_repository.select_all()

# results = author_repository.select(7)
book_repository.save(book_1)
book_repository.save(book_2)
# book_repository.select_all()
# result = book_repository.select(3)

pdb.set_trace()