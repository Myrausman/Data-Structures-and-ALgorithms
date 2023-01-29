from myarray import Array
from llistqueue import Queue
from customer import Cashier,Customer

import random

class GroceryStoreSimulation:
    # Create a simulation object.
    def __init__(self, num_clerks, num_minutes, between_time, service_time):
        # Parameters supplied by the user.
        self._arrive_prob = 1.0 / between_time
        self._service_time = service_time
        self._num_minutes = num_minutes

        # Simulation components.
        self._customer_q = Queue()
        self._the_cashiers= Array(num_clerks)
        for i in range(num_clerks):
            self._the_cashiers[i] = Cashier(i + 1)

        # Computed during the simulation.
        self._total_wait_time = 0
        self._num_customers = 0
        self._total_revenue = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for cur_time in range(self._num_minutes + 1):
            self._handle_arrival(cur_time)
            self._handle_begin_service(cur_time)
            self._handle_end_service(cur_time)

    # Print the simulation results.
    def print_results(self):
        num_served = self._num_customers - len(self._customer_q)
        avg_wait = float(self._total_wait_time) / num_served
        print("")
        print("Number of customers served = ", num_served)
        print("Number of customers remaining in line = %d" %
              len(self._customer_q))
        print("The average wait time was %4.2f minutes." % avg_wait)
        print("Total revenue generated: $%d" % self._total_revenue)

    def _handle_arrival(self, cur_time):
        p = random.random()
        if p < self._arrive_prob:    # a passenger should arrive
            customer = Customer( self._num_customers, cur_time )
      
            self._customer_q.enqueue(customer)

            print('Time ', cur_time, ': customer ',
                  self._num_customers, ' arrived.')

            self._num_customers += 1

    
    def _handle_begin_service( self, cur_time ):
        if self._customer_q.isEmpty() == False:   
            # handle a customer
            cashier_ID = self._find_free_cashier()
            if cashier_ID >= 0: 
                # found a free one
                this_customer = self._customer_q.dequeue()
                stop_time = cur_time + self._service_time
                self._the_cashiers[ cashier_ID ].start_service( this_customer, stop_time )

                self._total_wait_time += cur_time - this_customer._arrival_time

                print( 'Time ', cur_time, ': Cashier ', cashier_ID, \
                        ' started serving customer ', this_customer.id_num(), '.' )

    def _handle_end_service( self, cur_time ):
        cashier_ID = self._find_finish_cashier( cur_time )
        if cashier_ID >= 0:    # found one who should complete the service
            this_customer = self._the_cashiers[ cashier_ID ].stop_service()
        
            print( 'Time ', cur_time, ': Cashier ', cashier_ID, \
                    ' stopped serving customer ', this_customer.id_num(), '.' )

    def _find_free_cashier( self ):
        for i in range( len( self._the_cashiers ) ):
            if self._the_cashiers[ i ].is_free():
                return i   # found a free one
            return -1      # no free cashier is found

    def _find_finish_cashier( self, cur_time ):
        for i in range( len( self._the_cashiers ) ):
            if self._the_cashiers[ i ].is_finished( cur_time ):
                return i   # found a finished one
            return -1      # no finished cashier is found
# Set the simulation parameters.
clerks = 4
minutes = 300
between_time = 30
service_time = 25

# Create a simulation object and run the simulation.
sim = GroceryStoreSimulation(clerks, minutes, between_time, service_time)
sim.run()

# Print the results of the simulation.
sim.print_results()