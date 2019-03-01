# Data Migration

This script will import data from a CSV file to MySQL database and filter that data and shift it to another table inside that database.

## Prerequisite

```
Python 3+
MySQL

```

### Running the script

```
python3 main.py --import CSV_Filename.csv
```
This will import the CSV file into the database into table named 'imported_data'.

```
python3 main.py --migrate faultymail.csv
```
This will migrate the data from 'imported_data' table to 'migrated_data' table.
While migrating, all faulty Emails are printed onto the terminal and USD income is converted to INR in the 'migarted_data' table.
Program will prompt the user to enter the USD to INR rate once while migrating.


```
python3 main.py --help
```
Help command will display all the options that can be used with this script.

