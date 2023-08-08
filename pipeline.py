from collections import Counter
import pandas as pd
import json, os, logging


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

        # logs
        logging.basicConfig(filename="cars.log", 
                            level=logging.DEBUG,
                            format='\n%(message)s %(asctime)s', datefmt="%H:%M:%S %d-%b-%y")

    
    def start_process(self):
        """This is the main method which starts the pipeline process."""
        Cars.write_logging(self, "The process has been started at")
        Cars.unique_cars(self)


    def open_json_file(self) -> list:
        """This method open the json file and loads the dataset."""
        try:
            with open(self.json_file_path, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(repr(e))
        

    def create_data_frame(self, data) -> pd.DataFrame:
        """This method uses pandas to load the data into a DataFrame"""
        try:
            df = pd.DataFrame(data)
            self.data_frame = df
            return df
        except Exception as e:
            print(repr(e))
    

    def unique_cars(self) -> None:
        """This method prints the number of unique cars in the dataset."""
        try:
            number_of_unique_cars = self.data_frame["Name"].nunique()
            print(f"Number of unique cars in the dataset: {number_of_unique_cars}")
            Cars.write_logging(self, " --- After opening and reading the JSON file, and creating the DatFrame\n     the number of unique cars in the dataset has been printed at")
        except Exception as e:
            print(repr(e))
            Cars.write_logging(self, e)

        Cars.average_horsepower(self)

    
    def average_horsepower(self) -> None:
        """This method prints the average horse power of all the cars."""
        try:
            number_of_average_horsepower = self.data_frame["Horsepower"].mean()
            print(f"\nAverage horse power of all the cars: {number_of_average_horsepower:.0f}")
            Cars.write_logging(self, " --- The average horse power of all the cars has been printed at")
        except Exception as e:
            print(repr(e))
            Cars.write_logging(self, e)

        Cars.find_top_heaviest_cars(self)


    def find_top_heaviest_cars(self) -> None:
        """This method prints the top 5 most heaviest cars."""

        try:
            heaviest_cars = self.data_frame.nlargest(5, "Weight_in_lbs").reset_index(drop=True)

            print("\nTop 5 most heaviest cars:")
            print(heaviest_cars[["Name", "Weight_in_lbs"]])
            Cars.write_logging(self, " --- The top 5 most heaviest cars has been printed at")
        except Exception as e:
            print(repr(e))
            Cars.write_logging(self, e)

        Cars.manufacturer_counts(self)


    def manufacturer_counts(self) -> None:
        """This method prints the number of cars made by each manufacturer."""
        try:
            cars = self.data_frame["Name"]
            for cur_car in cars:
                brand = cur_car.split(" ")[0]
                self.car_manufacturers.append(brand)

            print("\nHere are the numbers of cars made by manufacturer:")

            value_counts = Counter(self.car_manufacturers)
            for car_brand, number_of_cars_by_brand in value_counts.items():
                print(f"{car_brand}: {number_of_cars_by_brand} cars")
            Cars.write_logging(self, " --- The number of cars made by each manufacturer has been printed at")
        except Exception as e:
            print(repr(e))
            Cars.write_logging(self, e)
            
        Cars.number_of_cars_by_year(self)


    def number_of_cars_by_year(self) -> None:
        """This method prints the number of cars made each year."""
        try:
            dates = self.data_frame["Year"]
            for cur_date in dates:
                year = cur_date.split("-")[0]
                self.production_years.append(year)
            value_counts = Counter(self.production_years)

            print("\nHere is an information about number of cars build during the years:")

            for year, number_of_cars_per_year in value_counts.items():
                print(f"{year} - {number_of_cars_per_year} cars")
            Cars.write_logging(self, " --- The number of cars made each year has been printed at")
        except Exception as e:
            print(repr(e))
            Cars.write_logging(self, e)

        Cars.export_data(self)

    
    def export_data(self):
        """This method saves the dataset to a CSV file."""
        try:
            self.data_frame.to_csv(self.export_location, index=False)
            Cars.write_logging(self, " --- The process of exporting data to CSV file has been completed at")
        except Exception as e:
            print(repr(e))
            Cars.write_logging(self, e)


    def write_logging(self, text):
        logging.debug(text)

cars = Cars()
cars.start_process()



