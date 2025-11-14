from Book import Book
from Category import Category

class Library:
    def __init__(self, category_list):
        if isinstance(category_list, list):
            pass
        else:
            raise TypeError("Mauvais type pour la liste de catégorie")
        
        self.category_list = category_list

    def borrow_book(self, category_name, title):
        for category in self.category_list:
            if category.name == category_name:
                return category.borrow(title)

        raise Exception("La categorie n'existe pas")
    
    def return_book(self, category_name, returned_book):
        for category in self.category_list:
            if category.name == category_name:
                category.return_book(returned_book)
                return
            
        raise Exception("La categorie n'existe pas")
        
    def total_available(self):
        total = 0
        for category in self.category_list:
            count = len(category.available_books())
            total += count
        return total