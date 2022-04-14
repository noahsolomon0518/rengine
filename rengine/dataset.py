import pandas as pd
from rengine import data


DATASET_FOLDER = data.__file__.rstrip("__init__.py")

def get_dataset(filename:str):
    if(filename.endswith(".xlsx")):
        df = pd.read_excel(DATASET_FOLDER+filename)
    else:
        df = pd.read_csv(DATASET_FOLDER+filename)
    return df

