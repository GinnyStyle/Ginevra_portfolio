prezzo_drink = 5.5
sconto_drink = 1
cliente_preferito = "Giacomino"

print("\nCome ti chiami?")
nome_cliente = str(input())

if nome_cliente == cliente_preferito:
    print("Ciao Giacomino qui uno sconto solo per te! Sul prezzo del dirnk")
    print(prezzo_drink-=sconto_drink)
else:
    print("Ciao " + nome_cliente)
    print("\nQuanti anni hai?")
    anni_cliente = int(input())
    print(prezzo_drink)
