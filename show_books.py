"""
show_books.py – Display all books and issued status
"""

from utils import books, issued_books, divider


def show_books():
    print("     LIBRARY CATALOGUE")
  

    if not books:
        print("\n    No books have been added to the catalogue yet.")
        return

    # Header row
    print(f"\n  {'#':<4} {'TITLE':<30} {'AUTHOR':<20} {'TOTAL':>6} {'AVAIL':>6}")

    for idx, (bid, info) in enumerate(books.items(), start=1):
        issued_count = sum(
            len(records) for key, records in issued_books.items() if key == bid
        )
        available = info["copies"] - issued_count
        available_display = str(available) if available > 0 else "❌"

        print(
            f"  {idx:<4} {info['title']:<30} {info['author']:<20} "
            f"{info['copies']:>6} {available_display:>6}"
        )

    
    print(f"\n  Total unique titles: {len(books)}")

    # Show currently issued books
    all_issued = [(bid, rec) for bid, recs in issued_books.items() for rec in recs]
    if all_issued:
        print(f"\n  {'  CURRENTLY ISSUED BOOKS':}")
        print(f"\n  {'TITLE':<30} {'STUDENT':<20} {'ISSUED ON':<12} {'DUE ON':<12}")
        from datetime import timedelta
        for bid, rec in all_issued:
            due = rec["issue_date"] + timedelta(days=rec["days"])
            print(
                f"  {books[bid]['title']:<30} {rec['student']:<20} "
                f"{str(rec['issue_date']):<12} {str(due):<12}"
            )
