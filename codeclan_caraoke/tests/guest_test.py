import unittest

from src.guest import Guest


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Johnny Bravo")
        

    def test_guest_has_a_name(self):
        self.assertEqual("Johnny Bravo", self.guest.name)

    