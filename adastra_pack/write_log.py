@staticmethod
def write_logging(text):
    my_log = open(rf"D:\Python\packages\adastra_pack\log_data.log", "a+")
    my_log.write(text)
    my_log.close()
