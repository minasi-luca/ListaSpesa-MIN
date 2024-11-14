lista = []
def Aggiungi_Lista(lista):
    prodotto = input("inserisci il prodotto:")
    lista.append(prodotto)
    print (lista)
Aggiungi_Lista(lista)
Aggiungi_Lista(lista)
Aggiungi_Lista(lista)



def Stampa_Lista(lista):
    print("lista della spesa:")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def Rimuovi_Prodotto(lista):
    prodotto = input("prodotto da rimuovere:")
    lista.pop(lista.index(prodotto))

Rimuovi_Prodotto(lista)
Stampa_Lista(lista)

while True:
    scelta=input("scegli cosa vuoi fare. (aggiungi , rimuovi , stampa, esci):/n 1. Aggiungi/n 2. rimuovi/n 3. stampa/n 4. esci")
    if scelta == "1":
        Aggiungi_Lista(lista)
