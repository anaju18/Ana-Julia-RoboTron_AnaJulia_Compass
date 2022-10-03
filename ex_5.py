soma = 0
num_pares = 0

for i in range (0, 20):
    valor = int(input("Informe um número: "))
    resultado = valor % 2
    if resultado ==0:
        soma = valor + soma
        num_pares = num_pares + 1 

média = soma / num_pares
print ("A média será: ", média)

