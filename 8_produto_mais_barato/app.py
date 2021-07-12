products = {}
cheaper = 999999

for product in range(3):
    product_name = input(f"Digite o nome do produto {product+1}\n")
    product_price = float(input(f"Digite o valor do produto {product+1}\n"))
    
    products[product_name] = product_price

for product in products:
    if (products[product] < cheaper):
        cheaper = products[product]
        cheaper_product = product

print('O produto mais barato é o: ', cheaper_product)