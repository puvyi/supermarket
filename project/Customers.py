
import random
class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, state, transition_probs=1, budget=100):
        self.name = name
        self.state = state
        self.budget = budget
        self.path = []
        self.TM = transition_probs

    def __repr__(self):
        print (f'<Customer {self.name} in {self.state}>')
    
    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        self.state = random.choice(['spices', 'drinks', 'fruit', 'dairy'])

    def is_active(self):
        '''
        Returns True if the customer has not reached the checkout yet.
        '''
        return self.state
    



if __name__=='__main__':
    c1 = Customer('Pradnya', 'spices')
    c2 = Customer('Santiago', 'drinks')
    c3 = Customer('Puviy', 'dairy')
    
    customer_list = [c1,c2,c3]
    for customer in customer_list:
        customer.__repr__()
        customer.__repr__()
        customer.__repr__()
    

