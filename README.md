# Classic cars pipeline

On this page:
* [Overview](#overview)
* [Instructions](#instructions)
* [Logfile](#logfile)
* [Testing](#testing)
* [Task](#task)

<a name="overview"></a>
## Overview

This is a small pipeline which opens a JSON file and creates a pandas DataFrame. After those steps the pipeline makes a few tasks:

1. Prints the number of unique cars in the dataset.
2. Prints the average horse power of all the cars.
3. Prints the top 5 most heaviest cars.
4. Prints the number of cars made by each manufacturer.
5. Prints the number of cars made each year.
6. Saves the dataset to a CSV file.
For all these tasks are used some pandas methods and functions, OOP programming, logging, error handling and docstrings

---


<a name="instructions"></a>
## Instructions

1. Download the package.
2. Change the routes of "json_file_path" and "export_location" of files in **Adastra class**.
3. Now you can start the **main_adastra.py**.
4. Check the output console.
5. Check the **output.csv**.
6. Check the **log_data.log**.

---


<a name="logfile"></a>
## Logfile

Here is an example how the Logfile looks like:

11:44:05 --- The process was started..

11:44:07 --- JSON data was read and the data frame was built..
The number of rows in data frame are: 406 rows

11:44:09 --- The number of unique cars in the dataset was printed..
Number of unique cars in the dataset: 311 cars

11:44:12 --- The average horse power of all the cars was printed..
Average horse power of all the cars: 105 hp

11:44:17 --- The top 5 most heaviest cars was printed..

... Information about each car on a new row ...

11:44:22 --- The number of cars made by each manufacturer was printed..

Here are the numbers of cars made by manufacturer:

... Information about each brand on a new row ...

11:44:27 --- The number of cars made each year was printed..

Here is an information about number of cars build during the years:

... Information about each year on a new row ...

11:44:32 --- The process of exporting data to CSV file was completed..

The csv file could be find here: D:\Python\packages\adastra_pack\output.csv

The log file could be find here: D:\Python\packages\adastra_pack\log_data.log

11:44:34 --- Process finished with SUCCESS..

---


<a name="testing"></a>
## Testing

1. Open the **testing_adastra.py**.
2. Start the file and you will see the resulsts in the **Console**.

---


<a name="task"></a>
## Task

**Problem Statement:**

You have been given a dataset containing information about various cars, including their make, model, year, and price. Your task is to write a Python program that can perform the following operations:

1. Load the dataset from a JSON file.
2. Print the number of unique cars in the dataset.
3. Print the average horse power of all the cars.
4. Print the top 5 most heaviest cars.
5. Print the number of cars made by each manufacturer.
6. Print the number of cars made each year.
7. Save the dataset to a CSV file.

**Instructions:**

1. Write a Python program that reads the dataset from the JSON file.
2. Use pandas to load the data into a DataFrame.
3. Implement the required operations using the DataFrame methods and functions.
4. Print the results to the console.
5. Save the final DataFrame to a CSV file.
6. Use OOP
7. Upload the code in public GIT repository
8. Logging, error handling, docstrings are mandatory
9. Provide setup.py or pyproject.toml
10. Write unittests (optional)

---