
class Seller:
    def __init__(self,id_num):
        self._id_num = id_num
        self._buyer = None
        self._stop_time = -1
    def id_num( self ):
        return self._id_num
    def is_free( self ):
        return self._buyer is None
    def is_finished( self, cur_time ):
        return self._buyer is not None and self._stop_time == cur_time
    def start_service( self, buyer, stop_time ):
        self._buyer = buyer
        self._stop_time = stop_time
    def stop_service( self ):
        the_buyer = self._buyer
        self._buyer = None
        return the_buyer
class Buyer:
    def __init__(self,id_num,arrival_time):
        self._id_num = id_num
        self._arrival_time = arrival_time
    def id_num(self) :
        return self._id_num     
    def time_arrived( self ) :
        return self._arrival_time