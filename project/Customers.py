
import random
from transition import TRANSITION_MATRIX

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, location, transition_probs=TRANSITION_MATRIX, budget=100):
        self.name = name
        self.location = location
        self.budget = budget
        self.path = [location]
        self.TM = transition_probs
        self.active =True

    def __repr__(self):
        return f'<Customer {self.name} in {self.location}>'
    
    def move(self):
        '''
        Propagates the customer to the next location.
        Returns nothing.
        '''
        if self.active:
            self.location = random.choice(['spices', 'drinks', 'fruit', 'dairy', 'checkout'], p=self.TM[self.location])
            self.path.append(self.location)
            if (self.location == 'checkout'):
                 self.active=False
                 print(f'Customer {self.name} is checking out')

    def printer(self):
        self.move()


if __name__=='__main__':
    c1 = Customer('Pradnya', location='spices')
    c2 = Customer('Santiago', location='drinks')
    c3 = Customer('Puviy', location='dairy')
    
   
    customer_list = [c1,c2,c3]
    for customer in customer_list:
        print(customer)
