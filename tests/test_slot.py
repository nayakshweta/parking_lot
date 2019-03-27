from unittest import TestCase
from slot import Slot

class TestSlot(TestCase):

    def test_initialize_slot(self):
        slot_number = 1
        slot = Slot(slot_number)

        assert slot.slot_number == 1
        assert slot.occupied_status == False
    
    def test_park_vehicle(self):
        slot_number = 1
        slot = Slot(slot_number)
        slot.park_vehicle('KA-03-BB-1234', 'White')

        assert slot.occupied_status == True
        assert slot.vehicle_number == 'KA-03-BB-1234'
        assert slot.vehicle_color == 'White'
    
    def test_exit_vehicle(self):
        slot_number = 1
        slot = Slot(slot_number)
        slot.park_vehicle('KA-03-BB-1234', 'White')
        slot.exit_vehicle()

        assert slot.vehicle_color == 'None'
        assert slot.vehicle_number == 'None'
        assert slot.occupied_status == False
        

