class Book:
    def __init__(self, title, author, publication_year, borrowed=False):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = borrowed

    def borrow_book(self):
        self.borrowed = True

    def return_book(self):
        self.borrowed = False

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}, Borrowed: {self.borrowed}"

class LibraryMember:
    def __init__(self, member_id, name, borrowed_books=[]):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.borrow_book()

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()

    def display_info(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"
