import re
import csv
import sys
import mysql.connector as mc
from getConnection import get_connection

def migrate_data():
    '''Gets data from the imported database, deals with all the conversions and stores them back into a new table '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_Query = "Select * from imported_data"
        cursor.execute (sql_select_Query)
        records = cursor.fetchall()
        create_migrated_table()
        EMAIL_REGEX = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        USDINR_rate = int(input("Enter the conversion rate USD to INR"))
        print("Total number of rows in imported_data is - ", cursor.rowcount)
    
        for row in records:
            data = {}
            data['Name'] = row[0]+row[1]
            data['Age'] = row[2]
            data['Location'] = row[3]
            data['Email'] = row[4]
            data['Income'] = row[5]
            notmatched = False
            pattern=re.search(EMAIL_REGEX,row[4])
            if pattern==None:
                notmatched=True
                print(data['Email'],data['Name'],data['Age'],data['Location'],data['Income'])
            income_in_INR=(data['Income'] * USDINR_rate)
            if not notmatched:
                cursor.execute("Insert into migrated_data (Name, Age,Location,\
                                                            Email, Income) \
                                                            VALUES (%s,%s,%s,%s,%s)",\
                                                            (data['Name'], data['Age'],\
                                                            data['Location'],data['Email'],\
                                                            income_in_INR))
        connection.commit()
    except mc.Error as error:
        print("Error while printing data from MySQL {}".format(error))

def create_migrated_table():
    """ Creates a table into the database"""
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_create_query="create table migrated_data (Name char(50),\
                                                     Age int(2),\
                                                     Location char(20),\
                                                     Email varchar(40),\
                                                     Income int(10)) "
        cursor.execute(sql_create_query)
        connection.commit()

    except mc.Error as error:
        print("Error while making a table in MySQL {}". format(error))

