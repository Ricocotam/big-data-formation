import random
import datetime

from names import get_random_prenom


boissons = [
    "bière",
    "blonde",
    "IPA",
    "blanche",
    "chouffe",
    "vodka",
    "gin tonic",
    "whisky",
    "coca",
    "whisky coca",
    "jus d'orange",
    "jus d'o",
    "eau",
    "jus de tomate",
    "perrier",
    "eau petillante",
    "badoit"
]

def get_random_boisson_volume():
    i = random.randint(0, len(boissons) - 1)
    volume = int(random.gauss(2, 1))
    volume = 0 if volume < 0 else volume
    return boissons[i], volume

def generate_apero():
    timestamp = datetime.now()
    nom_personne = get_random_prenom()
    boisson, volume = get_random_boisson_volume()

    return {
        "timestamp": str(timestamp),
        "name": nom_personne,
        "nom_boisson": boisson,
        "volume": volume
    }


if __name__ == "__main__":
    print(generate_apero)
