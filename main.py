"""

            LIBRARY MANAGEMENT SYSTEM                

"""

from add_books   import add_book
from show_books  import show_books
from issue_book  import issue_book
from return_book import return_book
from utils       import FINE_NOTICE, divider


def main_menu():
    print(divider("="))
    print("         LIBRARY MANAGEMENT SYSTEM")
    print(divider("="))
    print("  [1]    Add a Book")
    print("  [2]    View All Books")
    print("  [3]    Issue a Book")
    print("  [4]    Return a Book")
    print("  [5]    Fine / Charges Info")
    print("  [6]    Exit")
    


def library():

    print("   Welcome to the Library Management System!")
    

    while True:
        main_menu()
        choice = input("    Enter your choice (1-6): ").strip()
        if   choice == "1": add_book()
        elif choice == "2": show_books()
        elif choice == "3": issue_book()
        elif choice == "4": return_book()
        elif choice == "5": print(FINE_NOTICE)
        elif choice == "6":
            print("\n    Thank you for using the Library System. Goodbye!\n")
            break
        else:
            print("\n     Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    library()
