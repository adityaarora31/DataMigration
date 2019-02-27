import sys
import csv
import re
import mysql.connector as mc
from getConnection import get_connection
from importDataCSV import importdata_from_csv
from migrateDataDB import migrate_data


if len(sys.argv) > 1:
    
    if (sys.argv[1]=="import" and sys.argv[2]=="*.csv"):




#Enable only when you want to put data in database
#importdata_from_csv("NewDirtyData.csv") 
#Extract Database
#migrate_data()


