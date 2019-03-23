from unittest import TestCase
from slot import Slot

class TestSlot(TestCase):

    def test_initialize_slot(self):
        slot_number = 1
        slot = Slot(slot_number)

        assert slot.slot_number == 1
        assert slot.occupied_status == False
