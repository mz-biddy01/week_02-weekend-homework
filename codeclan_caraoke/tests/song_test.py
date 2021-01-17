import unittest

from src.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("water under the bridge")
        
    
    def test_song_has_a_title(self):
        self.assertEqual("water under the bridge", self.song1.title)

