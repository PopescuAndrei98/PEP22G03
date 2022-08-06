#string methods and functions


#len() function
my_sting="Hello Python"
print('Lengh is:', len(my_sting))
print('Lengh is:', my_sting.__len__())


my_sting=""
print('Lengh is:', len(my_sting))
#Format
my_sting="Hello Python {}"
print('Formatted text:', my_sting.format('abcd')) #inlocuieste anumite secvente de caractere cu un continut intre paranteze

my_sting="Hello Python {0} {1} {2}"
print('Formatted text:', my_sting.format('a','b','c'))


my_sting="Hello Python {enva} {envb} {envc}"
print('Formatted text:', my_sting.format(enva='a',envb='b',envc='c'))

#String tryps

#Normal string
normal1="Normal string\n"
normal2='Normal\n string'

#Multiline sting

normal1="""Normal string\n
New line"""
print(normal1)
normal2='''Normal
           string'''
print(normal2)

#raw string imi anuleaza orice din ""
normal1=r"""Normal string \n
New line"""
print(normal1)

#Formated strin
var1="insert"
normal1 = f"""Normal string {var1}
New line"""

print(print(normal1))
#None este un obiect

#replace method inlocuieste anumite caractere
var1="insert insert insert"
var1=var1.replace('ins', '_',2)
print('Replaced i:', var1)

