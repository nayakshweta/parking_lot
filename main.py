import sys, cmd
from parking_lot import Parking_Lot
from slot import Slot

class ParkingLotShell(cmd.Cmd):
    intro = "Welcome to the Parking System. Type ? to list commands. \n"
    prompt = '<parking system>'

    #----- parking lot commands -----#
    def do_create_parking_lot(self, args):
        global parking_lot
        parking_lot = Parking_Lot(args[0])
    
    def do_park(self, args):
        parking_lot.get_new_ticket(args[0], args[1])
    
    def do_leave(self, args):
        parking_lot.return_parking_ticket(args[0])
    
    def do_status(self, args):
        parking_lot.get_parking_status()
    
    def do_get_reg_numbers_for_cars_with_color(self, args):
        parking_lot.get_reg_numbers_for_cars_with_color(args[0])
    
    def do_slot_numbers_for_cars_with_colour(self, args):
        parking_lot.get_slot_numbers_for_cars_with_color(args[0])

    def do_slot_number_for_registration_number(self, args):
        parking_lot.get_slot_number_for_registration_number(args[0])

if __name__ == '__main__':
    ParkingLotShell().cmdloop()