import pickle
import json

with open("products_99.pkl", "rb") as file:
    products = pickle.load(file)

products = dict(map(lambda x: (x["name"], x["price"]), products))

with open("price_info_99.json", "rb") as file:
    commands = json.load(file)

methods = {"sum" : lambda x, p : x + p,
           "sub" : lambda x, p : x - p,
           "percent+" : lambda x, p : x * (1 + p),
           "percent-" : lambda x, p : x * (1 - p)
           }

for c in commands:
    method = methods[c["method"]]
    products[c["name"]] = method(products[c["name"]], c["param"])

with open("result.pkl", "wb") as file:
    file.write(pickle.dumps(products))