#execptii

def create_fraction(number):

    global result
    try:  #incearca sa faci linia asta
         if number >= 0:
             result = 1/number
         else:
            #result = 0
            raise ValueError('Number is small, cant use it') #pt o eroare <0
    except ZeroDivisionError:   # in caz de eroare fa urmatoarele
        result = 'Infinit'
        print('Cant use 0 divider')
    except ValueError:
        raise # trebuie sa iesi din program de aia e folosit
    except:
        result = 0
        print('This is an unknow Error')
    raise AttributeError
    return result
print(create_fraction(3))
#print(create_fraction(-1))

print(create_fraction(0))
print('Done')