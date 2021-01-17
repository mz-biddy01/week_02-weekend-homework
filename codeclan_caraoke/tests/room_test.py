import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("G23", 2)
        self.guest = Guest("Johnny Bravo")
        self.guest2 = Guest("Paul Cann")
        self.guest3 = Guest("Matt Barn")
        self.song1 = Song("water under the bridge")
    
    def test_room_has_a_name(self):
        self.assertEqual("G23", self.room1.name)

    def test_room_has_capacity_to_admit_guest(self):
        expected_answer = "Welcome"
        actual_answer = self.room1.check_in(self.guest)
        self.assertEqual(expected_answer, actual_answer)

    def test_guests_can_check_into_the_room(self):
        expected_answer = "Johnny Bravo" # Arrange -> the things I need for my test
        self.room1.check_in(self.guest) # Act -> call the method/function under test
        actual_answer = self.room1.guest_list[0] # Act -> what you get back from calling your method/function 
        self.assertEqual(expected_answer, actual_answer) # Assert -> check that expected and actual match

    def test_guests_can_check_out_of_the_room(self):
        self.room1.check_in(self.guest)
        self.room1.check_out(self.guest)
        self.assertEqual(0, len(self.room1.guest_list))
        # self.assertNotIn(self.room1.guest_list, self.guest.name)

    def test_no_song_in_the_room(self):
        self.assertEqual(0, len(self.room1.playlist))

    def test_song_can_be_added_to_room(self):
        self.room1.add_song(self.song1)
        self.assertIn(self.song1.title, self.room1.playlist)

    def test_when_there_is_no_capacity_for_another_guest(self):        
        expected_answer = "try again later"
        self.room1.check_in(self.guest)
        self.room1.check_in(self.guest2)
        actual_answer = self.room1.check_in(self.guest3)
        self.assertEqual(expected_answer, actual_answer)