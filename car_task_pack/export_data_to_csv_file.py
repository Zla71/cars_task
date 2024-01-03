from car_task_pack import write_log

def export_data(adastra_class_instance, data_frame, time):
    """This method saves the dataset to a CSV file."""

    try:
        data_frame.to_csv(adastra_class_instance.export_location, index=False)
        write_log.write_logging(adastra_class_instance, f"\n{time} --- The process of exporting data to CSV file was completed..\n")
        write_log.write_logging(adastra_class_instance, f"\nThe csv file could be find here: {adastra_class_instance.export_location}\n")
        write_log.write_logging(adastra_class_instance, f"\nThe log file could be find here: {adastra_class_instance.log_file_path}\n")


        print(f"\n{time} --- The process of exporting data to CSV file was completed..\n")
        print(f"The csv file could be find here: {adastra_class_instance.export_location}\n")
        print(f"The log file could be find here: {adastra_class_instance.log_file_path}\n")

    except Exception as e:
        print(repr(e))
        write_log.write_logging(adastra_class_instance, e)