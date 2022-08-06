# ex2
def suma(lista: list):
    sum(lista)
    return sum(lista)


def medie(lista: list):
    pass


def putere(lista: list):
    pass


meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}
numbers = []
data = input("Introduceti numere. Cand sunteti gata, introduceti x:\n")
while data != 'x':
    numbers.append(float(data))
    data = input("number:")
print(numbers)

# b
mesaj = input("""Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire
Introduceti optiunea dvs:
""")
my_function = meniu[mesaj]

rezultat=my_function (numbers)
print(rezultat)