from myarray import Array
from llistqueue import Queue
from buyer import Seller ,Buyer

import random

class GroceryStoreSimulation:
    # Create a simulation object.
    def __init__(self, num_sellers, num_minutes, between_time, service_time):
        # Parameters supplied by the user.
        self._arrive_prob = 1.0 / between_time
        self._service_time = service_time
        self._num_minutes = num_minutes

        # Simulation components.
        self._buyer_q = Queue()
        self._the_sellers= Array(num_sellers)
        for i in range(num_sellers):
            self._the_sellers[i] = Seller(i + 1)

        # Computed during the simulation.
        self._total_wait_time = 0
        self._num_buyers = 0
        self._total_revenue = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for cur_time in range(self._num_minutes + 1):
            self._handle_arrival(cur_time)
            self._handle_begin_service(cur_time)
            self._handle_end_service(cur_time)

    # Print the simulation results.
    def print_results(self):
        num_served = self._num_buyers - len(self._buyer_q)
        avg_wait = float(self._total_wait_time) / num_served
        print("")
        print("Number of buyers served = ", num_served)
        print("Number of buyers remaining in line = %d" %
              len(self._buyer_q))
        print("The average wait time was %4.2f minutes." % avg_wait)
        print("Total revenue generated: $%d" % self._total_revenue)

    def _handle_arrival(self, cur_time):
        p = random.random()
        if p < self._arrive_prob:    # a passenger should arrive
            buyer = Buyer( self._num_buyers, cur_time )
      
            self._buyer_q.enqueue(buyer)

            print('Time ', cur_time, ': buyer ',
                  self._num_buyers, ' arrived.')

            self._num_buyers += 1

    
    def _handle_begin_service( self, cur_time ):
        if self._buyer_q.isEmpty() == False:   
            # handle a buyer
            seller_ID = self._find_free_seller()
            if seller_ID >= 0: 
                # found a free one
                this_buyer = self._buyer_q.dequeue()
                stop_time = cur_time + self._service_time
                self._the_sellers[ seller_ID ].start_service( this_buyer, stop_time )

                self._total_wait_time += cur_time - this_buyer._arrival_time

                print( 'Time ', cur_time, ': seller ', seller_ID, \
                        ' started serving buyer ', this_buyer.id_num(), '.' )

    def _handle_end_service( self, cur_time ):
        seller_ID = self._find_finish_seller( cur_time )
        if seller_ID >= 0:    # found one who should complete the service
            this_buyer = self._the_sellers[ seller_ID ].stop_service()
        
            print( 'Time ', cur_time, ': seller ', seller_ID, \
                    ' stopped serving buyer ', this_buyer.id_num(), '.' )

    def _find_free_seller( self ):
        for i in range( len( self._the_sellers ) ):
            if self._the_sellers[ i ].is_free():
                return i   # found a free one
            return -1      # no free seller is found

    def _find_finish_seller( self, cur_time ):
        for i in range( len( self._the_sellers ) ):
            if self._the_sellers[ i ].is_finished( cur_time ):
                return i   # found a finished one
            return -1      # no finished seller is found
# Set the simulation parameters.
sellers = 5
minutes = 480
between_time = 30
service_time = 25

# Create a simulation object and run the simulation.
sim = GroceryStoreSimulation(sellers, minutes, between_time, service_time)
sim.run()

# Print the results of the simulation.
sim.print_results()