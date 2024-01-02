from adastra_pack import write_log

def find_average_horsepower(adastra_class_instance, data_frame, time) -> str:
    """This method prints the average horse power of all the cars."""
    try:
        adastra_class_instance.average_horsepower = data_frame["Horsepower"].mean()
        print(f"{time} --- The average horse power of all the cars was printed..")
        print(f"\nAverage horse power of all the cars: {adastra_class_instance.average_horsepower:.0f} hp\n")
        write_log.write_logging(f"{time} --- The average horse power of all the cars was printed..\n")
        write_log.write_logging(f"Average horse power of all the cars: {adastra_class_instance.average_horsepower:.0f} hp\n\n")
        return f"Average horse power of all the cars: {adastra_class_instance.average_horsepower:.0f} hp"
    except Exception as e:
        print(repr(e))
        write_log.write_logging(e)