from Customers import Customer
import numpy as np
from faker import Faker

class Supermarket:
    '''
    The supermarket class
    '''
    def __init__(self, timesteps=10) -> None:
        self.customer_list = []
        self.timesteps = timesteps
        self.time=0
        self.activecustomers=0

    def __repr__(self) -> str:
        return f'At time {self.time}, there are {self.activecustomers} in the super market'

    def add_customer(self):
        '''
        Uses Faker to add ONE customer to the Supermarket class and provides a random name
        '''
        f = Faker()
        name = f.name()
        c=Customer(name)
        self.customer_list.append(c)

    def add_customers(self, number):
        '''
        Parameters:
        number : integer 
        Adds a list of customers to the supermarket
        '''
        for i in range(number):
            self.add_customer()

    def simulate(self, no_of_customers):
        '''
        Parameters:
        no_of_customers : integer
        Runs the simulation with no_of_customers in the supermarket
        '''
        s.add_customers(no_of_customers)
        print('-----The list of customers added-----')
        s.customer_list()
        print('\n')
        print('-----SIMULATION BEGIN-----')
        while self.timesteps>0:
            s.next_timestep()
            s.timesteps-=1
        print('----- SIMULATION END -----')
        print(self)

    def move_all(self):
        for customer in self.customer_list:
            customer.move()

    def next_timestep(self):
        self.time+=1
        self.move_all()

    def customer_list(self):
        for customer in self.customer_list:
            print(customer)





if __name__=='__main__':
    s=Supermarket()
    s.simulate(5)