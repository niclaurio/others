from typing import Tuple


def semplifica(a:float, b:float)->str:
    '''
    riduce la frazione ai minimi termine
    utilizzata ogni qualvolta la soluzione della disequazione è unica

    Parameters
    ----------
    a : float
       numeratore
        
    b : float
       denominatore 

    Returns
    -------
    str
        x = risultato

    '''
    #controllo il segno della frazione 
    if (a > 0 and b > 0) or (a <0 and b <0):
        segno = 'più'
    else:
        segno = 'meno'
        
    #voglio lavorare con numeri positivi
    a = abs(a)
    b = abs(b)
    
    #a è multiplo di b??
    if a % b == 0:
        a = int(a / b)
        if segno == 'più':
            return " x = " + str(a)
        return "x = -" + str(a)
    
    #b è multiplo di a??
    if b % a == 0:
        b = int(b/a)
        if segno == 'più':
            return " x = 1/ " + str(b)
        return "- x = 1/ " + str(b)
    
    #semplifico l'eventuale parte pari in comune
    while a % 2 == 0 and b % 2 == 0:
        a = int(a / 2)
        b = int(b / 2)
        
    # se hanno divisori in comune a questo punto sicuramente saranno dispari
    divisore = 3
    while divisore <= a and divisore <= b:
        while a % divisore == 0 and b % divisore == 0:
            a = int(a/divisore)
            b = int(b/divisore)
        divisore = divisore + 2
    
    #attribuisco segno frazione
    if segno == 'più':
        return " x = " + str(a) + "/" + str(b)
    return " x = -" + str(a) + "/" + str(b)
    
  
def porta_fuori(delta:int)->Tuple[int, int]: 
    '''
    porta fuori dalla radice tutta la parte possibile

    Parameters
    ----------
    delta : int

    Returns
    -------
    Tuple(int, int)
        radice: parte portata fuori dalla radice
        delta: parte rimasta dentro la radice

    '''    
    radice = 1
    #porto fuori tutta la parte multipla di 4
    while delta % 4 == 0:
        delta = int(delta / 4)
        radice = radice * 2
    
    #a questo punto se posso portare fuori qualcosa sicuramente sarà un quadrato dispari
    divisore = 3
    quadrato = 9
    while quadrato <= delta:
        #delta è divisibile per quadrato??
        while delta % quadrato == 0:
            delta = int(delta / quadrato)
            radice = radice * divisore
        divisore = divisore + 2
        quadrato = divisore ** 2
    return (radice, delta)

    
 
def scomponi_2(a:float,b:float) -> str:
    '''
    stessa cosa di semplifica 
    utilizzata quando la soluzione della disequazione non è una sola

    Parameters
    ----------
    a : float
        numeratore
    b : float
        denominatore

    Returns
    -------
    str
        frazione ridotta ai minimi termini

    '''
    #controllo segno frazione
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        segno = 'più'
    else:
        segno = 'meno'
    
    #voglio lavorare con numeri positivi
    a = abs(a)
    b = abs(b)
    
    #a è multiplo di b??
    if a % b == 0:
        a = int(a / b)
        if segno == 'più':
            return str(a) 
        return  "-" + str(a)
    
    #semplifico l'eventuale parte pari in comune
    while a % 2 == 0 and b % 2 == 0:
        a = int(a / 2)
        b = int(b / 2)
    
    #a questo punto se hanno divisori in comune sono sicuramente dispari
    divisore = 3
    while divisore <= abs(a) and divisore <= abs(b):
        while a % divisore == 0 and b % divisore == 0:
            a = int(a / divisore )
            b = int(b / divisore)
        divisore = divisore + 2
    
    #assegno il segno alla frazione
    if segno == 'più':
        return str(a) +"/" + str(b)
    return "-" + str(a) +"/" + str(b)

def scomponi_3(a:int,b:int,c:int)-> Tuple[int, int, int]:
    '''
    riduce ai minimi termini i tre parametri

    Parameters
    ----------
    a : int
        
    b : int
        
    c : int
        

    Returns
    -------
    Tuple[int, int, int]
    '''
    #semplifico l'eventuale parte pari in comune
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a = int(a / 2)
        b = int(b / 2)
        c = int(c / 2)
    
    #a questo punto se hanno divisori in comune sono sicuramente dispari
    divisore = 3
    while divisore <= abs(a) and divisore <= abs(b) and divisore <= abs(c):
        while a % divisore == 0 and b % divisore == 0 and c % divisore == 0:
            a = int(a / divisore)
            b = int(b / divisore)
            c = int(c / divisore )
        divisore = divisore + 2
    return a,b,c
    
    
def conclusione(stringa_1:str, stringa_2:str, segno:str)->str:
  '''
    calcola la soluzione della disequazione

    Parameters
    ----------
    stringa_1 : str
        frazione più grande
    stringa_2 : str
        frazione più piccola
    segno : str
        

    Returns
    -------
    str
        risultato

  '''
  if segno == '>':
      return "x < " + stringa_2 + ", x >" + stringa_1
  elif segno == '=>':
      return "x <= " + stringa_2 + ", x =>" + stringa_1
  elif segno == '<':
      return stringa_2 + " < x < " + stringa_1
  return stringa_2 + " <= x <= " + stringa_1         
  
  
  
     
def disequazione(a:int,b:int,c:int, segno)->str:
    delta = b**2 - 4 * a * c
    
    #se il delta è negativo l'equazione ha soluzione solo se positiva
    if delta < 0:
        if segno == '>' or segno == '=>':
            return "per ogni x"
        return "nessuna soluzione"
    
    #un quadrato è sempre positivo 
    if delta == 0:
        if segno == '=>':
            return "per ogni x"
        elif segno == '>':
            return "per ogni x eccetto " + semplifica(-b, 2*a)
        elif segno == '<=':
            return semplifica(-b, 2*a)
        return "nessuna soluzione"
    
    a = 2 * a
    b = - b
    delta = porta_fuori(delta)
    radice = delta[0]
    radicando = delta[1]
    
    # delta è un quadrato perfetto???
    if radicando == 1: 
        numeratore_1 = b + radice
        numeratore_2 = b - radice 
        stringa_1 = scomponi_2(numeratore_1, a)
        stringa_2 = scomponi_2(numeratore_2, a)
    
    #da delta non è possibile portare fuori nulla?? 
    elif radice == 1:
        stringa_1 = "[" + str(b) + "+ radice(" +str(radicando) +")] / " +str(a)
        stringa_2 ="[" + str(b) + "- radice(" +str(radicando) +")] / " +str(a)
    
    else:
        lista = scomponi_3(radice, b, a)
        radice = lista[0]
        b = lista[1]
        a = lista[2] 
        if a == 1 and radice == 1:
            stringa_1 = str(b) + "+ radice(" +str(radicando) +")"
            stringa_2 = str(b) + "- radice(" +str(radicando) +")"
        elif a == 1:
            stringa_1 = str(b) + " + " + str(radice) + " * radice(" + str(radicando) +")"
            stringa_2 = str(b) + " - " + str(radice) + " * radice(" + str(radicando) +")"
        elif radice == 1:
            stringa_1 = "[" + str(b) + "+ radice(" +str(radicando) +")] / " + str(a)
            stringa_2 = "[" + str(b) + "- radice(" +str(radicando) +")] / " + str(a)
        else:
            stringa_1 = "[" + str(b) + " + " + str(radice) + " * radice(" + str(radicando) +")] /" + str(a)
            stringa_2 = "[" + str(b) + " - " + str(radice) + " * radice(" + str(radicando) +")] /" + str(a)
    return conclusione(stringa_1, stringa_2, segno)
            
def check_number()-> float:
    '''
    controlla che il numero inserito sia realmente in numero

    Returns
    -------
    float
        numero
    '''
    while True: 
        numero = input()
        try:
            numero = float(numero)
        except ValueError:
            print("non hai inserito un numero riprova")
        else:
            return numero
            
        
            
print("inserisci i valori del termine di secondo grado, primo grado e del termine noto")
a = check_number()
b = check_number()
c = check_number()

print("inserisci il segno della diseguazione")
segno = input()
if (segno in ['<', '<=', '>', '=>']) == False:
    raise ValueError(f"non hai inserito un segno accettabile")
    
# se a, b o  c è razionale lo trasformo in intero 
while (a != int(a)) or (b != int(b)) or (c != int(c)):
    a = a * 10
    b = b * 10
    c = c * 10
    
print(f'la disequazione {int(a)} * x ** 2 + {int(b)} * x + {int(c)} {segno} 0 ha come risultato: {disequazione(a, b,c,segno)}' )

