import json
import msgpack

with open("products_99.json", "rb") as file:
    data = json.load(file)

productPrices = {}

for record in data:
    if record["name"] not in productPrices:
        productPrices[record["name"]] = []
    productPrices[record["name"]].append(record["price"])

productInfo = []

for name, prices in productPrices.items():
    productInfo.append({"name" : name,
                        "min" : min(prices),
                        "max" : max(prices),
                        "avg" : sum(prices) / len(prices)})

with open("result.json", "w") as file:
    file.write(json.dumps(productInfo))

with open("result.msgpack", "wb") as file:
    file.write(msgpack.dumps(productInfo))


