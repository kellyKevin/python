
📜 Description
This repository contains various Python programs designed to showcase essential concepts and functionalities. Each program is beginner-friendly, making it an excellent resource for learning and reference.

🗂 Table of Contents
BankAccount Program
Circle Program
Product Management Functions
Library System
🏦 BankAccount Program
Description
A program that models a simple bank account with basic operations like depositing, withdrawing, checking balance, and retrieving customer details.

Features
Deposit: Add money to the account.
Withdraw: Withdraw money if the balance allows.
Check Balance: View the current balance.
Customer Details: Retrieve account holder information.
Usage
python
Copy
Edit
from bank_account import BankAccount

account = BankAccount("123456789", 1000, "2025-01-19", "John Doe")
account.deposit(500)
account.withdraw(200)
account.check_balance()
account.customer_details()
⚪ Circle Program
Description
A program to model a circle and provide methods to calculate its area and circumference.

Features
Get Area: Calculate the area of the circle.
Get Circumference: Calculate the circumference.
Usage
python
Copy
Edit
from circle import Circle

circle = Circle(5)
circle.getArea()
circle.getCircumference()
📦 Product Management Functions
Description
A set of functions to manage product information, such as adding products, updating prices, and adjusting quantities.

Features
Add Product: Create a new product with a name, price, and quantity.
Update Price: Update the price of an existing product.
Update Quantity: Adjust the quantity of an existing product.
Usage
python
Copy
Edit
from product_management import add_product, update_price, update_quantity

product = add_product("Laptop", 1000, 10)
update_price(product, 1200)
update_quantity(product, 5)
📚 Library System
Description
A program modeling a library system with classes for books and library members. It includes methods for borrowing and returning books and displaying information.

Features
Borrow Book: Borrow a book and update its status.
Return Book: Return a book and update its status.
Display Info: View information about books and members.
Usage
python
Copy
Edit
from library_system import Book, LibraryMember

book = Book("1984", "George Orwell", 1949)
member = LibraryMember("001", "Alice")
member.borrow_book(book)
member.return_book(book)
member.display_info()
🤝 Contributing
Fork this repository.
Submit pull requests for improvements or new programs.
Open an issue to discuss major changes or ideas.
