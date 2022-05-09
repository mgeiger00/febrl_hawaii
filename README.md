# HHS Dataset Generation Project
## CS460/461 Group Project
###### Created by Max Geiger, Jamie Strong, Aaron McLean, and Catherine Cornella, August 2021 - May 2022

### I. Program Purpose and Overview
The program’s purpose is to create a Hawaii-focused dataset of fictitious patient records, for the purpose of assisting the further refinement of partial patient record matching software. This is unique due to the common occurrence of a special character within Hawaiian names, referred to as the okena. 
The program creates a data set of fabricated patient data records, with the option of randomized duplications of names, exporting the resulting dataset in comma-separated value format (.CSV). The records are composed of the following fields: patient ID, first name, last name, street number, address, city, zip-code, state, date of birth, age, phone number, social security number, and blocking number. The distribution of the randomness can be one of three specific types, selectable upon execution.

### II. Program Requirements
To execute the program, it is required that Python 3 be installed on the machine, and may be necessary to install the `sets` and `pandas` packages. To do so, simply run `pip install sets` and `pip install pandas`, or consult online instructions. It is recommended to have a software able to read .csv files as well, although not required. The program is compatible with the latest version of Python 3. 

### III. Program Instructions and Customization Options
This main branch contains the generate.py script that uses the files in data folder to create a user defined dataset containing a mock patient record.
It includes a patient ID, first name, last name	 street number, address,	city, zipcode, state, date of birth, age, phone number, social security number,
and blocking number. An example of the output is in createdDataset.csv

#### - Program Execution
To execute the program, use the following command in your computer's Command Prompt (Windows), Terminal (Mac), or Command Line (Linux). Be sure you are executing the command in the same directory where you have the file saved.

                    python generate.py 2000 createdDataset.csv 200 30 5 4 6 zipf
                 
The first argument is the name of the file (generate.py), the second argument is the number of names you would like to use out of 3012 (2000), the third argument
is the desired name of the output file (createdDataset.csv), the fourth argument is the number of unique entries desired (200), the fifth is the number of duplicates
desired (30), the sixth argument is the maximum number of duplicates based on one original record (5), the seventh argument is the maximum number of modifications in a
single field (4), the eigth argument is the maximum number of modifications in the full record (6), and the ninth argument is the desired distribution of duplicate records
(which can be zipf, uniform, or poisson).
 
#### - Program Customization
Within the program, several variables can be changed to customize the program

### IV. Common Issues and Solutions
If you are having trouble with the execution of the file, we suggest you check the following areas:
#### - Command Arguments
The most probable error is a result of the arguments being specified incorrectly. This can be as trivial as a misspelling of one of the arguments, or an omission of an argument entirely. Ensure you have the correct number of arguments, in the correct order, with the correct input for that argument.
#### - Python Packages
Another common error, one we ran into during production and debugging, is that of missing Python packages. The most common two were sets and pandas, so it is advised to check those first. The installation of the package(s) should fix the issue. The list of required packages can be found at the very top of generate.py.
#### - Python Version
Be sure that you are using a version of python compatible with the program. It was designed and written with Python 3, and due to time restraints the complete list of versions could not be exhaustively tested. 
