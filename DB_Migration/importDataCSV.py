import csv
import mysql.connector as mc
from getConnection import get_connection

def importdata_from_csv(csv_file_name):
    '''This Gets The Data From A CSV File and Put It Into The Database'''
    try:
        content = csv.DictReader (open(csv_file_name))
        connection = get_connection() #Getting connection from Get Connection
        cursor = connection.cursor()
        create_imported_table() #Creating imported table in the database
        
        for row in content:
            #Inserts data from CSV into Imported_Data Table
           cursor.execute("Insert into imported_data(FirstName, LastName, Age,\
                                                    Location, Email, Income) \
                                                    VALUES (%s,%s,%s,%s,%s,%s)",\
                                                    (row['First_name'], row['Last_name'],\
                                                    row['Age'], row['Location'],\
                                                    row['Email'], row['Income']))
        connection.commit()

    except ImportError as file_error:
        print ("File not present in present working directory {}".format(file_error))

    except mc.Error as error :
            #Handling error if above code failed
            print("Failed to insert into MySQL table {}".format(error))

def create_imported_table():
    """ Creates a table into the database"""
    try:
        connection = get_connection()
        cursor = connection.cursor()
        #Create Table Query
        sql_create_query ="create table imported_data (Firstname char(20), Lastname char(20),\
                            Age int(2), Location char(20), Email varchar(40), Income int(5))"

        cursor.execute(sql_create_query)
        connection.commit()
    except mc.Error as error:

        print("Error while making a table in MySQL {}". format(error))

