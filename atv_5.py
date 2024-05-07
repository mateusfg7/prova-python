import os

lista_de_compras = []

while True:
    os.system("cls")
    
    print("\n[ Home ] - Listas de compras")
    print("\n[1] Adicionar item")
    print("[2] Remover item")
    print("[3] Consultar a lista")
    print("[4] Finalizar lista")
    escolha = int(input("-> "))
    
    if escolha == 1:
        os.system("cls")
        print("[ New ] - Adicionar item")
        
        print("\nNome do item")
        nome = input("-> ")
        
        print("\nQuantidade")
        qtd = int(input("-> "))
        
        if qtd < 1:
            print("\nQuantidade inválida, item não adicionado!")
        else:
            lista_de_compras.append([nome, qtd])

    elif escolha == 2:
        os.system("cls")
        print("[ Delete ] - Remover item\n")
        
        
        indice = 0
        for (nome, _) in lista_de_compras:
            print("[%d] %s" % (indice, nome))
            indice += 1
        
        print("")
        
        print("Número do item a ser removido")
        item = int(input("-> "))
        
        if item < 0 or item > (len(lista_de_compras) -1):
            print("\n[ ITEM NÃO ENCONTRADO! ]\n")
            input("Pressione enter para voltar...")
        else:
            del lista_de_compras[item]
                 
    elif escolha == 3:
        os.system("cls")
        print("[ Check ] - Lista de compras\n")
        
        if len(lista_de_compras) < 1:
            print("Lista vazia...")
        else:        
            for (nome, qtd) in lista_de_compras:
                print("(%d) %s" % (qtd, nome))
        
        print("")
        input("Pressione enter para voltar...")
    elif escolha == 4:
        break
    else:
        print("\n[ OPÇÃO INVÁLIDA! ]\n")
        input("Pressione enter para voltar...")
    
    
os.system("cls")

print("LISTA DE COMPRAS:\n")

total = 0
for (nome, qtd) in lista_de_compras:
    print("(%d) %s" % (qtd, nome))
    total += qtd

print("")

print("TOTAL: %d\n\n" % total)