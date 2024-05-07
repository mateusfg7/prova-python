import sys

idade = int(input("Sua idade: "))

if idade < 0:
    print("Idade inválida!")
    sys.exit()
    
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 17:
    print("Jovem")
elif idade > 17 and idade <= 120:
    print("Adulto")
else:
    print("Idade inválida!")