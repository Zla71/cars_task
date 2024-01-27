import pandas as pd
import json


def open_json_file(car_task_class_instance) -> list:
    """This method open the json file and loads the dataset."""
    try:
        with open(car_task_class_instance.json_file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(repr(e))

def create_data_frame(adastra_class_instance, data) -> pd.DataFrame:
    """This method uses pandas to load the data into a DataFrame"""
    try:
        df = pd.DataFrame(data)
        adastra_class_instance.data_frame = df
        return df
    except Exception as e:
        print(repr(e))
