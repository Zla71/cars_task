

class Adastra:

    def __init__(self) -> None:

        # directions
        self.json_file_path = r"D:\Python\packages\adastra_pack\cars.json"
        self.export_location = r"D:\Python\packages\adastra_pack\output.csv"

        # useful lists
        self.car_manufacturers = []
        self.production_years = []

        # useful variables
        self.number_of_unique_cars = None
        self.average_horsepower = None
        self.heaviest_cars = None
        self.number_cars_by_manufacturer = None
        self.number_cars_by_year = None
