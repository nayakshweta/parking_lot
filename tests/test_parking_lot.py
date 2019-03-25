from unittest import TestCase
from parking_lot import Parking_Lot
from slot import Slot

class TestParkingLot(TestCase):

    def test_initialize_parking_lot(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)

        assert len(parking_lot.slots) == 6
    
    def test_get_new_ticket(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White')

        assert parking_lot.slots[0].car_number == 'KA-03-BB-1234'
        assert parking_lot.slots[0].car_color == 'White'

    def test_get_parking_status(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red')
        parking_lot.get_new_ticket('KA-03-BB-1245', 'White')
        parking_lot.get_new_ticket('KA-03-BB-1780', 'Black')
        parking_lot.get_parking_status()
    
    def test_return_parking_ticket(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red')
        parking_lot.return_parking_ticket(1)

        assert parking_lot.slots[0].car_number == 'None'
        assert parking_lot.slots[0].car_color == 'None'
        assert parking_lot.slots[0].occupied_status == False
    
    def test_get_reg_numbers_for_cars_with_color(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red')
        parking_lot.get_new_ticket('KA-03-BB-1245', 'White')
        parking_lot.get_reg_numbers_for_cars_with_color('White')
