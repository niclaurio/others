
from divisione import divisione 
from moltiplicazione import prodotto
from potenze_radici import potenza, radice
from somma_algebrica import somma_algebrica


def check_number():
    number = input()
    while True:
        try:
            number = float(number)
        except ValueError:
            print("non hai inserito un numero riprova")
        else:
            return number
        
 

close = False
print("Benvenuto !!! ")

while close == False:   
    print("Per effettuare una somma premere 1, una moltiplicazione 2, una divisione 3, una potenza 4, una radice5, per uscire 6")
    n = check_number()
    if n == 1: 
        print("inserisci il primo numero da sommare")
        numero_1 = check_number()
        print("inserisci il secondo numero da sommare")
        numero_2 = check_number()
        print(somma_algebrica(numero_1, numero_2))
    elif n == 2: 
        print("inserisci il primo numero da moltiplicare")
        numero_1 = check_number()
        print("inserisci il secondo numero da moltiplicare")
        numero_2 = check_number()
        print(prodotto(numero_1, numero_2))
    elif n == 3:
        print("inserisci il dividendo")
        dividendo = check_number()
        print("inserisci il divisore")
        divisore = check_number()
        print(divisione(dividendo, divisore))
    elif n == 4:
        print("quanto vale la base??")
        base = check_number()
        print("quanto vale l'esponente??")
        esponente = check_number()
        if int(esponente) != esponente:
            raise ValueError(f"l'esponente deve essere un numero intero")
        print(potenza(base, esponente))
    elif n == 5:
        print("quanto vale il numero di cui calcolare la radice??")
        numero = check_number()
        print("quanto vale l'esponente??")
        esponente = check_number()
        if int(esponente) != esponente:
            raise ValueError(f"l'esponente deve essere un numero intero")
        if (numero < 0) and (esponente % 2 == 0):
            raise ValueError(f"non è possibile calcolare la radice di indice pari di un numero negativo")
        print(radice(numero, esponente))
    elif n == 6:
        close = True
    else:
        raise ValueError(f"nonhai inserito un numero intero tra quelli accettabili")
    
