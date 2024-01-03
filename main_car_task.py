from car_task_pack import number_of_cars_by_manufact
from car_task_pack import export_data_to_csv_file
from car_task_pack import number_of_cars_by_year
from car_task_pack import average_horse_power
from car_task_pack import top_heaviest_cars
from car_task_pack import make_dataframe
from car_task_pack import car_task_class
from car_task_pack import unique_cars
from car_task_pack import write_log
from car_task_pack import get_time
import time


car = car_task_class.CarsTask()

# START PIPELINE AND LOG THE PROCESS
current_time = get_time.get_currnet_time()
write_log.write_logging(car, f"\n{current_time} --- The process was started..\n\n")
print(f"\n{current_time} --- The process was started..\n")
time.sleep(2)

# INITIAL DATA
current_time = get_time.get_currnet_time()
json_data = make_dataframe.open_json_file(car)
data_frame = make_dataframe.create_data_frame(car, json_data)
write_log.write_logging(car, f"{current_time} --- JSON data was read and the data frame was built..\n")
write_log.write_logging(car, f"The number of rows in data frame are: {len(data_frame)} rows\n\n")
print(f"{current_time} --- JSON data was read and the data frame was built\n")
print(f"The number of rows in data frame are: {len(data_frame)} rows\n")
time.sleep(2)

# UNIQUE CARS
current_time = get_time.get_currnet_time()
unique_cars.find_unique_cars(car, data_frame, current_time)
time.sleep(2)

# AVERAGE HORSE POWER
current_time = get_time.get_currnet_time()
average_horse_power.find_average_horsepower(car, data_frame, current_time)
time.sleep(5)

# TOP 5 HEAVIEST CARS
current_time = get_time.get_currnet_time()
top_heaviest_cars.find_top_heaviest_cars(car, data_frame, current_time)
time.sleep(5)

# NUMBER OF CARS BY MANUFACTURER
current_time = get_time.get_currnet_time()
number_of_cars_by_manufact.find_manufacturer_counts(car, data_frame, current_time)
time.sleep(5)

# NUMBER OF CARS BY YEAR
current_time = get_time.get_currnet_time()
number_of_cars_by_year.find_number_of_cars_by_year(car, data_frame, current_time)
time.sleep(5)

# EXPORT DATA TO CSV FILE
current_time = get_time.get_currnet_time()
export_data_to_csv_file.export_data(car, data_frame, current_time)
time.sleep(2)

# THE PROCESS ENDED
current_time = get_time.get_currnet_time()
print(f"{current_time} --- The process finished..\n")
write_log.write_logging(car, f"\n{current_time} --- Process finished with SUCCESS..\n\n")

# FINISH THE LOG FILE
write_log.write_logging(car, "\n-----------------------------------------------------------------------------------------------\n")
write_log.write_logging(car, "-----------------------------------------------------------------------------------------------\n\n")

