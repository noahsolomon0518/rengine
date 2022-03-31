from unittest import TestCase
import unittest
from rengine.config import ExerciseLoad



class TestConfig(TestCase):
    def test_enum_case(self):
        self.assertEqual(ExerciseLoad.HEAVY, "heavy", f"{ExerciseLoad.HEAVY} is not equal to heavy")
  



if __name__ == "__main__":
    unittest.main()