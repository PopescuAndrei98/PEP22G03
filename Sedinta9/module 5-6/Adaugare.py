
def Adaugare_func(inventar):
    #from add import inventar
    produse= input("ce produse doriti sa adaugati?").split(",")
    inventar.update({produse[0].strip(): (produse[1], produse[2])})
