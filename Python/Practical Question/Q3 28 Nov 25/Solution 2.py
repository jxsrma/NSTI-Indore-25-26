products = {
    "Pen": 12,
    "Notebook": 55,
    "Bag": 480,
    "Bottle": 150,
    "File": 35,
    "Pouch": 90
}

productNew = {}

for name, price in products.items():
    if price > 40 and price % 5 == 0:
        productNew[name] = price

print(productNew)

for name, price in productNew.items():
    productNew[name] = round(price * 1.1)
    
print(productNew)