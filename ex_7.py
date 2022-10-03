def media(num_um, num_dois):
    return (num_um + num_dois)/2 

def main():
    num_um = int(input("informe o primeiro valor inteiro: "))
    num_dois = int(input("informe o segundo valor inteiro: "))
    media = media(num_um, num_dois)
    print (f"a média dos dois inteiros é: {media}")
