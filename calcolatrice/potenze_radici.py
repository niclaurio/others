from divisione import divisione 
from moltiplicazione import prodotto
from somma_algebrica import somma_algebrica
from typing import Tuple

def controllo_segnoo(esponente):
    if esponente > 0:
        segno = 'più'
    else:
        segno = 'meno'
        esponente = abs(esponente)
    return segno, esponente 


def potenza(base:float, esponente:int)-> float:
    tupla = controllo_segnoo(esponente)
    segno = tupla[0]
    esponente = tupla[1]
    risultato = 1
    while esponente > 0:
        risultato = prodotto(base, risultato)
        esponente = esponente - 1
    if segno == 'meno':
        return divisione(1, risultato)
    return risultato






def trova_estremi(numero:float, esponente:int)->Tuple[float, float]:
    '''
    calcola da quante cifre è formata la parte intera del risultato
    trova fra quali valori è compreso il risultato 
    Parameters
    ----------
    numero : float
        numero di cui calcolare la radice
    esponente : int
        

    Returns
    -------
    Tuple(float, float)
        float <= risultato < float

    '''
    i = 0
    while numero >= 1:
        numero = divisione(numero, potenza(10, esponente))
        i = i + 1
    estremo_dx = potenza(10, i)
    estremo_sx = potenza(10, i-1)
    return (estremo_sx, estremo_dx)
    

def ciclo_for(estremo_sx:float, estremo_dx:float, numero:float, esponente:int)->float:
    '''
    calcola gli estremi dell'intervallo in cui il risultato è sicuramente compreso

    Parameters
    ----------
    estremo_sx : float
        estremo inferiore dell'intervallo
        
    estremo_dx : float
        estremo superiore
    numero : float
        numero di cui calcolare la radice
    esponente : int
        

    Returns
    -------
    float
        risultato radice
    '''
    media_prec = 0
    for _ in range(1000):
        media = divisione(somma_algebrica(estremo_dx, estremo_sx), 2)
        if media == media_prec:
            return estremo_sx
        pot = potenza(media, esponente) 
        if pot> numero:
            estremo_dx = media
        elif pot == numero:
            return media
        else:
            estremo_sx = media
        media_prec = media
    return estremo_sx
    

    
def radice(numero:float, esponente:int)->float:
    tupla = controllo_segnoo(esponente)
    segno = tupla[0]
    esponente = tupla[1]
    tupla = trova_estremi(numero, esponente)
    estremo_sx = tupla[0]
    estremo_dx = tupla[1]
    risultato = ciclo_for(estremo_sx, estremo_dx, numero, esponente)
    if segno == 'meno':
        return divisione(1, risultato)
    return risultato

        

    


        