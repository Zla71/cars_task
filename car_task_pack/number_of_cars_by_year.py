from car_task_pack import write_log
from collections import Counter

def find_number_of_cars_by_year(adastra_class_instance, data_frame, time) -> None:
    """This method prints the number of cars made each year."""
    try:
        dates = data_frame["Year"]
        for cur_date in dates:
            year = cur_date.split("-")[0]
            adastra_class_instance.production_years.append(year)
        value_counts = Counter(adastra_class_instance.production_years)

        print(f"\n{time} --- The number of cars made each year was printed..\n\n")
        print("Here is an information about number of cars build during the years:\n")

        write_log.write_logging(adastra_class_instance, f"\n{time} --- The number of cars made each year was printed..\n\n")
        write_log.write_logging(adastra_class_instance, "Here is an information about number of cars build during the years:\n\n")

        for year, number_of_cars_per_year in value_counts.items():
            print(f"{year} - {number_of_cars_per_year} cars")
            write_log.write_logging(adastra_class_instance, f"{year} - {number_of_cars_per_year} cars\n")
        
    except Exception as e:
        print(repr(e))
        write_log.write_logging(adastra_class_instance, e)