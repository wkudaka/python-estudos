

def mean(x):
    return sum(x) / len(x)


def median(v):
    #@TODO: implementar https://en.wikipedia.org/wiki/Quickselect
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        #se for impar, retorna do valor do meio do vetor
        return sorted_v[midpoint]
    else:
        #se for par, retorna a média dos valores do meio do vetor
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]
