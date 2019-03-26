import sys, cmd
from parking_lot import Parking_Lot
from slot import Slot
import pickle


class ParkingLotShell(cmd.Cmd):
    intro = "Welcome to the Parking System. Type ? to list commands. \n"
    prompt = '<parking system>'

    if not sys.stdin:
        use_rawinput = True
    else:
        use_rawinput = False

    try:
        parking_dbfile = open('parkingPickle', 'rb')
        parking_lot = pickle.load(parking_dbfile)
    except:
        parking_lot = NotImplemented

    #----- parking lot commands -----#
    def do_create_parking_lot(self, args):
        self.parking_lot = Parking_Lot(args)
    
    def do_park(self, args):
        args_list = args.split()
        self.parking_lot.get_new_ticket(args_list[0], args_list[1])
    
    def do_leave(self, args):
        self.parking_lot.return_parking_ticket(args)
    
    def do_status(self, args):
        self.parking_lot.get_parking_status()
    
    def do_registration_numbers_for_cars_with_colour(self, args):
        self.parking_lot.get_reg_numbers_for_cars_with_color(args)
    
    def do_slot_numbers_for_cars_with_colour(self, args):
        self.parking_lot.get_slot_numbers_for_cars_with_color(args)

    def do_slot_number_for_registration_number(self, args):
        self.parking_lot.get_slot_number_for_registration_number(args)

    def do_EOF(self, line):
        return True

    def do_exit(self,*args):
        parking_dbfile = open('parkingPickle', 'ab')
        pickle.dump(self.parking_lot, parking_dbfile)
        parking_dbfile.close()
        return True

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'rt') as input:
            ParkingLotShell(stdin=input).cmdloop()
    else:
        ParkingLotShell().cmdloop()
    