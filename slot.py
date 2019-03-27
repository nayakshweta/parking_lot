class Slot:

    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.occupied_status = False
    
    def park_vehicle(self, vehicle_number, vehicle_color):
        self.vehicle_number = vehicle_number
        self.vehicle_color = vehicle_color
        self.occupied_status = True
    
    def exit_vehicle(self):
        self.vehicle_number = 'None'
        self.vehicle_color = 'None'
        self.occupied_status = False


