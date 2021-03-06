from unittest import TestCase
import unittest
from rengine.config import TIME_BASED_CONDITIONS, ExerciseType, MuscleGroup
from rengine.exercises import pick_random_exercise
import dataframe_image as dfi
from rengine.workouts import AutoGeneratedWorkout, BaseWorkout, LowerBodyWorkout, UpperBodyWorkout, dictionary_addition



class TestDictionAdd(TestCase):
    def test_add_with_same_keys(self):
        dict1 = dict(a = 1, b = 2, c = 56)
        dict2 = dict(a = 0.5, b = 20, c = 6)
        added_dict = dictionary_addition((dict1, dict2))
        self.assertDictEqual(added_dict, dict(a = 1.5, b = 22, c = 62), "Dictionary key value pairs are not adding correctly.")

    def test_add_with_different_keys(self):
        dict1 = dict(a = 1, b = 2, d = 56)
        dict2 = dict(a = 0.5, b = 20, c = 6)
        added_dict = dictionary_addition((dict1, dict2))
        self.assertDictEqual(added_dict, dict(a = 1.5, b = 22, c = 6, d = 56), "Dictionary key value pairs are not adding correctly when keys are different.")


class TestBaseWorkout(TestCase):
    def test_if_workout_has_correct_load(self):
        workout = BaseWorkout([
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.BACK], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CALVES], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CALVES], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
        ])
        self.assertDictEqual(workout.load_per_muscle_group, {
            MuscleGroup.CALVES:2,
            MuscleGroup.CHEST:5,
            MuscleGroup.BACK:1,
            MuscleGroup.TRICEPS:0,
            MuscleGroup.BICEPS:0,
            MuscleGroup.DELTOIDS:0,
            MuscleGroup.QUAD:0,
            MuscleGroup.HAMSTRINGS:0
        }, "Workouts load per muscle group not returning correct loads.")



class TestAutoGeneratedWorkout(TestCase):
    def test_if_min_muscle_gets_least_worked_muscle_that_is_being_trained(self):
        workout1 = AutoGeneratedWorkout(15, [MuscleGroup.CHEST, MuscleGroup.BACK, MuscleGroup.CALVES], exercises= [
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.BACK], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CALVES], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CALVES], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
            pick_random_exercise([MuscleGroup.CHEST], ExerciseType.HYPERTROPHY),
        ])
        self.assertEqual(workout1._find_next_muscle_group_to_work(), MuscleGroup.BACK, "AutoGeneratedWorkout is not correctly finding least worked muscle that is trainable.")
        workout1.add_exercises([pick_random_exercise([MuscleGroup.BACK], ExerciseType.HYPERTROPHY) for i in range(6)])
        self.assertEqual(workout1._find_next_muscle_group_to_work(), MuscleGroup.CHEST, "AutoGeneratedWorkout is not correctly finding least worked muscle that is trainable.")




class TestLowerBodyWorkout(TestCase):
    def test_generate(self):
        for i in range(15, 121, 15):
            workout = LowerBodyWorkout(i,"Barbell Squat")
            workout.create()
            self.assertGreater(len(workout.workout), 0, "No exercises were generated for this Lower body workout.")
            for exercise in workout.workout:
                self.assertIn(exercise.muscle_group, MuscleGroup.LOWER_BODY, "Lower body workout has a non-lower body exercise in it.")
            self.assertLessEqual(abs(workout.total_time-i), 7.5, f"{i} minute workout is atleast 10 minutes longer or shorter than expected")
            tbc = TIME_BASED_CONDITIONS[i]
            for muscle, cap in tbc["caps"].items():
                exercises_of_muscle = [exercise for exercise in workout.workout if exercise.muscle_group == muscle]
                self.assertLessEqual(len(exercises_of_muscle), cap, f"Lower body workout of length {i} is generating {len(exercises_of_muscle)} {muscle} exercises when it should only be generating {cap}.")
    
    def test_muscle_group_cap(self):   
        for i in range(15, 121, 15):
            tbc = TIME_BASED_CONDITIONS[i]
            workout = LowerBodyWorkout(i,"Romanian Deadlift")
            workout.create()
            for muscle, cap in tbc["caps"].items():
                exercises_of_muscle = [exercise for exercise in workout.workout if exercise.muscle_group == muscle]
                self.assertLessEqual(len(exercises_of_muscle), cap, f"Upper body workout of length {i} is generating {len(exercises_of_muscle)} {muscle} exercises when it should only be generating {cap}.")

    def test_buffer_times(self):
        for x in range(3):
            for i in range(15, 121, 15):
                workout = LowerBodyWorkout(i,"Barbell Squat")
                workout.create()
                self.assertLessEqual(abs(workout.total_time-i), 7.5, f"{i} minute workout is atleast 7.5 minutes longer or shorter than expected")




class TestUpperBodyWorkout(TestCase):
    def test_generate(self):
        for i in range(15, 121, 15):
            workout = UpperBodyWorkout(i,"Barbell Bench Press")
            workout.create()
            self.assertGreater(len(workout.workout), 0, "No exercises were generated for this upper body workout.")
            for exercise in workout.workout:
                self.assertIn(exercise.muscle_group, MuscleGroup.UPPER_BODY, "Upper body workout has a non-upper body exercise in it.")         

    def test_muscle_group_cap(self):   
        for i in range(15, 121, 15):
            tbc = TIME_BASED_CONDITIONS[i]
            workout = UpperBodyWorkout(i,"Barbell Bench Press")
            workout.create()
            for muscle, cap in tbc["caps"].items():
                exercises_of_muscle = [exercise for exercise in workout.workout if exercise.muscle_group == muscle]
                self.assertLessEqual(len(exercises_of_muscle), cap, f"Lower body workout of length {i} is generating {len(exercises_of_muscle)} {muscle} exercises when it should only be generating {cap}.")

    def test_buffer_times(self):
        for x in range(3):
            for i in range(15, 121, 15):
                workout = UpperBodyWorkout(i,"Barbell Bench Press")
                workout.create()
                self.assertLessEqual(abs(workout.total_time-i), 7.5, f"{i} minute workout is atleast 7.5 minutes longer or shorter than expected")




if __name__ == "__main__":
    unittest.main()


    
