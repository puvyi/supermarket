from Customers import Customer
import numpy as np
from faker import Faker
import pandas as pd

class Supermarket:
    '''
    The supermarket class
    '''
    def __init__(self, timesteps=10) -> None:
        self.customer_list = []
        self.timesteps = timesteps
        self.time=0
        self.activecustomers=0
<<<<<<< HEAD
        self.path_table={}
=======
        self.path_table=pd.DataFrame(columns=['timesteps','numberofcustomers'])
>>>>>>> 5c1d6bce6d3b6bb6436f3d26c2fde7d98bdac505

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
        self.activecustomers=no_of_customers
        s.add_customers(no_of_customers)
        #print('-----The list of customers added-----')
        s.print_customer_list()
        #print('\n')
        #print('-----SIMULATION BEGIN-----')
        while self.timesteps>0:
<<<<<<< HEAD
            s.update_customer_list()
=======
            self.update_customer_list()
            self.write_timestep()
>>>>>>> 5c1d6bce6d3b6bb6436f3d26c2fde7d98bdac505
            s.next_timestep()
            s.timesteps-=1

        #print('----- SIMULATION END -----')
        #print(self)

    def move_all(self):
        for customer in self.customer_list:
            customer.move()
            #print(customer)

    def next_timestep(self):
        self.time+=1
        #self.print_customer_path()
        self.move_all()

<<<<<<< HEAD
    def update_customer_list(self):
        checkout_no=0
        for customer in self.customer_list:
            if customer.location=='checkout':
                checkout_no+=1
            
            if not customer.active:
                self.customer_list.remove(customer)
        self.activecustomers=len(self.customer_list) 
        self.path_table['checkout'] =checkout_no          



    def print_path(self):
       for customer in self.customer_list:
           print(customer.path)
           print(f'{customer.name} is spending {customer.total_time} min')
=======
    def write_timestep(self):
        new_row ={
            'timesteps':self.timesteps,
            'numberofcustomers':self.activecustomers
        }
        tempdf =pd.DataFrame(new_row, index=['index'])
        #self.path_table.loc(tempSeries)
        self.path_table=pd.concat([self.path_table, tempdf],ignore_index=True)
        print(self.path_table)


    def update_customer_list(self):
        for customer in self.customer_list:
            if not customer.active:
                self.customer_list.remove(customer)
        self.activecustomers = len(self.customer_list)

    def print_customer_path(self):
        for customer in self.customer_list:
            print(f'{customer.name} is spending {customer.total_time} minutes\n', customer.path)
>>>>>>> 5c1d6bce6d3b6bb6436f3d26c2fde7d98bdac505

    def print_customer_list(self):
        for customer in self.customer_list:
            print(customer.name)




if __name__==‘__main__‘:
    customer_per_minute = pd.read_csv(‘customer_per_minute.csv’, index_col=0)
    customer_per_minute = customer_per_minute.astype(int)
    for index in customer_per_minute:
        timestep_customers = customer_per_minute[‘customer_no_count’]
        s=Supermarket()
        s.simulate(timestep_customers) #5
        s.print_path()
    s=Supermarket()
    s.simulate(5)
<<<<<<< HEAD
    print("\n still in market\n--------")
    s.print_customer_list()
    print(s.path_table)
=======
    print('\nStill in the market\n-------------------')
    s.print_customer_list()
    s.write_timestep()
>>>>>>> 5c1d6bce6d3b6bb6436f3d26c2fde7d98bdac505
    