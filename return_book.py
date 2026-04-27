"""
return_book.py – Handle book returns and fine calculation
"""

from datetime import timedelta
from utils import books, issued_books, divider, book_id_from_title, date_today, compute_fine


def return_book():
    print("\n" + divider("═"))
    print("     RETURN A BOOK")
    print(divider("═"))

    # Collect all currently issued titles for display
    all_issued_bids = [bid for bid, recs in issued_books.items() if recs]

    if not all_issued_bids:
        print("\n   No books are currently issued out.")
        return

    print("\n  Currently issued books:\n")
    for bid in all_issued_bids:
        for rec in issued_books[bid]:
            due = rec["issue_date"] + timedelta(days=rec["days"])
            print(f"    • {books[bid]['title']}  →  {rec['student']}  (Due: {due})")

    print()
    title = input("    Enter Book Title to Return : ").strip()
    if not title:
        print("\n     Book title cannot be empty.")
        return

    bid = book_id_from_title(title)

    if bid not in issued_books or not issued_books[bid]:
        print(f"\n    '{title}' is not currently issued.")
        return

    student = input("    Student Name               : ").strip()
    if not student:
        print("\n     Student name cannot be empty.")
        return

    # Find the specific issue record for this student
    matching = [
        (i, rec) for i, rec in enumerate(issued_books[bid])
        if rec["student"].lower() == student.strip().lower()
    ]

    if not matching:
        print(f"\n    No record found for '{student.title()}' issuing '{books[bid]['title']}'.")
        return

    # If multiple records (same student issued same book twice), take the first
    idx, record = matching[0]
    today      = date_today()
    due_date   = record["issue_date"] + timedelta(days=record["days"])
    overdue_days = (today - due_date).days

    print(f"\n  {'─' * 48}")
    print(f"    Book       : {books[bid]['title']}")
    print(f"    Student    : {record['student']}")
    print(f"    Issued On  : {record['issue_date']}")
    print(f"     Due Date   : {due_date}")
    print(f"    Return Date: {today}")
    

    if overdue_days > 0:
        fine = compute_fine(overdue_days)
        print(f"\n     OVERDUE by {overdue_days} day(s)!")
        print(f"\n    Fine Breakdown:")
        _print_fine_breakdown(overdue_days)
        print(f"\n    TOTAL FINE DUE : ₹ {fine:.2f}")
        print(f"\n    Please collect the fine before completing the return.")
    else:
        days_early = abs(overdue_days)
        print(f"\n    Returned {'on time' if days_early == 0 else f'{days_early} day(s) early'}!  No fine applicable. 🎉")

    # Remove the record and put the book back
    issued_books[bid].pop(idx)
    print(f"\n    '{books[bid]['title']}' has been returned to the catalogue.")


def _print_fine_breakdown(overdue_days: int):
    """Print week-by-week fine breakdown."""
    from utils import BASE_FINE
    remaining = overdue_days
    week      = 1
    factorial = 1
    cumulative = 0.0

    while remaining > 0:
        factorial  *= week
        rate        = BASE_FINE * factorial
        days_in_wk  = min(remaining, 7)
        week_total  = rate * days_in_wk
        cumulative += week_total

        print(
            f"    Week {week}  ({days_in_wk} day{'s' if days_in_wk > 1 else ''} × ₹{rate}/day)"
            f"  =  ₹{week_total:.2f}"
        )
        remaining -= days_in_wk
        week      += 1
