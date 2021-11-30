import pymongo

from apero import generate_apero
from blessure import generate_blessure
from identity import generate_identity

client = pymongo.MongoClient()
db = client.formation

nb_apero = 100_000
aperos = [generate_apero() for i in range(nb_apero)]
result = db.Apero.insert_many(aperos)
print("Insert successful : ", result.acknowledged)

nb_identity = 30_000
identitys = []
for i in range(nb_identity):
  new_identity = generate_identity()
  identitys.append(new_identity)
result = db.Identites.insert_many(identitys)
print("Insert successful : ", result.acknowledged)

nb_blessures = 300_000
blessures = [generate_blessure() for i in range(nb_blessures)]
result = db.Blessures.insert_many(blessures)
print("Insert successful : ", result.acknowledged)
