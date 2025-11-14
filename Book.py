class Book:
    def __init__(self, title, author, year, available):
        if isinstance(title, str):
            pass
        else:
            raise TypeError("Mauvais type pour le titre")
        
        if isinstance(author, str):
            pass
        else:
            raise TypeError("Mauvais type pour l'auteur")

        if isinstance(year, int):
            pass
        else:
            raise TypeError("Mauvais type pour la date")
        
        if isinstance(available, bool):
            pass
        else:
            raise TypeError("Mauvais type pour la disponibilité")

        self.title = title
        self.author = author
        self.year = year
        self.available = available
    
    def show_book(self):
        availability = "Disponible" if self.available == True else "Indisponible"
        print(f"{self.title} de {self.author} paru en {self.year} -- {availability}")
