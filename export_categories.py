"""Automatically exports various categories to config for easy type hints."""

from io import TextIOWrapper
import os
import shutil
from typing import List
from rengine.dataset import get_dataset



CONFIG_PROXY_PATH = "rengine/config_proxy.py"
DATASET = get_dataset("clean_data.csv")



def export_unique_values_from_df_column(writer: TextIOWrapper, col_name: str, var_name: str):
    writer.write(f"\nclass {var_name}:\n")
    unique_values: List[str] = DATASET[col_name].unique()
    print(unique_values)
    writer.writelines([
        f"    {('_'.join(value.upper().split(' '))).replace('-', '_')} = \"{value}\"\n" for value in unique_values if type(value) == str
    ])
    writer.write("    ALL = \"All\"\n")
    





if __name__ == "__main__":
    if(os.path.exists(CONFIG_PROXY_PATH)):
        os.remove(CONFIG_PROXY_PATH)
    with open(CONFIG_PROXY_PATH, "x") as f:
        export_unique_values_from_df_column(f, "EXERCISE", "ExerciseName")
        export_unique_values_from_df_column(f, "Equipment", "EquipmentAvailable")
