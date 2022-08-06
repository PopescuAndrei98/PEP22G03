from Adaugare import *

from Stergere import *

inventar = {}

if __name__ == '__main__':
    while True:

        selection = input("""
        Meniu:
        1. Vizualizare stoc
        2. Adaugare produs
        3. Stergere produs
        4. Iesire
        """)

        if selection == "1":
            print(inventar)

        if selection == "2":
            Adaugare_func(inventar)

        if selection == "3":
            Stergere_func(inventar)
        if selection == "4":
            break
        print(inventar)

