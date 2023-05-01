import unittest
import os
from chordpro_chord import myfunctions


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.sample_chordpro_file = "data/sample_chordpro_file.chopro"
        self.sample_song = myfunctions.Song(self.sample_chordpro_file)
        self.data_folder_path = "data/"

    def test_readChordProFile(self):
        content = self.sample_song.content
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)

    def test_getChords(self):
        chords = self.sample_song.getChords()
        self.assertIsInstance(chords, list)
        for chord in chords:
            self.assertIsInstance(chord, str)

    def test_getChorus(self):
        chorus = self.sample_song.getChorus()
        self.assertIsInstance(chorus, list)
        for chord in chorus:
            self.assertIsInstance(chord, str)

    def test_getTitle(self):
        title = self.sample_song.getTitle()
        self.assertIsInstance(title, str)
        self.assertNotEqual(title, "")

    def test_getKey(self):
        key = self.sample_song.getKey()
        self.assertIsInstance(key, str)

    def test_createChordDictFromChordProFiles(self):
        chord_dict = myfunctions.createChordDictFromChordProFiles(self.data_folder_path)
        self.assertIsInstance(chord_dict, dict)
        for key, value in chord_dict.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, list)
            for chord in value:
                self.assertIsInstance(chord, str)


if __name__ == "__main__":
    unittest.main()

"""
to run this tests: python3 -m unittest test_library.py
"""
