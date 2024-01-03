def write_logging(adastra_class_instance, text):
    my_log = open(adastra_class_instance.log_file_path, "a+")
    my_log.write(text)
    my_log.close()
