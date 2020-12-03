# -*- coding: utf-8 -*-

from Catalog import Catalog

class User:
    catalog = Catalog()
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.book_issued = ""
        self.bookitem = None
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days=10):
        b = User.catalog.searchByName(name)
        if b:
            if b.total_count > 0:
                bookitem = b.book_item[-1]
                User.catalog.removeBookItem(name, bookitem.rack)
                self.book_issued = name
                self.bookitem = bookitem

    
    #assume name is unique
    def returnBook(self,name):
        if self.book_issued:
            b = User.catalog.searchByName(name)
            User.catalog.addBookItem(b, self.bookitem.rack)
            self.book_issued = ""
            self.bookitem = None
        else:
            print("No book issued by this member")     
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.emp_id
    
    def addBook(self,name,author,isbn,publish_date,pages):
        return User.catalog.addBook(name,author,isbn,publish_date,pages)

    def addBookItem(self, book, rack):
        User.catalog.addBookItem(book, rack)
    
    def removeBook(self,name):
        b = User.catalog.searchByName(name)
        if b:
            User.catalog.books.remove(b)
    
    def removeBookItemFromCatalog(self,catalog,book,rack):
        User.catalog.removeBookItem(book, rack)
        User.catalog.different_book_count -= 1

