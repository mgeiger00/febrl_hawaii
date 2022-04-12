# HHSProject
CS460/461 Group Project on Data Matching
This main branch contains the generate.py script that uses the files in /data to create a user defined dataset containing a mock patient record.
It includes a patient ID, first name, last name	 street number, address,	city, zipcode, state, date of birth, age, phone number, social security number,
and blocking number. An example of the output is in createdDataset.csv

To run generate.py the following command can be used in your computer's command center. Be sure to be in the directory where you have the file saved.

                    python generate.py 2000 createdDataset.csv 200 30 5 4 6 zipf
                 
The first argument is the name of the file (generate.py), the second argument is the number of names you would like to use out of 3012 (2000), the third argument
is the desired name of the output file (createdDataset.csv), the fourth argument is the number of unique entries desired (200), the fifth is the number of duplicates
desired (30), the sixth argument is the maximum number of duplicates based on one original record (5), the seventh argument is the maximum number of modifications in a
single field (4), the eigth argument is the maximum number of modifications in the full record, and the ninth argument is the desired distribution of duplicate records
(which can be zipf, uniform, or poisson).
