class Customer:
    def __init__(self,id_num,arrival_time):
        self._id_num = id_num
        self._arrival_time = arrival_time
    def id_num(self) :
        return self._id_num     
    def time_arrived( self ) :
        return self._arrival_time
class Cashier:
    def __init__(self,id_num):
        self._id_num = id_num
        self._customer = None
        self._stop_time = -1
    def id_num( self ):
        return self._id_num
    def is_free( self ):
        return self._customer is None
    def is_finished( self, cur_time ):
        return self._customer is not None and self._stop_time == cur_time
    def start_service( self, customer, stop_time ):
        self._customer = customer
        self._stop_time = stop_time
    def stop_service( self ):
        the_customer = self._customer
        self._customer = None
        return the_customer