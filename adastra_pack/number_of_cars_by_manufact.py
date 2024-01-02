from adastra_pack import write_log
from collections import Counter


def find_manufacturer_counts(adastra_class_instance, data_frame, time) -> None:
    """This method prints the number of cars made by each manufacturer."""
    try:
        cars = data_frame["Name"]
        for cur_car in cars:
            brand = cur_car.split(" ")[0]
            adastra_class_instance.car_manufacturers.append(brand)

        print(f"{time} --- The number of cars made by each manufacturer was printed..")
        print("\nHere are the numbers of cars made by manufacturer:\n")

        value_counts = Counter(adastra_class_instance.car_manufacturers)
        write_log.write_logging(f"{time} --- The number of cars made by each manufacturer was printed..\n\n")
        write_log.write_logging("Here are the numbers of cars made by manufacturer:\n\n")

        for car_brand, number_of_cars_by_brand in value_counts.items():
            if number_of_cars_by_brand < 2:
                print(f"{car_brand}: {number_of_cars_by_brand} car")
                write_log.write_logging(f"{car_brand}: {number_of_cars_by_brand} car\n")
            else:
                print(f"{car_brand}: {number_of_cars_by_brand} cars")
                write_log.write_logging(f"{car_brand}: {number_of_cars_by_brand} cars\n")                
        
    except Exception as e:
        print(repr(e))
        write_log.write_logging(e)