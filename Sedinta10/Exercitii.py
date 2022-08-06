# import time
#
# x= 2
# try:
#     time.sleep(10)
#     for i in range(x):
#         if i == 0:
#             raise  ArithmeticError
#         print(1/(-1+i))
#
# except ZeroDivisionError:
#     print("Divizia cu 0 nepermisa.")
#
# except ArithmeticError:
#     print("Other math error")
#    # time.sleep(10)
#
# except Exception:
#     print("Something else happend")
#
# except:
#     print("ALL other error")


#####  nu e intreg!!
# var1= ">>>"
# var2="    "
# counter=0
# while True:
#    inp= input(f"{var1}")
#     try:
#
#         if inp[-1] ==":":
#             counter +-1
#             var1 = "...    "+var2*counter
#         elif inp=="\b":
#             counter -=1
#             var1 = "...    " + var2 * counter
#     except IndexError:
#         input(f"{var1}")

#SCrierea de numere prime din orice interval dorim.
import random


def generate_primes(limit: int):
    result = [ ]
    for i in range(1, limit + 1):
        for j in range(2, i//2+ 2):
           if i % j == 0:
            break
        else:
            result.append(i)
    return result

generate_primes(100)

#  selectare 2 nr prime random
#  select_primes(generate_primes(100))

def select_primes(in_list:list):
    i = random.choices(in_list)
    in_list.remove(i[0])
    j = random.choices(in_list)
    return i[0],j[0]
print(select_primes(generate_primes(100)))


# de calculat