
import random
class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, state, budget=100):
        self.name = name
        self.state = state
        self.budget = budget
        self.path = []
        self.TM = None

    def __repr__(self):
        print (f'<Customer {self.name} in {self.state}>')
    
    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        self.state = random.choice(['spices', 'drinks', 'fruit', 'dairy'])

    def __init__(self, name, state, transition_probs, budget=100):
        

if __name__=='__main__':
    c1 = Customer('Pradnya', 'spices')
    c1.__repr__()
    c1.next_state()
    c1.__repr__()
    #print(c1)

