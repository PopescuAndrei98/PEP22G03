
def Stergere_func(inventar:dict):
    #from add import inventar
    produse = input("cate produse doriti sa stergeti?").strip()
    del inventar[produse]