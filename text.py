#Dichiarazione variabili
nome_barman = "Edobot"
drink_speciale = "digital vodka"
prezzo_dirnk =  5.5

#inizio del programma
print("Benvenuto al Pub Drink e codici")
print("Mi chiamo "+nome_barman+' ...e sono pronto a servirti! =)')

print("Il drink piu' cool del nostro locale e': "+str(drink_speciale))
print("Provalo subio al modico prezzo di: "+str(prezzo_dirnk))
print("\nInserisci il tuo anno di nascita ")
anno_nascita = int(input())
anni_cliente = 2022 - anno_nascita
print("Hai "+str(anni_cliente)+" anni")

if anni_cliente <18:
    print("\nSei minorenne: puoi ordinare solo analcolici")
else:
    print("\nSei maggorenne: puoi ordinare alcolici e analcolici")
