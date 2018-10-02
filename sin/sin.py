from math import pi


def sin1(x):
    # A FAIRE: remplacer ce "return x" par le vrai calcul du sinus.
    
    sinx = 0
    for indice in range(0,15):

        factorielle = 1

        for j in range(1,2*indice+2):

            factorielle = j*factorielle

        sinx = sinx +((-1)**indice)*((x**(2*indice+1))/factorielle)
    
    return sinx

def cos1(y):
    # A FAIRE: remplacer ce "return x" par le calcul du cosinus par son développement de Taylor.
    
    cosy = 0
    for indice in range(0,15):

        factorielle = 1

        for j in range(1,2*indice+1):

            factorielle = j*factorielle

        cosy = cosy +((-1)**indice)*((y**(2*indice))/factorielle)

    return cosy

def sin2(x):
    # On se ramène à un calcul avec x positif ou nul:
    signe = 1
    if x < 0:
        x = -x
        signe = -signe
    # A FAIRE: normaliser et appeler sin1(x) avec x dans [0, pi/2]

    
    
    return signe * sin1(x)


def sin3(x):
    # On se ramène à un calcul avec x positif ou nul:
    signe = 1
    if x < 0:
        x = -x
        signe = -signe
    # A FAIRE: normaliser x dans [0, pi/2]
    y = pi/2 - x
    return signe * cos1(y)

def sin4(x):
    # On se ramène à un calcul avec x positif ou nul:
    signe = 1
    if x < 0:
        x = -x
        signe = -signe
    # A FAIRE: normaliser x dans [0, pi/2]
    # A FAIRE: selon la valeur pivot optimale (trouvée en comparant sin2 et sin3), utiliser sin1(x) ou cos1(y)
    if x < pi/4: # la valeur de pi/4 est à remplacer par celle (approximative) trouvée
        return signe * sin1(x)
    else:
        y = pi/2 - x
        return signe * cos1(y)
