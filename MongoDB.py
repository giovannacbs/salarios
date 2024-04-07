# Entering data into MongoDB

import pandas as pd
from pymongo import MongoClient

uri = [insert yours]
db = MongoClient(uri, ssl=True, tlsAllowInvalidCertificates=True)[yours]

df = pd.read_csv("pnad23.csv")
records = df.to_dict('records')

pnad = db.pnad23_gdcbs
pnad.insert_many(records)
