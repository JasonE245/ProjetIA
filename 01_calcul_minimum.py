"""
Nom fichier: 01_calcul_minimum.py
Auteur: Jason Roger Marc Edmonds & Rodrigo Silva Riço
Date création: 12.10.26
Dernière modif: 30.10.26
Version: 1.2

But : trouver le x qui donne le plus petit résultat de f(x) = (x - 3)², sans que le programme connaisse la réponse.

"""
# ----------------------------------------------------------------------------------------------------------------------

# point de départ, choisi loin du minimum
variable_x = 5

PAS = 0.0001
TAUX_APPRENTISSAGE = 0.1

# ----------------------------------------------------------------------------------------------------------------------


def fonction(x):
    """
    Fonction dont on cherche le minimum : f(x) = (x - 3)²
    :param x: valeur d'entrée
    :return: (x - 3)²
    """
    x -= 3
    return x * x


def fonction_difference(a, b):
    """
    :param a: première valeur
    :param b: valeur à soustraire
    :return: a - b
    """
    return a - b


def fonction_derivee(difference, decalage):
    """
    Vitesse à laquelle f monte à l'endroit où on est.
    :param difference: f(x + decalage) - f(x)
    :param decalage: petit décalage utilisé pour calculer la difference
    :return: la dérivée de f en x
    """
    return difference / decalage


# ----------------------------------------------------------------------------------------------------------------------

for tours in range(300):
    resultat_1 = fonction(variable_x)
    resultat_2 = fonction(variable_x + PAS)

    diff = fonction_difference(resultat_2, resultat_1)
    derivee = fonction_derivee(diff, PAS)

    # on descend dans le sens opposé à la pente
    variable_x = variable_x - derivee * TAUX_APPRENTISSAGE

    print(tours + 1, ": ", variable_x)