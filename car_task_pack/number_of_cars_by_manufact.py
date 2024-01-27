from car_task_pack import write_log
from collections import Counter


def find_manufacturer_counts(car_task_class_instance, data_frame, time) -> None:
    """This method prints the number of cars made by each manufacturer."""
    try:
        cars = data_frame["Name"]
        for cur_car in cars:
            brand = cur_car.split(" ")[0]
            car_task_class_instance.car_manufacturers.append(brand)

        print(f"{time} --- The number of cars made by each manufacturer was printed..")
        print("\nHere are the numbers of cars made by manufacturer:\n")

        value_counts = Counter(car_task_class_instance.car_manufacturers)
        write_log.write_logging(car_task_class_instance, f"{time} --- The number of cars made by each manufacturer was printed..\n\n")
        write_log.write_logging(car_task_class_instance, "Here are the numbers of cars made by manufacturer:\n\n")

        for car_brand, number_of_cars_by_brand in value_counts.items():
            if number_of_cars_by_brand < 2:
                print(f"{car_brand}: {number_of_cars_by_brand} car")
                write_log.write_logging(car_task_class_instance, f"{car_brand}: {number_of_cars_by_brand} car\n")
            else:
                print(f"{car_brand}: {number_of_cars_by_brand} cars")
                write_log.write_logging(car_task_class_instance, f"{car_brand}: {number_of_cars_by_brand} cars\n")                
        
    except Exception as e:
        print(repr(e))
        write_log.write_logging(car_task_class_instance, e)