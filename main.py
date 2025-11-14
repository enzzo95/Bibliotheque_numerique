from Book import Book
from Category import Category
from Library import Library

FILE_PATH = "books.csv"

def load_and_initialize_categories(filepath):

    """
    Initialisation du .CSV chatgptéisé car je n'arrivais pas a regrouper les livres par catégorie
    """

    categories_list = [] 
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            
            for line in f:
                try:
                    line = line.strip()
                    if not line: 
                        continue

                    parts = [part.strip() for part in line.split(';')]
                    if len(parts) != 5:
                        raise ValueError("Ligne n'a pas 5 colonnes.")
                        
                    category_name, title, author, year_str, available_str = parts
                    
                    book = Book(title, author, int(year_str), available_str.lower() == 'yes')

                    found_category = None

                    for cat in categories_list:
                        if cat.category_name == category_name: 
                            found_category = cat
                            break
                    
                    if found_category:
                        found_category.books_list.append(book) 

                    else:
                        new_cat = Category(category_name, [book]) 
                        categories_list.append(new_cat)

                except (ValueError, TypeError) as e:
                    print(f"Erreur : {e}")
                    
    except FileNotFoundError:
        print(f"Erreur : fichier non trouvé")
        return None

    return categories_list


#MAIN :
final_categories = load_and_initialize_categories(FILE_PATH)

if not final_categories:
    raise Exception("Erreur de chargement des données")
    
library = Library(final_categories)

print("Début.....")

emprunt = None

try:
    print(f"Livres disponibles avant toute action :  {library.total_available()}")

    emprunt = library.borrow_book('Roman', 'Bel-Ami')

    print(f"Livres disponibles après l'emprunt : {library.total_available()}")

    library.borrow_book('Roman', 'Bel-Ami')

except (TypeError, Exception) as e:
    print(f"Erreur : {e}")

try:
    library.return_book('Roman', emprunt)

    print(f"Livres disponibles apres le retour du livre : {library.total_available()}")
    
except (TypeError, Exception) as e:
    print(f"Erreur : {e}")



