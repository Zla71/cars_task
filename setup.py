from setuptools import setup

setup(
    name='Classic Cars',
    version='1.0',
    description=
    '''This is a small pipeline which opens a JSON file and creates a pandas DataFrame.
    After those steps the pipeline makes a few tasks:
    1. Prints the number of unique cars in the dataset.
    2. Prints the average horse power of all the cars.
    3. Prints the top 5 most heaviest cars.
    4. Prints the number of cars made by each manufacturer.
    5. Prints the number of cars made each year.
    6. Saves the dataset to a CSV file.
    For all these tasks are used some pandas methods and functions, OOP programming, logging, error handling and docstrings ''',
    author='Zlati Rachev',
    author_email='zlati.rachev7@gmail.com',
    repo="https://github.com/Zla71/example",
    install_requires=[
        'collections',
        'pandas',
        'json',
        'logging',
        'os',
    ],
)
