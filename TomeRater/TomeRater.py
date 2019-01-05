class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)

        else:
            print("No user with email %s" % email)
        
        if book in self.books:
            self.books[book] += 1

        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[new_user.email] = new_user

        if user_books != None:
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        print(list(self.books))
        
    def print_users(self):
        print(list(self.users.values()))

    def most_read_book(self):
        most_read = sorted(self.books.items(), key=lambda kv: kv[1])
        return "Most read book: " + str(most_read[-1][0])

    def highest_rated_book(self):
        rated_books = {}
        for i in self.books:
            rated_books[i] = i.get_average_rating()
        highest_rated = sorted(rated_books.items(), key=lambda kv: kv[1])
        return "Highest rated book: " + str(highest_rated[-1][0])

    def most_positive_user(self):
        rated_users = {}
        for i in self.users:
            rated_users[i] = self.users[i].get_average_rating()
        highest_rated = sorted(rated_users.items(), key=lambda kv: kv[1])
        return "Most positive user: " + str(highest_rated[-1][0])
        

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "ISBN has been updated"

    def add_rating(self, rating):
        if type(rating) != int:
            pass
        elif rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __repr__(self):
        return "%s" % self.title

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            self = other_book
          

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "%s by %s" % (self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "%s, a %s manual on %s" % (self.title, self.level, self.subject)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "Email address has been updated"

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        book_values = []
        for i in self.books.values():
            if type(i) != int:
                pass
            else:
                book_values.append(i)
            
        return sum(book_values) / len(book_values)

    def __repr__(self):
        return "User %s, email: %s, books read: %s" % (self.name, self.email, str(len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            self = other_user