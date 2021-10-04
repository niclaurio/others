from typing import Tuple


def semplifica(a:int, b:int)-> str:
  '''
    riduce la frazione ai minimi termine
    utilizzata ogni qualvolta la soluzione dell'equazione è un numero razionale

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
  #controllo segni
  if (a < 0 and b < 0) or (a > 0 and b > 0):
    segno = 'più'
  else:
    segno = 'meno'
    
  #voglio solo numeri positivi
  a = abs(a)
  b = abs(b)
  
  # a è multiplo di b ??
  if a % b == 0:
    a = int(a/b)
    if segno == 'più':
      return "x = " + str(a)
    else:
      return " x = -" + str(a)
  
  #semplifico l'eventuale parte pari in comune
  while a % 2 == 0 and b % 2 == 0:
    a = int(a / 2)
    b = int(b / 2)
  
  #a questo punto se hanno divisori in comune sicuramente sono dispari  
  divisore = 3
  while (divisore) <= a and (divisore) <= b:
    while a % divisore == 0 and b % divisore == 0:
      a = int(a / divisore)
      b = int(b / divisore)
    divisore = divisore + 2
    
  #assegno il segno al risultato
  if segno == 'più':
    return "x = " + str(a) + "/" + str(b)
  return "x = -" + str(a) + "/" + str(b)



def porta_fuori(delta:int)-> Tuple[int, int]:
  '''
    porta fuori dalla radice delta

    Parameters
    ----------
    delta : int

    Returns
    -------
    Tuple[int, int]
        radice:int
               parte portata fuori dalla radice 
        delta: int
             parte rimasta sotto radice

    '''
  radice = 1
  
  #porto fuori l'eventuale
  while delta % 4 == 0:
    delta = int(delta / 4)
    radice = radice * 2
  
  #a questo punto se posso portare fuori qualcosa sicuramente sarà una quantità dispari
  # affinche sia un divisore il quadrato dovrà essere <= di delta
  divisore = 3
  quadrato = 9
  while quadrato <= delta:
      #per portare fuori dalla radice devo dividere per il quadrato di un numero
      #quello che risulterà fuori dalla radice sarà il numero
    while delta % quadrato == 0:
      delta = int(delta / quadrato)
      radice = radice * divisore
    divisore = divisore + 2
    quadrato = divisore ** 2
  return (radice, delta)

def scomponi(n1:int,n2:int,n3:int)->Tuple[int, int, int]:
  '''
    riduce i tre numeri ai minimi termini
    utilizzato nel caso in cui la soluzione non sia un numero razionale ma presenti una radice
    Parameters
    ----------
    n1 : int
        .
    n2: int
      
    n3 : int
    

    Returns
    -------
    Tuple[int, int, int]
       n1,n2,n3 ridotti ai minimi termini

  '''
  while n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
    n1 = int(n1 / 2)
    n2 = int(n2 / 2)
    n3 = int(n3 / 2)
  divisore = 3
  while (divisore <= abs(n1) or n1 == 0) and divisore <= abs(n2) and divisore <= abs(n3):
    while n1 % divisore == 0 and n2 % divisore == 0 and n3 % divisore == 0:
      n1 = int(n1 / divisore)
      n2 = int(n2 / divisore)
      n3 = int(n3 / divisore)
    divisore = divisore + 2
  return (n1,n2,n3)


def soluzione(b:int, radice:int, a:int, radicando:int)->str:
  '''
  utilizzato nel caso in cui la soluzione non sia un numero razionale ma presenti una radice
  calcola la soluzione dell'equazione
  i termini in input b, radice ed a sono stati ridotti ai minimi termini con scomponi 

    Parameters
    ----------
    b : int
        termine primo grado dell'equazione
    radice : int
        termine fuori dalla radice
    a : int
        termine secondo grado dell'equazione; nella soluzione indica il denominatore
    radicando : int
        termine dentro la radice

    Returns
    -------
    str
       x1 = soluzione1, x2= soluzione2 

    '''
  #ho suddiviso in vari casi perchè per esempio non ha senso dividere per denominatore 1 o sommare per b = 0
  if b == 0 and a == 1 and radice == 1:
   return "x = radice(" +str(radicando) + "), x = -radice(" +str(radicando) + ")"
  
  elif a == 1 and radice == 1:
    return "x = " + str(b) +" + radice(" + str(radicando) + "), x = " + str(b) + " - radice(" + str(radicando) + ")"

  elif a == 1 and b == 0:
    return "x = " + str(radice) + "* radice (" + str(radicando) + ") , x = -"+ str(radice) + "* radice (" + str(radicando) + ")"

  elif b == 0 and radice == 1:  
    return " x = radice(" + str(radicando) + ") / " + str(a) + " , x = - radice("+ str(radicando) + ") / " + str(a)

  elif b == 0:
    return "x = " +str(radice) + "*radice(" + str(radicando) + ") / " + str(a)  +", x = -" +str(radice) + "*radice(" + str(radicando) + ") / " + str(a) 

  elif a == 1: 
    return "x = " +str(b) + " + " + +str(radice) + "*radice(" + str(radicando) + "), x = " +str(b) + " - " + +str(radice) + "*radice(" + str(radicando) + ")"

  elif radice == 1:
    return "x = [" + str(b) + " + radice(" + str(radicando) + ")] /" + str(a) + ", x = [" + str(b) + " - radice(" + str(radicando) + ")] /" + str(a)

  # siamo per forza nel caso generale b != 0 a != 1 e radice != 1
    return " x = [" + str(b) + " + " + str(radice) + "* radice(" + str(radicando) + ")] /" + str(a) + ", x = [" + str(b) + " - " + str(radice) + "* radice(" + str(radicando) + ")] /" + str(a)
  



def equazione(a:int, b:int, c:int) ->str:
  '''
    funzione ricapitolativa

    Parameters
    ----------
    a : int
        termine secondo grado
    b : int
       termine primo grado
    c : int
        termine noto

    Returns
    -------
    str
        soluzione

    '''
  delta = b ** 2 - 4 * a * c
  if a == 0 and b == 0 and c == 0:
    return "indeterminato"
  elif delta < 0 or (a == 0 and b == 0):
    return "Impossibile"
  elif a == 0:
    c = -c 
    return semplifica(c, b)
  elif delta == 0:
    b = -b
    a = 2 * a
    return semplifica(b, a)
  b = -b
  a = 2 * a
  lista = porta_fuori(delta)
  radice = lista[0]
  radicando = lista[1]
  if radicando == 1:
    numeratore_1 = b + radice
    numeratore_2 = b - radice
    return semplifica(numeratore_1, a) + ", " + semplifica(numeratore_2, a)
  elif radice == 1: 
    return "x = [" + str(b) + "+ radice(" + str(radicando) +")] /" + str(a) + ", x = ["+ str(b) + "- radice(" + str(radicando) +")] /" + str(a) 
  lista = scomponi(b, radice, a)
  b = lista[0]
  radice = lista[1]
  a = lista[2]
  return soluzione(b,radice,a, radicando)
  



#inserisco i valori delle incognite e stampo il risultato
if __name__ == "__main__" : #esegue solo se il codice non è richiamato in altro script
    print("inserisci i valori del termine di secondo grado, primo grado e del termine noto")
    a = float(input())
    b = float(input())
    c = float(input())
    
    #voglio che siano tutti numeri interi non razionali
    while a != int(a) or b!= int(b) or c != int(c):
        a = a * 10
        b = b * 10
        c = c * 10
    a = int(a)
    b = int(b)
    c = int(c)
    
    #se il primo termine è negativo cambio di segno tutti i termini
    if a < 0:
        a = - a
        b = - b
        c = - c
    print("l'equazione " +str(a) + "*x**2 + " + str(b) +"*x + " + str(c) +" ha come soluzioni: " +str(equazione(a,b,c)))
    