
import numpy as np
from transition import TRANSITION_MATRIX

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, location='entry', transition_probs=TRANSITION_MATRIX, budget=100):
        self.name = name
        self.location = location
        self.budget = budget
        self.path = [location]
        self.TM = transition_probs
        self.active =True
        self.total_time = 0

    def __repr__(self):
        return f'<Customer {self.name} is in {self.location}>'
    
    def move(self):
        '''
        Propagates the customer to the next location.
        Returns nothing.
        '''
<<<<<<< HEAD
        #if (self.active and self.location is 'entry'):
            #self.location = np.random.choice(['spices', 'drinks', 'fruit', 'dairy'], p=self.TM[self.location][0:4],replace=True)
            #self.path.append(self.location)
        if (self.active):# and self.location != 'entry'):
            self.location = np.random.choice(['spices', 'drinks', 'fruit', 'dairy', 'checkout'], p=self.TM[self.location],replace=True)
=======
        if self.active:
            self.location =np.random.choice(['spices', 'drinks', 'fruit', 'dairy', 'checkout'], p =self.TM[self.location])
>>>>>>> 86b2571ef06c8a700de1201f16ca8e55257a31fe
            self.path.append(self.location)
            self.total_time+=1
            if (self.location == 'checkout'):
                 self.active=False
                 print(f'Customer {self.name} is checking out')


if __name__=='__main__':
    c1 = Customer('Pradnya')
    c2 = Customer('Santiago')
    #c3 = Customer('Puviy')
    
<<<<<<< HEAD
    customer_list = [c1,c2]
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
    print(f'{c1.name} spent {c1.total_time}.')
    print(f'{c2.name} spent {c2.total_time}.')
=======
   
    customer_list = [c1,c2,c3]
    for customer in customer_list:
        print(customer,customer.path)
>>>>>>> 86b2571ef06c8a700de1201f16ca8e55257a31fe
