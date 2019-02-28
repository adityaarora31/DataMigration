import sys
import csv
import re
import mysql.connector as mc
from getConnection import get_connection
from importDataCSV import importdata_from_csv
from migrateDataDB import migrate_data

if __name__ == "__main__":

    if len(sys.argv) > 1:
        
        if (sys.argv[1] == "--import" and (sys.argv[2]).isalpha):
            print("Importing From CSV... Please Wait")
            importdata_from_csv(sys.argv[2])

        elif (sys.argv[1]=="--migrate" and sys.argv[2].isalpha):
            print("Migrating Now...Please Wait")
            migrate_data()

        elif (sys.argv[1]== "--help"):
            pass
        else:
            print("Something went wrong with the parameters Please Check")
    else:

        print("Please Supply Some Argument To The Script")
            
else: 
    print("Code won't execute if imported")


#Enable only when you want to put data in database
#importdata_from_csv("NewDirtyData.csv") 
#Extract Database
#migrate_data()


