
import numpy as np
from transition import TRANSITION_MATRIX

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, location='entry', transition_probs=TRANSITION_MATRIX, budget=100):
        '''
        Customer attributes
        name : of the customer
        location : in the supermarket
        budget : amout carried by the customer
        path : path of traveresed by the customer in the supermarket
        TM : Transition matrix calculated from the data
        active : is the customer still in the supermarket? 
        total_time - the customer spends in the supermarket
        '''
        self.name = name
        self.location = location
        self.budget = budget
        self.path = [location]
        self.TM = transition_probs
        self.active =True
        self.total_time = 0

    def __repr__(self):
        '''
        __repr__ Enables the use the print(Customer) method to print the class in this format
        '''
        return f'<Customer {self.name} is in {self.location}>'
    
    def move(self):
        '''
        Propagates the customer to the next location.
        Returns nothing.
        '''
        #if (self.active and self.location is 'entry'):
            #self.location = np.random.choice(['spices', 'drinks', 'fruit', 'dairy'], p=self.TM[self.location][0:4],replace=True)
            #self.path.append(self.location)
        if (self.active):# and self.location != 'entry'):
            self.location = np.random.choice(['entry', 'dairy', 'drinks', 'fruit', 'spices', 'checkout'], p=self.TM[self.location],replace=False)
            self.path.append(self.location)
            self.total_time+=1
            if (self.location == 'checkout'):
                 self.active=False
                 print(f'Customer {self.name} is checking out')


if __name__=='__main__':
    c1 = Customer('Pradnya')
    c2 = Customer('Santiago')
    c3 = Customer('Puviy')
    
    customer_list = [c1,c2, c3]
    for customer in customer_list:
        print(customer)
        customer.move()
        print(customer)
        customer.move()
        print(customer)
        customer.move()
        print(customer)
    print(c1.path)
    print(c2.path)
    print(c3.path)
    print(f'{c1.name} spent {c1.total_time} minutes in the supermarket.')
    print(f'{c2.name} spent {c2.total_time} minutes in the supermarket.')
    print(f'{c3.name} spent {c3.total_time} minutes in the supermarket.')

