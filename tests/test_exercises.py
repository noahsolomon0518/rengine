
import logging
import random
from unittest import TestCase
import unittest

from numpy import unicode_
from rengine.config import ExerciseLoad, ExerciseType, MuscleGroup

from rengine.exercises import Exercise, ExerciseFromTypePreset, pick_random_exercise

logging.basicConfig(level=logging.INFO)

class TestPickExercise(TestCase):
    def test_correct_exercise_type_and_muscle_group_and_load(self):
        for i in range(10):
            muscle = random.choice(MuscleGroup.ALL)
            type = random.choice([ExerciseType.HYPERTROPHY])
            load = [random.choice(ExerciseLoad.ALL)]
            exercise = pick_random_exercise([muscle], type, load)
            self.assertEqual(exercise.muscle_group, muscle, f"Picked exercise from wrong muscle group.")
            self.assertEqual(exercise.exercise_type, type, f"Picked exercise from wrong exercise type.")
            self.assertEqual(exercise.exercise_load, load[0], f"Picked exercise from wrong exercise load.")

    def test_random_chest_strength(self):
        for i in range(10):
            exercise = pick_random_exercise([MuscleGroup.CHEST], ExerciseType.STRENGTH)
            self.assertEqual(exercise.muscle_group, MuscleGroup.CHEST, f"Picked exercise from wrong muscle group.")


    def test_equipment_filtering(self):
        pass


    def test_pick_exercise_without_equipment(self):
        #Should return None
        pass

        



class TestExercise(TestCase):
    def test_get_length_with_int_ranges(self):
        exercise = Exercise("bench press", 4, 5, 3)

    def test_get_length_with_tuple_ranges(self):
        exercise = Exercise("bench press", 4, 5, (3,4))
    
    def test_str(self):
        exercise = Exercise("bench press", 4, 6, (3,4))

class TestExerciseFromTypePreset(TestCase):
    def test_init(self):
        preset_exercise = ExerciseFromTypePreset("Pull-Up", ExerciseType.STRENGTH)

    def test_init_with_unknown_exercise_name(self):
        #Should raise unknown exercise name error
        pass

if __name__ == "__main__":
    unittest.main()