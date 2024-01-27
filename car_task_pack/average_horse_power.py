from car_task_pack import write_log

def find_average_horsepower(car_task_class_instance, data_frame, time) -> str:
    """This method prints the average horse power of all the cars."""
    try:
        car_task_class_instance.average_horsepower = data_frame["Horsepower"].mean()
        print(f"{time} --- The average horse power of all the cars was printed..")
        print(f"\nAverage horse power of all the cars: {car_task_class_instance.average_horsepower:.0f} hp\n")
        write_log.write_logging(car_task_class_instance, f"{time} --- The average horse power of all the cars was printed..\n")
        write_log.write_logging(car_task_class_instance, f"Average horse power of all the cars: {car_task_class_instance.average_horsepower:.0f} hp\n\n")
        return f"Average horse power of all the cars: {car_task_class_instance.average_horsepower:.0f} hp"
    except Exception as e:
        print(repr(e))
        write_log.write_logging(car_task_class_instance, e)