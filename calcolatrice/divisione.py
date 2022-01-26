from moltiplicazione import controllo_segni


def divisione(dividendo:float, divisore:float)->float:
    tupla = controllo_segni(dividendo, divisore)
    segno = tupla[0]
    dividendo = tupla[1]
    divisore = tupla[2]
    risultato = 0
    for i in range(13):
        risultato = risultato  * 10 
        dividendo = dividendo * 10 
        while dividendo >= divisore:
            dividendo = dividendo - divisore
            risultato += 1
        if divisore == 0:
            break
    risultato = str(int(risultato))
    lunghezza = len(risultato)-1
    if lunghezza > i:
        parte_intera = lunghezza - i
        parte_intera = risultato[:parte_intera]
        i = i+ 1
        parte_decimale = risultato[-i:]
        risultato = float(parte_intera + '.' + parte_decimale)
    elif lunghezza == i: 
        risultato = float('0.' + risultato)
    else:
        n = i - lunghezza
        p = ''
        while n > 0:
            p = p + '0'
            n = n - 1
        risultato = '0.' + p + risultato 
    if segno == 'meno':
        return - float(risultato)
    return float(risultato)



            

