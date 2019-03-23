class Slot:

    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.occupied_status = False
    
    def park_car(self, car_number, car_color):
        self.car_number = car_number
        self.car_color = car_color
        self.occupied_status = True
    
