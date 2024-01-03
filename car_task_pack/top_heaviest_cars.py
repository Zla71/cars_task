from car_task_pack import write_log

def find_top_heaviest_cars(adastra_class_instance, data_frame, time) -> None:
    """This method prints the top 5 most heaviest cars."""

    try:
        adastra_class_instance.heaviest_cars = data_frame.nlargest(5, "Weight_in_lbs").reset_index(drop=True)

        print(f"{time} --- The top 5 most heaviest cars was printed..")
        print("\nTop 5 most heaviest cars:")
        print(adastra_class_instance.heaviest_cars[["Name", "Weight_in_lbs"]])
        print()
        write_log.write_logging(adastra_class_instance, f"{time} --- The top 5 most heaviest cars was printed..\n\n")
        write_log.write_logging(adastra_class_instance, f'{adastra_class_instance.heaviest_cars[["Name", "Weight_in_lbs"]]}\n\n')
    except Exception as e:
        print(repr(e))
        write_log.write_logging(adastra_class_instance, e)