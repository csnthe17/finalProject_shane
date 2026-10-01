library_items = []

import datetime

x = datetime.datetime.now()
currentYear = x.year


class LibraryItem:
    def __init__(self, item_id, title, category, publication_year, is_borrowed=False):
        self.item_id = item_id
        self.title = title
        self.category = category
        self.publication_year = publication_year
        self.is_borrowed = is_borrowed

    def calculate_late_fee(self, days_late):
        return 0


class Book(LibraryItem):
    def __init__(self, item_id, title, category, publication_year, is_borrowed, author):
        super().__init__(
            item_id,
            title,
            category,
            publication_year,
            is_borrowed
        )
        self.author = author

    def get_type(self):
        return "Book"

    def calculate_late_fee(self, days_late):
        fee = days_late * 2000

        if days_late > 7:
            fee += 10000

        return fee


class Magazine(LibraryItem):
    def __init__(self, item_id, title, category, publication_year, is_borrowed, issue_number):
        super().__init__(
            item_id,
            title,
            category,
            publication_year,
            is_borrowed
        )
        self.issue_number = issue_number

    def get_type(self):
        return "Magazine"

    def calculate_late_fee(self, days_late):
        fee = days_late * 3000

        if days_late > 5:
            fee += 15000

        return fee


def checkExistingItemID(item_id):
    for item in library_items:
        if item.item_id.lower() == item_id.lower():
            return True

    return False

def print_item(item, item_number=None):

    if item_number is not None:
        print(f"Item # {item_number}")

    print(f"ID               : {item.item_id}")
    print(f"Title            : {item.title}")
    print(f"Category         : {item.category}")
    print(f"Publication Year : {item.publication_year}")

    if item.get_type() == "Book":
        print("Type             : Book")
        print(f"Author           : {item.author}")

    elif item.get_type() == "Magazine":
        print("Type             : Magazine")
        print(f"Issue Number     : {item.issue_number}")

    if item.is_borrowed:
        status = "Borrowed"
    else:
        status = "Available"

    print(f"Status           : {status}")
    print("---------------------------------------------")



def add_item():
  while True:
    print("\n===== Add Library Item =====")
    print("1. Book")
    print("2. Magazine")
    print("3. Back To Main Menu")

    while True:
        item_type = input("Choose Type [1/2/3] : ").strip()
        if item_type == "":
            print("Please enter 1-3")
            continue
        if item_type not in ["1", "2", "3"]:
            print("Please choose 1-3 only")
            continue
        break

    if item_type == "3":
        return

    if item_type == "1":
       Activelayer = "===== Add Book ====="  
       HeadId="BK"
    elif item_type == "2":
       Activelayer = "===== Add Magazine ====="  
       HeadId="MG"
 
    print(f"\n{Activelayer}")
    while True:
     temp_id = input(f"Item ID            : {HeadId}").strip()
     if temp_id == "":
        print("ID cannot be empty")
        continue
     item_id = HeadId + temp_id
     if checkExistingItemID(item_id):
        print(f"ID '{item_id}' already exists")
        continue
     break
    while True:
     title=input("Title              : ").strip()
     if title =="":
       print("Title cannot be empty")
       continue
     break
    while True:    
     category=input("Category              : ").strip()
     if category =="":
        print("Category cannot be empty")
        continue
     break
    while True:
     pub_year = input("Publication Year   : ").strip()
     if pub_year == "":
        print("Publication Year cannot be empty")
        continue
     if not pub_year.isdigit():
        print("Publication Year must be a number")
        continue
     pub_year = int(pub_year)
     if pub_year > currentYear:
        print(f"Invalid Year, must be <= {currentYear}")
        continue
     if pub_year <= 0:
        print("Invalid Year")
        continue
     break

    if item_type == "1":
        while True:
         author=input("Author              : ").strip()
         if author =="":
            print("Author cannot be empty")
            continue
         break

        book = Book(
            item_id,
            title,
            category,
            pub_year,
            False,
            author
        )
        library_items.append(book)
        print("Book added successfully!")

    elif item_type == "2":
        while True:
         issue_number  = input("Issue Number       : ").strip()
         if issue_number == "":
            print("issue_number cannot be empty")
            continue
         if not issue_number.isdigit():
            print("Issue Number must be a number")
            continue
         issue_number = int(issue_number)
         if issue_number <= 0:
            print("Issue Number must be greater than 0")
            continue
         break
        
        magazine = Magazine(
            item_id,
            title,
            category,
            pub_year,
            False,
            issue_number
        )
        library_items.append(magazine)
        print("Magazine added successfully!")

def show_all_items():
  while True:
    if not library_items:
        print("No Items yet")
    else :
      print("\n==== LIBRARY ITEMS ====")
      totalitem = 1
    
      for item in library_items:

        if item.get_type() == "Book":

            print_item(item, totalitem)

            totalitem += 1

      for item in library_items:

        if item.get_type() == "Magazine":

            print_item(item, totalitem)

            totalitem += 1

      print(f"Total Items : {len(library_items)}")
    
    print("\n1. Show again?")
    print("2. Back To Main Menu")
    choose=input ("Choose 1/2 : ").strip()
    if choose =="2" :
        return
       
    

def find_item():
  while True:
    keyword = input("Enter Item ID /Title : ").strip().lower()

    if keyword == "":
        print("Item ID or Title cannot be empty")
        continue

    found = False

    for item in library_items:

        if keyword in item.title.lower() or keyword in item.item_id.lower():

            print_item(item)

            found = True

    if not found:
        print("Item not found")

    print("\n 1. Find again?")
    print("2. Back To Main Menu")
    choose=input ("Choose 1/2 : ").strip()
    if choose =="2" :
        return


def borrow_item():
    print("\n===== Borrow Item =====")
    print("You must borrow at least 5 items- at least 2 Books and 2 Magazines.")
    print("Type '0' to CANCEL borrowing")

    while True:
        borrowed_items = []
        book_count = 0
        magazine_count = 0
        is_cancelled = False

        while len(borrowed_items) < 5:
            print(f"\nItem {len(borrowed_items) + 1} of 5")
            item_id = input("Enter Item ID to borrow (0 to cancel): ").strip()

            if item_id == "0":
                print("\nBorrow cancelled! All selections cleared.")
                is_cancelled = True
                break

            if item_id == "":
                print("Item ID cannot be empty")
                continue

            found_item = None
            for item in library_items:
                if item.item_id.lower() == item_id.lower():
                    found_item = item
                    break

            if found_item is None:
                print("Item not found")
                continue
            if found_item.is_borrowed:
                print("This item is already borrowed")
                continue
            if found_item in borrowed_items:
                print("This item has already been selected")
                continue

            borrowed_items.append(found_item)
            if found_item.get_type() == "Book":
                book_count += 1
            else:
                magazine_count += 1

            print(f"'{found_item.title}' added")
            print(f"Book : {book_count} | Magazine : {magazine_count}")

        if is_cancelled:
            return  

        if len(borrowed_items) != 5 or book_count < 2 or magazine_count < 2:
            print("\nYou must borrow at least 5 items- at least 2 Books and 2 Magazines.")
            print(f"Books : {book_count} | Magazines : {magazine_count}")
            print("Please enter the items again.")
            continue
        break

    for item in borrowed_items:
        item.is_borrowed = True

    print("\n===== Borrowing Summary =====")
    for item in borrowed_items:
        print(f"{item.get_type()} - {item.title}")
    print(f"\nTotal Items : {len(borrowed_items)}")
    print(f"Books : {book_count} | Magazines : {magazine_count}")
    print("\nSuccessfully borrowed!")
    


def return_item():
 while True:
    print("\n===== Return Item =====")

    item_id = input("Enter Item ID to return : ").strip()

    if item_id == "":
        print("Item ID cannot be empty")
        return

    found_item = None

    for item in library_items:
        if item.item_id.lower() == item_id.lower():
            found_item = item
            break

    if found_item is None:
        print("Item not found")
        return

    if not found_item.is_borrowed:
        print("This item is not currently borrowed")
        return

   
    while True:
        days_late = input("Days Late : ").strip()

        if days_late == "":
            print("Days Late cannot be empty")
            continue

        if not days_late.isdigit():
            print("Days Late must be a number")
            continue

        days_late = int(days_late)

        if days_late < 0:
            print("Days Late cannot be negative")
            continue

        break

    late_fee = found_item.calculate_late_fee(days_late)

    found_item.is_borrowed = False
    print(f"Item Type : {found_item.get_type()}")
    print(f"Days Late : {days_late}")
    print(f"Late Fee : Rp{late_fee:,}")
    print("Item successfully returned")

    print("\n 1. Return again?")
    print("2. Back To Main Menu")
    choose=input ("Choose 1/2 : ").strip()
    if choose =="2" :
        return  

def category_summary():
  while True:  
    if not library_items:
        print("No Items yet")
        return

    category_data = {}

    for item in library_items:

        category = item.category

        if category not in category_data:
            category_data[category] = {
                "Book_total": 0,
                "Book_borrowed": 0,
                "Magazine_total": 0,
                "Magazine_borrowed": 0
            }

        if item.get_type() == "Book":
         category_data[category]["Book_total"] += 1
         if item.is_borrowed:
            category_data[category]["Book_borrowed"] += 1
        else:
          category_data[category]["Magazine_total"] += 1
          if item.is_borrowed:
            category_data[category]["Magazine_borrowed"] += 1  

    print("\n===== CATEGORY SUMMARY =====")

    for category, data in category_data.items():

        print(f"\nCategory : {category}")
        print(f"Total of Book   : {data['Book_total']}")
        print(f"Borrowed Book   : {data['Book_borrowed']}")
        print(f"Available Book  : {data['Book_total'] - data['Book_borrowed']}")
        print(f"\nTotal of Magazine   : {data['Magazine_total']}")
        print(f"Borrowed Magazine   : {data['Magazine_borrowed']}")
        print(f"Available Magazine  : {data['Magazine_total'] - data['Magazine_borrowed']}")
        print(f"\nGrand Total  : {data['Book_total'] + data['Magazine_total']}")
    
    print("\n 1. Show Category Summary again?")
    print("2. Back To Main Menu")
    choose=input ("Choose 1/2 : ").strip()
    if choose =="2" :
            return  

def get_summary_data():
    if not library_items:
        return None

    total_items = len(library_items)
    total_books = 0
    total_magazines = 0
    borrowed_items = 0

    newest_item = library_items[0]
    oldest_item = library_items[0]

    for item in library_items:
        if item.get_type() == "Book":
            total_books += 1
        else:
            total_magazines += 1
        if item.is_borrowed:
            borrowed_items += 1
        if item.publication_year > newest_item.publication_year:
            newest_item = item
        if item.publication_year < oldest_item.publication_year:
            oldest_item = item

    available_items = total_items - borrowed_items

    return {
        "total": total_items,
        "books": total_books,
        "magazines": total_magazines,
        "borrowed": borrowed_items,
        "available": available_items,
        "newest": newest_item,
        "oldest": oldest_item
    }

def library_summary():
    data = get_summary_data()
    if data is None:
        print("No Items yet")
        return

    print("\n===== LIBRARY SUMMARY =====")
    print(f"Total Items : {data['total']}")
    print(f"Total Books : {data['books']}")
    print(f"Total Magazines : {data['magazines']}")
    print(f"Borrowed Items : {data['borrowed']}")
    print(f"Available Items : {data['available']}")
    print(f"Newest Item : {data['newest'].title}")
    print(f"Oldest Item : {data['oldest'].title}")

def save_report():
    data = get_summary_data()
    if data is None:
        print("No Items yet")
        return

    f = open("library_report.txt", "w")

    f.write("===== LIBRARY REPORT =====\n\n")
    for item in library_items:
        status = "Borrowed" if item.is_borrowed else "Available"
        f.write(f"ID : {item.item_id}\n")
        f.write(f"Title : {item.title}\n")
        f.write(f"Type : {item.get_type()}\n")
        f.write(f"Category : {item.category}\n")
        f.write(f"Publication Year : {item.publication_year}\n")
        if item.get_type() == "Book":
            f.write(f"Author : {item.author}\n")
        else:
            f.write(f"Issue Number : {item.issue_number}\n")
        f.write(f"Status : {status}\n")
        f.write("\n----------------------------------------\n\n")

    f.write("========================================\n")
    f.write("LIBRARY SUMMARY\n")
    f.write("========================================\n")
    f.write(f"Total Items : {data['total']}\n")
    f.write(f"Total Books : {data['books']}\n")
    f.write(f"Total Magazines : {data['magazines']}\n")
    f.write(f"Borrowed Items : {data['borrowed']}\n")
    f.write(f"Available Items : {data['available']}\n")
    f.write(f"Newest Item : {data['newest'].title}\n")
    f.write(f"Oldest Item : {data['oldest'].title}\n")
    f.write("========================================\n")

    f.close()
    print("Report saved to library_report.txt")

def read_report():
    f = open("library_report.txt", "r")
    content = f.read()
    print("\n" + content)
    f.close()
    
def mainMenu():
    while True:
        print("\n===== LIBRARY BORROWING MANAGEMENT SYSTEM =====")
        print("1. Add Library Item")
        print("2. Show All Items")
        print("3. Find Item")
        print("4. Borrow Item")
        print("5. Return Item")
        print("6. Category Summary")
        print("7. Library Summary")
        print("8. Save Report")
        print("9. Read Report")
        print("10. Exit")

        menu = input("\nChoose menu: ").strip()

        if menu == "1": add_item()
        elif menu == "2": show_all_items()
        elif menu == "3": find_item()
        elif menu == "4": borrow_item()
        elif menu == "5": return_item()
        elif menu == "6":category_summary()
        elif menu == "7":library_summary()
        elif menu == "8": save_report()
        elif menu == "9": read_report()
        elif menu == "10": 
            print("Thank you") 
            break
        else:
            print("Please choose 1-10 only")
mainMenu()