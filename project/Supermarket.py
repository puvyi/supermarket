
import Customers


class Supermarket:
    '''
    The supermarket class
    '''
    def __init__(self, steps=10) -> None:
        self.customers = []
        self.steps =steps

    def add_customers(self, customer):
        self.customers.append(customer)


    
