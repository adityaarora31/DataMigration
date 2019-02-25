import mysql.connector
import csv
def importdata():
    
    try:
        #with open('DirtyData.csv') as csvopener:
        Content=csv.DictReader(open('NewDirtyData.csv'))
        connection=mysql.connector.connect(host='127.0.0.1',user='root',password='igdefault',database='DataMigration')
        cursor=connection.cursor()
        for row in Content:
            firstname=row['First_name']
            lastname=row['Last_name']
            age=row['Age']
            location=row['Location']
            email=row['Email']
            income=row['Income']
        #print("{fname}{newage}{newlocation}{newemail}{newincome}".format(fname=firstname,newage=age,newlocation=location,newemail=email,newincome=income))
        #print("Done")
        #cursor.execute("insert values into imported_data (Name,Age,Location,Email,Income)" values (%s,%d,%s,%s,%d))
        #insert_tuple=(firstname,age,location,email,income)
        #insert_stmt="Insert into imported_data (Name,Age,Location,Email,Income) VALUES (%s,%d,%s,%s,%d),"
            cursor.execute("Insert into imported_data (FirstName,LastName,Age,Location,Email,Income) VALUES (%s,%s,%s,%s,%s,%s)",(firstname,lastname,age,location,email,income))
            connection.commit()
        # select_stmt="Select * from imported_data"
        # cursor.execute(select_stmt)
    except mysql.connector.Error as error :
            connection.rollback()
            print("Failed to insert into MySQL table {}".format(error))
    finally:
        pass


importdata()