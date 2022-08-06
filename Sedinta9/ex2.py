my_text = ("""in p$imava$a anu^ui 1894, t%ata ^%nd$a a f%!t int#$#!ata, ia$
^um#a ^a m%da a f%!t &%n!t#$nata d# u&id#$#a %n%$abi^u^ui $%na^d
adai$ in &i$&um!tant# &#^# mai n#%bi!nuit# !i in#xp^i&abi^#.
pub^i&u^ a af^at d#ja a&#^# d#ta^ii a^# &$im#i &a$# au i#!it ^a
iv#a^a in an&@#ta p%^iti#i; da$ mu^t# au f%!t !up$imat# &u a&#a
%&azi#, d#%a$#&# &azu^ a&uza$ii #$a atat d# &%p^#!it%$ d#
put#$ni&, in&at nu #$a n#&#!a$ !a !# p$#zint# t%at# fapt#^#. abia
a&um, ^a !fa$!itu^ a ap$%ap# z#&# ani, imi #!t# p#$mi! !a
ap$%vizi%n#z a&#^# v#$igi ^ip!a &a$# a^&atui#!& int$#gu^ ^ant
$#ma$&abi^. &$ima #$a int#$#!anta in !in#, da$ a&#^ int#$#! nu
#$a nimi& p#nt$u min# in &%mpa$ati# &u &%ntinua$#a d# n#&%n&#put,
&a$# mi-a %f#$it &#^ mai ma$# !%& !i !u$p$iza din %$i&# #v#nim#nt
din vitța m#a av#ntu$%a!a. &@ia$ !i a&um, dupa a&#!t int#$va^
^ung, mă t$#z#!& #m%ti%nat &and ma gand#!& ^a a!ta !i !imt din
n%u a&#^ p%t%p b$u!& d# bu&u$i#, uimi$# !i n#in&$#d#$# &a$# mi-a
&ufundat &u t%tu^ mint#a.
"""
)
litere = {
'!':'s',
'@':'h',
'#':'e',
'$':'r',
'^':'l',
'%':'o',
'&':'c',
'*':'k'
}
result=''
for i in my_text:
    if i in litere.keys():
        result+=litere[i]
    else:
        result+=i
print(result)


c= False
result = ''
for i in result.split():
    if c == True:
        i= i.capitalize()
        c=False
    if '.' in i :
       c=True
    result +=i
print(result)


#b
resultb= ''
counter=0
for i in result:
    if i == '.':
        counter = 3
    if counter == 1:
       i = i.upper()
       counter = 0
    else:
        counter -= 1
    resultb +=i
print(resultb)
#pana aici
# result =result.__iter__()
#
# for i in result:
#     if i == '.':
#         counter = 3
#     if counter == 1:
#        i = i.upper()
#        counter = 0
#     else:
#         counter -= 1
#     resultb +=i
# print(resultb)


#c).
text_si_mai_spart = text1.replace(",","").replace(".","").replace(";","").split(" ")
print("")
lista = []
for i in text_si_mai_spart:
    lista.append(i)
print(lista)
#d).
scurte = 0
medii = 0
lungi = 0
for i in text_si_mai_spart:
    if len(i) <= 5:
        scurte = scurte + 1
    if 5 < len(i) <= 8:
        medii = medii + 1
    if len(i) > 8:
        lungi = lungi + 1
print("Avem", str(scurte), "cuvinte scurte.")
print("Avem", str(medii), "cuvinte medii.")
print("Avem", str(lungi), "cuvinte lungi.")