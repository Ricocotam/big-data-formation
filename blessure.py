import random

from names import get_random_prenom, get_random_nom

membres = [
    "jambe",
    "bras",
    "cou",
    "tête",
    "oreille",
    "coude",
    "genou",
    "hanche",
    "pubis",
    "pied",
    "cheville",
    "main",
    "épaule",
    "côte"
]

member_side = [
    "jambe",
    "oreille",
    "coude",
    "genou",
    "pied",
    "cheville",
    "main",
    "epaule",
    "côte"
]
side = ["droit", "gauche"]

def generate_blessure():
    nom = get_random_nom()
    prenom = get_random_prenom()

    i = random.randint(0, len(membres) - 1)
    m = membres[i]
    ret = {
        "lastname": nom,
        "firstname": prenom,
        "limb": m
    }
    if m in member_side:
        s = side[random.random() > 0.5]
        ret["side"] = s
    if m == "côte":
        nb = random.gauss(1.5, 1)
        nums = set(random.randint(1, 12) for i in range(int(nb)))
        ret["limb-id"] = nums

    return ret
