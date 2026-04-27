"""
utils.py – Shared data store and helper functions
"""

from datetime import datetime

# ── Book records ────────────────────────────────────────────────────
# books        : { book_id: { "title": str, "copies": int } }
# issued_books : { book_id: [ { "student": str, "issue_date": date,
#                               "days": int, "copy_id": str } ] }

books: dict[str, dict] = {}
issued_books: dict[str, list] = {}

# ── Fine structure ──────────────────────────────────────────────────
# Week 1  : ₹10  / day / book
# Week 2  : ₹20  / day / book  (10 × 2)
# Week 3  : ₹60  / day / book  (10 × 2 × 3)
# Week N  : base × factorial(n)

BASE_FINE = 10   # ₹ per day (week 1)


def compute_fine(overdue_days: int) -> float:
    """
    Calculate fine for overdue_days (days beyond the allotted period).
    Applies weekly multipliers: week k  →  BASE * k!
    """
    if overdue_days <= 0:
        return 0.0

    total_fine = 0.0
    remaining  = overdue_days
    week       = 1
    factorial  = 1

    while remaining > 0:
        factorial   *= week          # 1, 2, 6, 24 …
        rate         = BASE_FINE * factorial
        days_in_week = min(remaining, 7)
        total_fine  += rate * days_in_week
        remaining   -= days_in_week
        week        += 1

    return total_fine


def date_today() -> "datetime.date":
    return datetime.today().date()


def divider(char: str = "─", width: int = 58) -> str:
    return "  " + char * width


def book_id_from_title(title: str) -> str:
    return title.strip().upper()


FINE_NOTICE = """
  
                  FINE / LATE-RETURN CHARGES             
  
    Books must be returned within the allotted days.       
                                                            
    Overdue fine is calculated weekly:                      
                                                            
     • Week 1  (days  1 – 7)  : ₹ 10 / day / book         
     • Week 2  (days  8 – 14) : ₹ 20 / day / book         
     • Week 3  (days 15 – 21) : ₹ 60 / day / book         
     • Week 4  (days 22 – 28) : ₹240 / day / book         
     • Week N  →  ₹ 10 × N!  / day / book                 
                                                            
    Fine is charged on every overdue day, cumulative.      
  
"""
