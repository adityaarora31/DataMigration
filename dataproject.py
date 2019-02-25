import mysql.connector
def importdata():
    
    try:
        with open("DirtyData.csv", mode="r+") as csvopener:
            Content=csvopener.readline()
        connection=mysql.connector.connect(host='127.0.0.1',user='root',password='igdefault',database='DataMigration')
        cursor=connection.cursor()
        listdata=[]
        listdata=Content.split(",")
        firstname=listdata[0]+listdata[1]
        age=listdata[2]
        location=listdata[3]
        email=listdata[4]
        income=listdata[5]
        #print("{fname}{newage}{newlocation}{newemail}{newincome}".format(fname=firstname,newage=age,newlocation=location,newemail=email,newincome=income))
        #print("Done")
        #cursor.execute("insert values into imported_data (Name,Age,Location,Email,Income)" values (%s,%d,%s,%s,%d))
        #insert_tuple=(firstname,age,location,email,income)
        #print(insert_tuple)
        #insert_stmt="Insert into imported_data (Name,Age,Location,Email,Income) VALUES (%s,%d,%s,%s,%d),"
        #print(insert_stmt)
        cursor.execute("Insert into imported_data (Name,Age,Location,Email,Income) VALUES (%s,%s,%s,%s,%s)",(firstname,age,location,email,income))
        #print(result)
        connection.commit()
        select_stmt="Select * from imported_data"
        cursor.execute(select_stmt)
        #connection.commit()
       # print("Done")
    except mysql.connector.Error as error :
            connection.rollback()
            print("Failed to insert into MySQL table {}".format(error))
    finally:
        pass


importdata()