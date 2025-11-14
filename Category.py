from Book import Book

class Category:
    def __init__(self, category_name, books_list):

        #Vérification des types
        if isinstance(category_name, str):
            pass
        else:
            raise TypeError("Mauvais type pour le nom de catégorie")
        
        if isinstance(books_list, list):
            pass
        else:
            raise TypeError("Mauvais type pour la liste de livres")
        
        self.category_name = category_name
        self.books_list = books_list

    #Méthode qui retourne une liste des livres disponibles dans la catégorie
    def available_books(self):
        available_books = []
        for book in self.books_list:
            if book.available == True:
                available_books.append(book)
        return available_books

    #Emprunter un livre
    def borrow(self, title):
        searched_book = None
        for book in self.books_list:
            if book.title.lower() == title.lower():
                searched_book = book
                break
        
        if searched_book == None:
            raise Exception(f"Le livre {title} n'a pas été trouvé")
        
        elif searched_book.available == False:
            raise Exception("Le livre a déjà été emprunté")
        else:
            searched_book.available = False
            return searched_book
                
    #Retourner un livre
    def return_book(self, returned_book):
        for book in self.books_list:
            if book == returned_book:
                returned_book.available = True
                return book
        raise Exception("Le livre n'est pas dans cette catégorie")