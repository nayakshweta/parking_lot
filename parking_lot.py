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

    def get_new_ticket(self, car_number, car_color):
        n = 1
        while n <= self.number_of_slots:
            if self.slots[n - 1].occupied_status == False:
                closest_empty_slot = self.slots[n - 1]
                break
            else:
                print "No empty slots"
            n += 1
        closest_empty_slot.park_car(car_number, car_color)