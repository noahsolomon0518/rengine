import pandas as pd

from rengine import data
from argparse import ArgumentParser




def clean_data():
    df = pd.read_excel(data.__file__.rstrip("__init__.py") + "exercises.xlsx", header=1)
    df = df.iloc[:,:-1]
    df["MaxReps"] = df.apply(lambda x: 1 if x["Endurance"] == 2 else 0,axis=1)
    df = df.rename(columns = {"Stength": "Strength"})
    return df


def set_equipment(row, equipment):
    return equipment if row[equipment] else row["Equipment"]

def set_muscle_group(row, muscle_group):
    return muscle_group if row[muscle_group] else row["Muscle Group"]

def simplify_exercises_excel_sheet(file_name: str=None):
    df = clean_data()
    df["Equipment"] = df.apply(lambda x: "na")
    df["Muscle Group"] = df.apply(lambda x: "na")
    equipment_available = df.loc[:,"Barbell": "Assisted Pull-Up Machine"].columns
    muscle_groups = df.loc[:,"Back": "Biceps"].columns
    for equipment in equipment_available:
        df["Equipment"] = df.apply(lambda x: set_equipment(x, equipment), axis=1)
    for muscle_group in muscle_groups:
        df["Muscle Group"] = df.apply(lambda x: set_muscle_group(x, muscle_group), axis=1)

    df = df.drop(equipment_available.to_list(), axis=1)
    df = df.drop(muscle_groups.to_list(), axis=1)

    if(file_name):
        df.to_csv(f"rengine/data/{file_name}")


#run from root dir command: python clean.data.py <filename>
if __name__ == "__main__":
    parser = ArgumentParser("Data Cleaner")
    parser.add_argument("filename", action="store", metavar="filename", type=str, default="clean_data.csv")
    args = vars(parser.parse_args())
    simplify_exercises_excel_sheet(args["filename"])




