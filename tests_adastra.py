from adastra_pack.make_dataframe import create_data_frame, open_json_file
from adastra_pack.average_horse_power import find_average_horsepower
from adastra_pack.unique_cars import find_unique_cars
from adastra_pack.get_time import get_currnet_time
from adastra_pack.adastra_class import Adastra
from unittest import main, TestCase
import pandas as pd

class TestAdastra(TestCase):
    def setUp(self) -> None:
        self.car = Adastra()
        self.json_data = open_json_file(self.car)
        self.data_frame = create_data_frame(self.car, self.json_data)
        self.current_time = get_currnet_time()
        self.expected_type_pd = pd.DataFrame
        self.expected_list = list
        self.expected_length = 406
        self.expected_result_unique_cars = "Number of unique cars in the dataset: 311 cars"
        self.expeted_result_average_horse_power = "Average horse power of all the cars: 105 hp"
    
    def test_open_and_check_json_file(self):
        self.assertEqual(self.expected_list, type(self.json_data))
        self.assertEqual(self.expected_length, len(self.json_data))

    def test_open_check_data_frame(self):
        self.assertEqual(self.expected_type_pd, type(self.data_frame))
        self.assertEqual(self.expected_length, len(self.data_frame))

    def test_find_unique_cars(self):
        result = find_unique_cars(self.car, self.data_frame, self.current_time)
        self.assertEqual(self.expected_result_unique_cars, result)

    def test_average_horse_power(self):
        result = find_average_horsepower(self.car, self.data_frame, self.current_time)
        self.assertEqual(self.expeted_result_average_horse_power, result)

if __name__ == "__main__":
    main()