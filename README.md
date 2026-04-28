# 📚 Library Management System

A simple terminal-based Library Management System built in Python. Designed for managing a small library's day-to-day operations — no external dependencies required.

## Features

- Add books with title, author, and number of copies
- View the full catalogue with available vs. issued counts
- Issue books to students with name, date, and duration tracking
- Return books with automatic overdue detection and fine calculation
- Progressive fine system — fines increase week by week (₹10 → ₹20 → ₹60 → ...)

## Fine Structure

| Week | Rate per day |
|------|-------------|
| Week 1 | ₹10 |
| Week 2 | ₹20 |
| Week 3 | ₹60 |
| Week N | ₹10 × N! |

## Project Structure

```
library/
├── main.py          # Menu loop and entry point
├── utils.py         # Shared data store and fine engine
├── add_books.py     # Add books to the catalogue
├── show_books.py    # View all books
├── issue_book.py    # Issue a book to a student
└── return_book.py   # Return a book and calculate fines
```

## Getting Started

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
python main.py
```

> Requires Python 3.8+. No third-party packages needed.
