compra = 0.00
while True:
    print("\nMENU")
    print("[1] Adicionar valor")
    print("[2] Encerrar")
    escolha = int(input("-> "))

    print("")
    
    if escolha == 1:
        valor_produto = float(input("Novo valor: R$ ").replace(",", "."))
        
        compra += valor_produto
    elif escolha == 2:
        break
    else:
        print("Escolha inválida!")
        
pagamento = float(input("Valor pago: R$ ").replace(",", "."))

if compra <= pagamento:
    troco = "%.2f" % (pagamento - compra)
    
    print("\nTroco: %s" % troco.replace(".", ","))
else:
    print("\nValor insuficiente!")
    
