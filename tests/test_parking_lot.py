from unittest import TestCase
from parking_lot import Parking_Lot
from slot import Slot

class TestParkingLot(TestCase):

    def test_initialize_parking_lot(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)

        assert len(parking_lot.car_slots) == 6
        assert len(parking_lot.bike_slots) == 6
    
    def test_find_closest_empty_slot_for_car(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        closest_empty_slot = parking_lot.find_closest_empty_slot_for_car()

        assert closest_empty_slot.slot_number == 1

    def test_find_closest_empty_slot_for_bike(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.bike_slots[0].occupied_status = True
        parking_lot.bike_slots[1].occupied_status = True
        closest_empty_slot = parking_lot.find_closest_empty_slot_for_bike()

        assert closest_empty_slot.slot_number == 3

    def test_get_new_ticket(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White', 'Car')

        assert parking_lot.car_slots[0].vehicle_number == 'KA-03-BB-1234'
        assert parking_lot.car_slots[0].vehicle_color == 'White'
        assert parking_lot.car_slots[0].occupied_status == True

        assert parking_lot.bike_slots[0].occupied_status == False

    def test_get_parking_status(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White', 'Car')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red', 'Bike')
        parking_lot.get_new_ticket('KA-03-BB-1245', 'White', 'Bike')
        parking_lot.get_new_ticket('KA-03-BB-1780', 'Black', 'Car')
        parking_lot.get_parking_status()
    
    def test_return_parking_ticket(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White', 'Car')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red', 'Bike')
        parking_lot.return_parking_ticket(1, 'Car')

        assert parking_lot.car_slots[0].vehicle_number == 'None'
        assert parking_lot.car_slots[0].vehicle_color == 'None'
        assert parking_lot.car_slots[0].occupied_status == False
    
    def test_get_reg_numbers_for_vehicles_with_color(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White', 'Car')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red', 'Bike')
        parking_lot.get_new_ticket('KA-03-BB-1245', 'White', 'Bike')
        parking_lot.get_reg_numbers_for_vehicles_with_color('White')
    
    def test_get_slot_numbers_of_cars_with_color(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White', 'Car')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red', 'Bike')
        parking_lot.get_new_ticket('KA-03-BB-1245', 'White', 'Bike')
        parking_lot.get_slot_numbers_for_vehicles_with_color('White')

    def test_get_slot_number_for_registration_number(self):
        number_of_slots = 6
        parking_lot = Parking_Lot(number_of_slots)
        parking_lot.get_new_ticket('KA-03-BB-1234', 'White', 'Car')
        parking_lot.get_new_ticket('KA-03-BH-1260', 'Red', 'Bike')
        parking_lot.get_new_ticket('KA-03-BB-1245', 'White', 'Bike')
        parking_lot.get_slot_number_for_registration_number('KA-03-BH-1260')
    