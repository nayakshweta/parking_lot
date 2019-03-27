from slot import Slot

class Parking_Lot:

    def __init__(self, number_of_slots):
        self.number_of_slots = int(number_of_slots)
        self.car_slots = []
        self.bike_slots = []

        n = 1
        while n <= self.number_of_slots:
            slot = Slot(n)
            self.car_slots.append(slot)
            n += 1
        
        n = 1
        while n <= self.number_of_slots:
            slot = Slot(n)
            self.bike_slots.append(slot)
            n += 1

        print "Created a parking lot with " + str(self.number_of_slots) + " car and bike slots each"


    def find_closest_empty_slot_for_car(self):
        n = 1
        closest_empty_slot = 0

        while n <= self.number_of_slots:
            if self.car_slots[n - 1].occupied_status == False:
                closest_empty_slot = self.car_slots[n - 1]
                break
            n += 1
        return closest_empty_slot

    def find_closest_empty_slot_for_bike(self):
        n = 1
        closest_empty_slot = 0

        while n <= self.number_of_slots:
            if self.bike_slots[n - 1].occupied_status == False:
                closest_empty_slot = self.bike_slots[n - 1]
                break
            n += 1
        return closest_empty_slot


    def get_new_ticket(self, vehicle_number, vehicle_color, vehicle_type):

        if vehicle_type == 'Car':
            closest_empty_slot = self.find_closest_empty_slot_for_car()
        elif vehicle_type == 'Bike':
            closest_empty_slot = self.find_closest_empty_slot_for_bike()

        if not closest_empty_slot:
            print "Sorry, parking lot is full!"
        else:
            print "Allocated slot number: " + str(closest_empty_slot.slot_number)
            closest_empty_slot.park_vehicle(vehicle_number, vehicle_color)


    def get_parking_status(self):

        print "Car Parking"
        print "==========="
        print "\nSlot No.\tRegistration Number\tColor"
        for slot in self.car_slots:
            if slot.occupied_status == True:
                print str(slot.slot_number) + '\t\t' + slot.vehicle_number + '\t\t' + slot.vehicle_color
        
        print "Bike Parking"
        print "============"
        print "\nSlot No.\tRegistration Number\tColor"
        for slot in self.bike_slots:
            if slot.occupied_status == True:
                print str(slot.slot_number) + '\t\t' + slot.vehicle_number + '\t\t' + slot.vehicle_color


    def return_parking_ticket(self, slot_number, vehicle_type):
        slot_number = int(slot_number)

        if vehicle_type == 'Car':
            slot = self.car_slots[slot_number - 1]
        elif vehicle_type == 'Bike':
            slot = self.bike_slots[slot_number - 1]

        slot.exit_vehicle()
        print "Slot Number " + str(slot_number) + " " + vehicle_type + " is free."


    def get_reg_numbers_for_vehicles_with_color(self, vehicle_color):
        list_of_cars = []
        list_of_bikes = []

        for slot in self.car_slots:
            if (slot.occupied_status == True) and (slot.vehicle_color == vehicle_color):
                list_of_cars.append(slot.vehicle_number)
        print "The cars with color " + vehicle_color + " are: " + ', '.join(list_of_cars)

        for slot in self.bike_slots:
            if (slot.occupied_status == True) and (slot.vehicle_color == vehicle_color):
                list_of_bikes.append(slot.vehicle_number)
        print "The bikes with color " + vehicle_color + " are: " + ', '.join(list_of_bikes)

        if not list_of_cars:
            print "No Cars Found"
        if not list_of_bikes:
            print "No Bikes Found"


    def get_slot_numbers_for_vehicles_with_color(self, vehicle_color):
        list_of_cars = []
        list_of_bikes = []

        for slot in self.car_slots:
            if (slot.occupied_status == True) and (slot.vehicle_color == vehicle_color):
                list_of_cars.append(str(slot.slot_number))
        print "The cars with color " + vehicle_color + " are at the slots: " +', '.join(list_of_cars)

        for slot in self.bike_slots:
            if (slot.occupied_status == True) and (slot.vehicle_color == vehicle_color):
                list_of_bikes.append(str(slot.slot_number))
        print "The bikes with color " + vehicle_color + " are at the slots: " +', '.join(list_of_bikes)

        if not list_of_cars:
            print "No Cars Found"
        if not list_of_bikes:
            print "No Bikes Found"


    def get_slot_number_for_registration_number(self, vehicle_number):
        list_of_cars = []
        list_of_bikes = []

        for slot in self.car_slots:
            if (slot.occupied_status == True) and (slot.vehicle_number == vehicle_number):
                list_of_cars.append(str(slot.slot_number))
        print "Car Parking: " + ', '.join(list_of_cars)

        if not list_of_cars:
            print "No Cars Found"

        for slot in self.bike_slots:
            if (slot.occupied_status == True) and (slot.vehicle_number == vehicle_number):
                list_of_bikes.append(str(slot.slot_number))
        print "Bike Parking: " + ', '.join(list_of_bikes)

        if not list_of_bikes:
            print "No Bikes Found"