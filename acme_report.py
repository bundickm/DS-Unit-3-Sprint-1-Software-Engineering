'''
module to create and report on Acme products
'''
from random import choice, randint, uniform
from acme import Product


def generate_products(quantity=30):
    '''
    generate a random assortment of fine Acme products

    Input:
    quantity: int, default 30, how many products to create

    Output:
    products: list of n Product objects, where n = quantity
    '''
    products = []
    adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

    # create products with random values and append to products
    for _ in range(quantity):
        name = (choice(adjective) + ' ' + choice(noun))
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name=name, price=price,
                                weight=weight, flammability=flammability))

    return products


def inventory_report(products):
    '''
    create a report based off a list of Acme products

    Input:
    products: list of Product objects

    Output:
    print report to screen
    '''
    unique_names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    product_count = len(products)

    # gather information for report
    for product in products:
        unique_names.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    # print report to screen
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(set(unique_names)))
    print('Average price:', (total_price/product_count))
    print('Average weight:', (total_weight/product_count))
    print('Average flammability:', (total_flammability/product_count))


if __name__ == '__main__':
    inventory_report(generate_products())
