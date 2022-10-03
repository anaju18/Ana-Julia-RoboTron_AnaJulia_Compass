número = int(input("Diga um número: "))
número_2 = int(input("Diga um número: "))
resultado = (número + número_2) % 2
if resultado ==0:
    print("O número {} é PAR".format(número + número_2))
else: 
    print ("O número {} é ÍMPAR".format(número + número_2))