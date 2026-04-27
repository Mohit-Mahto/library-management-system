"""
add_books.py – Add books to the library catalogue
"""

from utils import books, divider, book_id_from_title


def add_book():
    print("\n" + divider("═"))
    print("     ADD A BOOK TO THE CATALOGUE")

    title   = input("\n    Enter Book Title      : ").strip()
    if not title:
        print("\n     Book title cannot be empty.")
        return

    author  = input("     Enter Author Name      : ").strip() or "Unknown"
    copies_str = input("    Number of Copies       : ").strip()

    try:
        copies = int(copies_str)
        if copies < 1:
            raise ValueError
    except ValueError:
        print("\n     Invalid number of copies. Please enter a positive integer.")
        return

    bid = book_id_from_title(title)

    if bid in books:
        books[bid]["copies"] += copies
        print(f"\n    '{title}' already exists. Added {copies} more copy/copies.")
        print(f"      Total copies now: {books[bid]['copies']}")
    else:
        books[bid] = {
            "title" : title.title(),
            "author": author.title(),
            "copies": copies,
        }
        print(f"\n    Book added successfully!")
        print(f"      Title   : {books[bid]['title']}")
        print(f"      Author  : {books[bid]['author']}")
        print(f"      Copies  : {copies}")
