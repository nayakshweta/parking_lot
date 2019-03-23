from slot import Slot

class Parking_Lot:

    def __init__(self, number_of_slots):
        self.number_of_slots = number_of_slots
        self.slots = []
        n = 0
        while n < self.number_of_slots:
            slot = Slot(n)
            self.slots.append(slot)
            n += 1
