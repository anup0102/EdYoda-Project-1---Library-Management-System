# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
    def __init__(self, name, author, isbn, publish_date, pages):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self, rack):
        b = BookItem(self, rack)
        self.book_item.append(b)
        self.total_count += 1
        
    def printBook(self):
        print (self.name,self.author)
        for book_item in self.book_item:
            print (book_item.rack)
            
    def searchBookItem(self,rack):
        for book_item in self.book_item:
            if rack.strip() == book_item.rack:
                return book_item

    def removeBookItem(self,book_item):
        if book_item in self.book_item:
            self.book_item.remove(book_item)
            self.total_count -=1
            
    def __repr__(self):
        return self.name + ' ' + self.author