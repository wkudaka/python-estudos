import math

#pdf = probability density function
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


#cdf = cumulative distribution function
def uniform_cdf(x):
    if x < 0:   return 0
    elif x < 1: return x
    else:       return 1

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):

    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z,  hi_p  =  10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # considera o ponto medio...
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            #se o ponto medio for muito pequeno, procura acima
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # se for muito grane procura abaixo
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z
