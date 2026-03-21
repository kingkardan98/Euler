# Si può pensare il problema come un insieme di 100-uple, partendo dalla considerazione che,
# se si considerasse l'insieme di tutte, TUTTE le possibili 100-uple, potrebbero essere 100¹⁰⁰.
# Chiaro che la maggior parte di queste non sono 100-uple valide.

# Ho letto il teorema "stars and bars", che dice che, dati n numero somma e k lunghezza della tupla, il numero di tuple
# composte da interi non negativi la cui somma è n è pari a binom(n + k - 1, k - 1). In generale, un numero ha 2**(n-1)
# composizioni, che corrisponde al numero di partizioni di un insieme di cardinalità n.

# Vorrei poter definire le composizioni in maniera ricorsiva, calcolando le composizioni di 1, poi di 2, eccetera eccetera.

import functools

@functools.cache
def partitions(number, top):
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    result = sum(
        partitions(
            number - x, min(number - x, x)) 
            for x in range(1, top+1)
        )
    
    if number <= top:
        result += 1
    return result

print(partitions(100,100) - 1)