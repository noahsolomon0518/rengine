
import logging
from unittest import TestCase
from rengine.data_structures import StrengthExerciseQueue

import unittest


logging.basicConfig(level=logging.INFO)

class TestStrengthExerciseQueue(TestCase):
    def test_add_element_to_queue(self):
        queue = StrengthExerciseQueue()
        queue.add("exercise 1", 5)
        self.assertEqual(queue.head.exercise_name, "exercise 1")
        self.assertEqual(queue.tail.exercise_name, "exercise 1")

        queue.add("exercise 2", 10)
        self.assertEqual(queue.head.exercise_name, "exercise 1")
        self.assertEqual(queue.tail.exercise_name, "exercise 2")



        queue.add("exercise 3", 1.2)
        self.assertEqual(queue.tail.next.exercise_name, "exercise 1")
        self.assertEqual(queue.tail.exercise_name, "exercise 2")
        self.assertEqual(queue.head.exercise_name, "exercise 3")
        
        queue.add("exercise 4", -1)
        self.assertEqual(queue.head.previous.previous.exercise_name, "exercise 1")
        self.assertEqual(queue.tail.exercise_name, "exercise 2")
        self.assertEqual(queue.head.previous.exercise_name, "exercise 3")
        self.assertEqual(queue.head.exercise_name, "exercise 4")

    

    def test_get_element_from_queue(self):
        queue = StrengthExerciseQueue()
        queue.add("exercise 1", 5)
        queue.add("exercise 2", 15)
        queue.add("exercise 3", 7)
        queue.add("exercise 4", 1)
        queue.add("exercise 5", 20)
        for i in range(3):
            element = queue.get()
            self.assertEqual(element.exercise_name, "exercise 4")
            self.assertEqual(queue.head.exercise_name, "exercise 1")
            self.assertEqual(queue.tail.exercise_name, "exercise 4")

            element = queue.get()
            self.assertEqual(element.exercise_name, "exercise 1")
            self.assertEqual(queue.head.exercise_name, "exercise 3")
            self.assertEqual(queue.tail.exercise_name, "exercise 1")

            element = queue.get()
            self.assertEqual(element.exercise_name, "exercise 3")
            self.assertEqual(queue.head.exercise_name, "exercise 2")
            self.assertEqual(queue.tail.exercise_name, "exercise 3")

            element = queue.get()
            self.assertEqual(element.exercise_name, "exercise 2")
            self.assertEqual(queue.head.exercise_name, "exercise 5")
            self.assertEqual(queue.tail.exercise_name, "exercise 2")

            element = queue.get()
            self.assertEqual(element.exercise_name, "exercise 5")
            self.assertEqual(queue.head.exercise_name, "exercise 4")
            self.assertEqual(queue.tail.exercise_name, "exercise 5")
        

if __name__ == "__main__":
    unittest.main()