import random
from names import get_random_prenom, get_random_nom


def generate_identity():
    nom = get_random_nom()
    prenom = get_random_prenom()
    jour = random.randint(1, 31)
    mois = random.randint(1, 12)
    annee = random.randint(1891, 2020)
    date_naissance = "{}/{}/{}".format(jour, mois, annee)
    dep_naissance = random.randint(1, 95)
    secu_random = "".join([str(random.randint(0, 9)) for _ in range(6)])

    return {
        "nom": nom,
        "prenom": prenom,
        "date_naissance": date_naissance,
        "dpt_naissance": dep_naissance,
        "secu1": secu_random[:3],
        "secu2": secu_random[3:]
    }