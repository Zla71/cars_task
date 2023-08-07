from collections import Counter
import pandas as pd
import json, os


class Cars:

    def __init__(self) -> None:

        # directions
        self.cwd = os.getcwd()
        self.json_file_path = self.cwd + os.path.sep + "cars.json"
        self.export_location = self.cwd + os.path.sep + "output.csv"

        # initial data
        self.json_data = Cars.open_json_file(self)
        self.data_frame = Cars.create_data_frame(self, self.json_data)

        # useful lists
        self.car_manufacturers = []
        self.production_years = []

    
    def start_process(self):
        """This is the main method which starts the pipeline process."""
        Cars.unique_cars(self)


    def open_json_file(self) -> list:
        """This method open the json file and loads the dataset."""
        with open(self.json_file_path, "r") as file:
            data = json.load(file)

        return data
    

    def create_data_frame(self, data) -> pd.DataFrame:
        """This method uses pandas to load the data into a DataFrame"""
        df = pd.DataFrame(data)
        self.data_frame = df

        return df
    

    def unique_cars(self) -> None:
        """This method prints the number of unique cars in the dataset."""
        number_of_unique_cars = self.data_frame["Name"].nunique()
        print(f"Number of unique cars in the dataset: {number_of_unique_cars}")

        Cars.average_horsepower(self)

    
    def average_horsepower(self) -> None:
        """This method prints the average horse power of all the cars."""
        number_of_average_horsepower = self.data_frame["Horsepower"].mean()
        print(f"\nAverage horse power of all the cars: {number_of_average_horsepower:.0f}")

        Cars.find_top_heaviest_cars(self)


    def find_top_heaviest_cars(self) -> None:
        """This method prints the top 5 most heaviest cars."""
        heaviest_cars = self.data_frame.nlargest(5, "Weight_in_lbs").reset_index(drop=True)

        print("\nTop 5 most heaviest cars:")
        print(heaviest_cars[["Name", "Weight_in_lbs"]])

        Cars.manufacturer_counts(self)


    def manufacturer_counts(self) -> None:
        """This method prints the number of cars made by each manufacturer."""
        cars = self.data_frame["Name"]
        for cur_car in cars:
            brand = cur_car.split(" ")[0]
            self.car_manufacturers.append(brand)

        print("\nHere are the numbers of cars made by manufacturer:")

        value_counts = Counter(self.car_manufacturers)
        for car_brand, number_of_cars_by_brand in value_counts.items():
            print(f"{car_brand}: {number_of_cars_by_brand} cars")

        Cars.number_of_cars_by_year(self)


    def number_of_cars_by_year(self) -> None:
        """This method prints the number of cars made each year."""
        dates = self.data_frame["Year"]
        for cur_date in dates:
            year = cur_date.split("-")[0]
            self.production_years.append(year)
        value_counts = Counter(self.production_years)

        print("\nHere is an information about number of cars build during the years:")

        for year, number_of_cars_per_year in value_counts.items():
            print(f"{year} - {number_of_cars_per_year} cars")
        
        Cars.export_data(self)

    
    def export_data(self):
        """This method saves the dataset to a CSV file."""
        self.data_frame.to_csv(self.export_location, index=False)


cars = Cars()
cars.start_process()



