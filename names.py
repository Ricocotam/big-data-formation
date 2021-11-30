import random
import pandas

# Download : wget https://www.data.gouv.fr/fr/datasets/r/9ae80de2-a41e-4282-b9f8-61e6850ef449
noms = pandas.read_csv("patronymes.csv")
noms = noms[noms["count"] > 2000]
noms = noms["patronyme"].tolist()

# Download : wget https://www.data.gouv.fr/fr/datasets/r/4b13bbf2-4185-4143-92d3-8ed5d990b0fa
prenoms = pandas.read_csv("prenom.csv")
prenoms = prenoms[prenoms["count"] > 5000]
prenoms = prenoms["prenoms"].tolist()

def get_random_nom():
    i = random.randint(0, len(noms) - 1)
    return noms[i]


def get_random_prenom():
    i = random.randint(0, len(prenoms) - 1)
    return prenoms[i]