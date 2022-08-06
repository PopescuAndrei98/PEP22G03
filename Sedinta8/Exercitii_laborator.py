#problema1
def fct_media(lista_varste):
    return  sum(lista_varste) /len(lista_varste)

def media_varsta():
        lista=[]
        nr_persoane=int(input("Cati participanti avem la sondaj"))
        for nr in range (nr_persoane):
            mesaje="Introduceti varsta participantului"
            while True:
                try:
                    varsta=int(input(f"{mesaje}, {nr+1}"))
                    lista.append(varsta)
                    break

                except ValueError:
                    mesaje="Reintroduceti varsta participantului "
                    continue
                    #varsta = int(input(f"Reintroduceti varsta participantului , {nr + 1}"))


        var1=fct_media(lista)
        print("Media de varsta a participantilor la sondajul de opinie este:",var1)
media_varsta()




