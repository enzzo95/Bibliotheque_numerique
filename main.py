from Book import Book
from Category import Category
from Library import Library

liste_livres = []

livre1 = Book("TITRE1", "james", 1995, True)
livre2 = Book("TITRE2", "james", 1996, True)
livre3 = Book("TITRE3", "james", 1997, True)
livre4 = Book("TITRE4", "james", 1998, False)
livre5 = Book("TITRE5", "james", 1999, True)

liste_livres.append(livre1)
liste_livres.append(livre2)
liste_livres.append(livre3)
liste_livres.append(livre4)
liste_livres.append(livre5)

liste_cat = []
cat = Category("livres cools", liste_livres)
liste_cat.append(cat)

bibli = Library(liste_cat)

livre2.show_book()

emprunt = cat.borrow("titre2")

livre2.show_book()

print(bibli.total_available())

cat.return_book(emprunt)

print(bibli.total_available())