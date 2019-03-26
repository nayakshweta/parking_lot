import sys, cmd
from parking_lot import Parking_Lot
from slot import Slot

class ParkingLotShell(cmd.Cmd):
    intro = "Welcome to the Parking System. Type ? to list commands. \n"
    prompt = '<parking system>'

    #----- parking lot commands -----#
    def do_create_parking_lot(self, args):
        global parking_lot
        parking_lot = Parking_Lot(args)
    
    def do_park(self, args):
        args_list = args.split()
        parking_lot.get_new_ticket(args_list[0], args_list[1])
    
    def do_leave(self, args):
        parking_lot.return_parking_ticket(args)
    
    def do_status(self, args):
        parking_lot.get_parking_status()
    
    def do_registration_numbers_for_cars_with_colour(self, args):
        parking_lot.get_reg_numbers_for_cars_with_color(args)
    
    def do_slot_numbers_for_cars_with_colour(self, args):
        parking_lot.get_slot_numbers_for_cars_with_color(args)

    def do_slot_number_for_registration_number(self, args):
        parking_lot.get_slot_number_for_registration_number(args)

if __name__ == '__main__':
    ParkingLotShell().cmdloop()