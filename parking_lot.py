from slot import Slot

class Parking_Lot:

    def __init__(self, number_of_slots):
        self.number_of_slots = number_of_slots
        self.slots = []
        n = 1
        while n <= self.number_of_slots:
            slot = Slot(n)
            self.slots.append(slot)
            n += 1
        print "Created a parking lot with 6 slots."


    def get_new_ticket(self, car_number, car_color):
        n = 1
        while n <= self.number_of_slots:
            if self.slots[n - 1].occupied_status == False:
                closest_empty_slot = self.slots[n - 1]
                break
            n += 1
            if n == self.number_of_slots:
                print "Sorry, parking lot is full!"
        print "Allocated slot number: " + str(closest_empty_slot.slot_number)
        closest_empty_slot.park_car(car_number, car_color)


    def get_parking_status(self):
        print "\nSlot No.\tRegistration Number\tColor"
        for slot in self.slots:
            if slot.occupied_status == True:
                print str(slot.slot_number) + '\t\t' + slot.car_number + '\t\t' + slot.car_color
    

    def return_parking_ticket(self, slot_number):
        slot = self.slots[slot_number - 1]
        slot.exit_car()
        print "Slot Number " + str(slot_number) + " is free."
    

    def get_reg_numbers_for_cars_with_color(self, car_color):
        list_of_cars = []

        for slot in self.slots:
            if (slot.occupied_status == True) and (slot.car_color == car_color):
                list_of_cars.append(slot.car_number)
        print ', '.join(list_of_cars)

        if not list_of_cars:
            print "Not Found"


    def get_slot_numbers_of_cars_with_color(self, car_color):
        list_of_cars = []
        
        for slot in self.slots:
            if (slot.occupied_status == True) and (slot.car_color == car_color):
                list_of_cars.append(str(slot.slot_number))
        print ', '.join(list_of_cars)

        if not list_of_cars:
            print "Not Found"


    def get_slot_number_for_registration_number(self, car_number):
        list_of_cars = []

        for slot in self.slots:
            if (slot.occupied_status == True) and (slot.car_number == car_number):
                list_of_cars.append(str(slot.slot_number))
        print ', '.join(list_of_cars)

        if not list_of_cars:
            print "Not Found"