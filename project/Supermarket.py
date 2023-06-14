
from Customers import Customer
import numpy as np 
import pandas as pd

class Supermarket:
    '''
    The supermarket class
    '''
    def __init__(self,no_customer,steps=10):
        self.no_customer=no_customer
        self.customer_list = []
        self.steps =steps
        self.minute=0
        self.active=True
        self.activecustomers=0

    def __repr__(self) -> str:
        pass

    def add_customers(self):
        for customer_id in range(self.no_customer):
            self.customer_list.append(Customer(f'customer{customer_id}'))

    def move_all(self):
        for step in range(self.steps):
            for customer in self.customer_list:
                customer.move()

    def simulate(self):
        for customer in self.customer_list:
            print(f'{customer.name} at {customer.location}')

    def next_timestep(self):
        #time
        #move_all
        pass
        
        
                
if __name__ == '__main__':
    sample=Supermarket(5)
    sample.add_customers()
    sample.move_all()
    sample.simulate()
    



    
