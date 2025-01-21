class Book:
    def __init__(self,name,price,library):
        self.name=name
        self.price=price        
        self.library=library
        library.add_book(self)
        self.status="Available"
        print(f"Book {self.name} added.! Its price is {self.price} Rs")

    def get_price(self):
        print(f"The price of '{self.name}' : {self.price}")

# Library-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def __str__(self):
        return f"Library : name: {self.name} \n Available Books :{self.books}"

    def get_available_books(self):
        if len(self.books) > 0:
            print(f"Book in {self.name}")
            print("-------------------------")
            for book in self.books:
                print(book.name)
        else:
            print("No Books available in Library")

    def add_book(self,book):
        self.books.append(book)
    
    def check_availability(self,book):
        if book in self.books:
            if book.status == "Available":
                print(f"The book {book.name} is AVAILABLE")
                return True
            else:
                print(f"The book {book.name} is NOT AVAILABLE")
                return False
        else:
            print(f"The book {book.name} is NOT AVAILABLE IN OUR LIBRARY")
            return False
    
    def rent_book(self,book):
        if not self.check_availability(book):
            book.status="Not Available"
            print(f"The book {book.name} is Not AVAILABLE anymore!")


    def return_book(self,book):
        if book in self.books:
            if book.status == "Available":
                print(f"The book {book.name} has been Returned Already")
            else:
                book.status="Available"
                print(f"Book {book.name} is now available in the Library")
        else:
            print("This Book Doest Belong to our Library")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
oxford_library = Library("Oxford")
bangalore_library = Library("Bangalore")

oxford_library.get_available_books()

book1 = Book("Alice in Wonderland", 290.58, oxford_library)
book2 = Book("Clutchless", 580, oxford_library)
book3 = Book("Good Vibes", 230, oxford_library)
book4 = Book("Twilight Saga", 210.50, bangalore_library)
book5 = Book("Million Dots", 500, bangalore_library)

oxford_library.get_available_books()

oxford_library.get_available_books()
bangalore_library.get_available_books()

oxford_library.rent_book(book1)
oxford_library.get_available_books()

oxford_library.return_book(book1)
oxford_library.get_available_books()

oxford_library.rent_book(book2)
oxford_library.return_book(book2)

bangalore_library.rent_book(book4)
bangalore_library.rent_book(book4)
bangalore_library.return_book(book4)
bangalore_library.return_book(book4)

book5.get_price()
book4.get_price()