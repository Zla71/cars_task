def write_logging(car_task_class_instance, text):
    my_log = open(car_task_class_instance.log_file_path, "a+")
    my_log.write(text)
    my_log.close()
