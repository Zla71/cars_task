from car_task_pack import write_log

def find_unique_cars(car_task_class_instance, data_frame, time) -> str:
    """This method prints the number of unique cars in the dataset."""
    
    try:
        car_task_class_instance.number_of_unique_cars = data_frame["Name"].nunique()
        print(f"{time} --- The number of unique cars in the dataset was printed..\n")
        print(f"Number of unique cars in the dataset: {car_task_class_instance.number_of_unique_cars} cars\n")
        write_log.write_logging(car_task_class_instance, f"{time} --- The number of unique cars in the dataset was printed..\n")
        write_log.write_logging(car_task_class_instance, f"Number of unique cars in the dataset: {car_task_class_instance.number_of_unique_cars} cars\n\n")
        return f"Number of unique cars in the dataset: {car_task_class_instance.number_of_unique_cars} cars"
    except Exception as e:
        print(repr(e))
        write_log.write_logging(car_task_class_instance, e)