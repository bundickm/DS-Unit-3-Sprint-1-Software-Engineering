'''
module for creating fine acme products
'''

from random import randint


class Product:
    '''
    Create generic acme products, this is the clay from
    which other products are born

    functions:
    __init_
    stealability
    explode
    '''
    def __init__(self, name, price=10, weight=20,
                 flammability=.5, identifier=randint(1000000, 9999999)):
        '''
        function for instantiation of Product

        Input:
        name: string, name of the product
        price: int, default 10
        weight: int, default 20
        flammability: float, default .5, Product with flammability
                      over 50 have extreme volatility
        identifier: int, randomly assigned ID number
        '''
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        calculate the how stealable a product is based on price and weight

        Output:
        return string of a phrase summarizing stealability ratio
        '''
        steal_ratio = self.price / self.weight
        if steal_ratio < .5:
            return 'Not so stealable...'
        elif steal_ratio < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        '''
        calculate the how explodey a product is based on
        flammability and weight

        Output:
        return string of a phrase summarizing explosive rating
        '''
        volatility = self.flammability * self.weight
        if volatility < 10:
            return '...fizzle'
        elif volatility < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''
    Acme boxing glove, another fine Acme Product

    functions:
    __init__
    explode
    punch
    '''
    def __init__(self, name, price=10, weight=10,
                 flammability=.5, identifier=randint(1000000, 9999999)):
        '''
        function for instantiation of BoxingGlove
        overwrite some of the default values for Product
        '''
        Product.__init__(self, name, price, weight, flammability, identifier)

    def explode(self):
        '''
        overwrite explode function to remind you gloves usually aren't volatile
        '''
        return "...it's a glove."

    def punch(self):
        '''
        translate the glove weight into an assessment of how much it
        will hurt to be hit by

        Output:
        return phrase assess punch hurtiness
        '''
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
