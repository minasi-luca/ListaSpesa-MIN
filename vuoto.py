lista = []
def Aggiungi_Lista(lista):
    prodotto = input("inserisci il prodotto:")
    lista.append(prodotto)
    print (lista)




def Stampa_Lista(lista):
    print("lista della spesa:")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def Rimuovi_Prodotto(lista):
    prodotto = input("prodotto da rimuovere:")
    lista.pop(lista.index(prodotto))

def Conta_Elementi(lista):
    return print("numero elementi:", len(lista))
def Svuota_Lista(lista):
    lista.clear()

while True:
    scelta=input("scegli cosa vuoi fare. (aggiungi , rimuovi , stampa, esci):\n 1. Aggiungi\n 2. rimuovi\n 3. stampa\n 4. esci\n 5. conta elementi\n 6. svuota lista\n")
    if scelta == "1":
        Aggiungi_Lista(lista)

    if scelta == "2":
        Rimuovi_Prodotto(lista)
    
    if scelta == "3":
        Stampa_Lista(lista)

    if scelta == "4":
       break;
    
    if scelta == "5":
        Conta_Elementi(lista)

    if scelta == "6":
        Svuota_Lista(lista)




    
