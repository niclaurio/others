from typing import Tuple
from somma_algebrica import somma_algebrica

def controllo_segni(numero_1:float, numero_2:float)->Tuple[str, float, float]:
    '''
    Parameters
    ----------
    numero_1 : float
    
    numero_2 : float
   

    Returns
    -------
    Tuple[str, float, float]
        str: segno della moltiplicazione
        float: valore assoluto numero_1
        float: valore assoluto numero_2

    '''
    if (numero_1 > 0 and numero_2 > 0 ) or (numero_1 < 0 and numero_2 < 0):
        segno = 'più'
    else: 
        segno = 'meno'
    return segno, abs(numero_1), abs(numero_2)



def moltiplico (numero_1:str, numero_2:str)->float:
    '''
    calcola il prodotto in colonna fra due numeri
    
    Parameters
    ----------
    numero_1 : str
        
    numero_2 : str
        

    Returns
    -------
    float
        risultato della moltiplicazione

    '''
    risultato = 0
    iteration = 0
    resto = 0
    for  indice in range(len(numero_2)-1, -1,-1):
        p = numero_2[indice] 
        if p != '.':
            p = int(float(str(p)))
            riga = ''
            for i in range(len(numero_1)-1, -1, -1):
                if numero_1[i] != '.':
                    elemento = p * int(float( numero_1[i])) + resto
                    resto = 0
                    while elemento > 9 and i > 0:
                        elemento = elemento - 10
                        resto = resto + 1
                    riga =  str(elemento) + riga
            riga = float(riga)
            riga = int(riga * (10 ** iteration))
            iteration = iteration + 1
            risultato = int(somma_algebrica(risultato, riga))
    return risultato



def prodotto(numero_1:float, numero_2:float)->float:
    lista = controllo_segni(numero_1, numero_2)
    segno = lista[0]
    numero_1 = str(float(lista[1]))
    numero_2 = str(float(lista[2]))
    
    # il numero delle cifre decimali del risultato sarà la somma delle cifre decimali dei due numeri
    cifre_decimali = len(numero_1) + len(numero_2) - len(str(int(float(numero_1)))) - len(str(int(float(numero_2)))) - 2
    
    #assegno a numero_2 il numero con meno cifre e a numero_1 l'altro
    if  len(numero_2)> len(numero_1):
        n = numero_2
        numero_2 = numero_1
        numero_1 = n 
    
    risultato = str(moltiplico(numero_1, numero_2))
    
    #calcolo la lunghezza della parte intera del risultato
    parte_intera = len(risultato) - cifre_decimali
    
    # la parte intera del risultato sarà costituita dalle prime (parte_intera)-cifre del risultato
    parte_intera = risultato[:parte_intera] 
    
    # la parte decimale del risultato sarà costituita dalle ultime (cifre_decimali)-cifre del risultato
    parte_decimale = risultato[-cifre_decimali:]
    
    risultato = parte_intera + '.' + parte_decimale
    if segno == 'meno':
        return - float(risultato)
    else:
        return float(risultato)
    
                
                
