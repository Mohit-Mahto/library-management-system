"""
issue_book.py – Issue a book to a student
"""

from datetime import timedelta
from utils import books, issued_books, divider, book_id_from_title, date_today, FINE_NOTICE


def issue_book():
    print("\n" + divider("═"))
    print("     ISSUE A BOOK")
    

    if not books:
        print("\n    No books available in the catalogue.")
        return

    # Show available books first
    print("\n  Available books:\n")
    available_books = []
    for bid, info in books.items():
        issued_count = sum(len(recs) for key, recs in issued_books.items() if key == bid)
        avail = info["copies"] - issued_count
        if avail > 0:
            available_books.append((bid, info, avail))
            print(f"    • {info['title']}  (by {info['author']})  — {avail} copy/copies available")

    if not available_books:
        print("\n    All books are currently issued out.")
        return

    print()
    title = input("    Enter Book Title to Issue : ").strip()
    if not title:
        print("\n     Book title cannot be empty.")
        return

    bid = book_id_from_title(title)
    if bid not in books:
        print(f"\n    '{title}' not found in the catalogue.")
        return

    issued_count = sum(len(recs) for key, recs in issued_books.items() if key == bid)
    if issued_count >= books[bid]["copies"]:
        print(f"\n   No available copy of '{books[bid]['title']}' at the moment.")
        return

    student = input("    Student Name             : ").strip()
    if not student:
        print("\n     Student name cannot be empty.")
        return

    days_str = input("    Issue Duration (days)    : ").strip()
    try:
        days = int(days_str)
        if days < 1:
            raise ValueError
    except ValueError:
        print("\n     Please enter a valid number of days (≥ 1).")
        return

    today   = date_today()
    due_date = today + timedelta(days=days)

    record = {
        "student"   : student.title(),
        "issue_date": today,
        "days"      : days,
    }

    issued_books.setdefault(bid, []).append(record)

    print("\n    Book issued successfully!")
    print(f"\n  {'─' * 45}")
    print(f"    Book     : {books[bid]['title']}")
    print(f"     Author   : {books[bid]['author']}")
    print(f"    Student  : {record['student']}")
    print(f"    Issued   : {today}")
    print(f"     Due Date  : {due_date}  ({days} days)")
    print(f"  {'─' * 45}")
    print(FINE_NOTICE)
