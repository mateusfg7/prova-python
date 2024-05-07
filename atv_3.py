numero = int(input("Escreva um número: ")) 

contador = numero 
while contador > 0:
    if not contador % 2 == 0:
        print(contador) 
    contador -= 1 
