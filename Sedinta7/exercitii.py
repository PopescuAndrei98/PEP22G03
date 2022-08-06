# #Functii /tupluri obiecte /tuples
# # o insiruire
#
# my_tuple = ("a ",1 ,None, 'a')
# print(type(my_tuple))
#
# #tuple methods
#
# result = my_tuple.count('a')
# print(f'Numarul de obiecte in tuple: {result}')
#
# print(len(my_tuple))
#
# #tuple slice
# result= my_tuple[1:3]
# print('slice:',result)
#
# #unpaking tuple
# var1, var2, var3, var4 = my_tuple
#
# print(var1, var2, var3, var4)
#
# var1, *var2, var3 = my_tuple
#
# print(var1, var2, var3)
#
# #args as tuple
#
# def my_print(args,*args2):
#     print(type(args))
#     print(args)
#
#     print(type(args2))
#     print(args2)
# my_print('value1', 'value2', '123','abcd') #dynamic number of arguments
#
# #dictionary
# #tuple declarat (1,2,3)
# # au o cheie care pastreaza anumite obiecte in o anumita ordine
# my_dict= {'key1': None, 123: 'abcd', True: (1,2,3) }   #pentru a declara un dictionar
#
# print(my_dict)
# print(type(my_dict))
#
# #dict methods
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)
# print(my_dict.values())
#
# for value in my_dict.values():
#     print(value)
#
# print(my_dict.items())
# for item in my_dict.items():
#     print(item)
#
# for keys, value in my_dict.items():
#     print(keys,value)
#
# #understanding dict items
#
# result= my_dict.items()
# itered=result.__iter__()
# key,value = next(itered)
# print(key,value)
# key,value=next(itered)
# print(key,value)
# key,value=next(itered)
# print(key,value)

# din laborator ex2
# def app():
#     numar = 5
#     while True:
#         putere = input("Introdu un numar: ")
#         if putere == "q":
#             break
#         numar = numar ** int(putere)
#         print("Avesta este puterea calculata: ", numar)
# app()

#ex3
# def check_logs():
#    acces={}
#
#    for i in range(1, 4):
#         acces[input(f"User PC.{i}")] = input(f"User password.{i}")
#
#    for user, parola in acces.items():
#
#         print(f"{user} --> {parola}")
#
# check_logs()
angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}
angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}
angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755,
}
angajat4 = {
'nume': 'Oana Popa',
'departament': 'HR',
'ID': 1977,
'Salar': 5400,
}
angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900,
}
lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]
#a
# for angajat in lista_dict:
#     if angajat['Salar'] > 5000:
#         print(f"{angajat['nume']} -> {angajat['departament']}{angajat['ID']}")

#b
list = []
for angajat in lista_dict:
    if angajat['departament'] != "Management":
        list.append(angajat['nume'])
print(list)

#c
counter =0
suma=0
for angajat in lista_dict:
    if angajat['departament'] == "HR":
      counter +=1
      suma +=angajat['Salar']
media= suma/counter
print(media)

