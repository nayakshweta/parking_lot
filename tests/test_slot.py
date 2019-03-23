from unittest import TestCase
from slot import Slot

class TestSlot(TestCase):

    def test_initialize_slot(self):
        slot_number = 1
        slot = Slot(slot_number)

        assert slot.slot_number == 1
        assert slot.occupied_status == False
    
    def test_park_car(self):
        slot_number = 1
        slot = Slot(slot_number)
        slot.park_car('KA-03-BB-1234', 'White')

        assert slot.occupied_status == True
        assert slot.car_number == 'KA-03-BB-1234'
        assert slot.car_color == 'White'
        
