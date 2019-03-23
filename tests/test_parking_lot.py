from unittest import TestCase
from parking_lot import Parking_Lot

class TestSlot(TestCase):

    def test_initialize_parking_lot(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        
        assert len(parking_lot.slots) == 6