import mysql.connector
import csv
import re

def get_connection():
    '''Makes a connection to the specified database'''
    try: 
        connection=mysql.connector.connect(host='127.0.0.1',user='root',password='igdefault',database='Bootcamp')
        return connection
    except mysql.connector.Error as error:
        print("You have some error while connecting to the database {}". format(error))

def importdata():
    try:
        '''This Gets The Data From A CSV File and Put It Into The Database'''
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
            cursor.execute("Insert into imported_data (FirstName,LastName,Age,Location,Email,Income) VALUES (%s,%s,%s,%s,%s,%s)",(firstname,lastname,age,location,email,income))
            connection.commit()
    except mysql.connector.Error as error :
            connection.rollback()
            print("Failed to insert into MySQL table {}".format(error))
        

def get_data():
    '''Gets data from the imported database, deals with all the conversions and stores them back into a new table '''
    try:
        # import pdb
        # pdb.set_trace()
        # connection=mysql.connector.connect(host='127.0.0.1',user='root',password='igdefault',database='Bootcamp')
        connection=get_connection()
        cursor=connection.cursor()
        sql_select_Query="Select * from imported_data"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        USD_to_INR_rate=int(input("Enter the conversion rate USD to INR"))
        print("Total number of rows in imported_data is - ", cursor.rowcount)
        for row in records:
            data = {}
            data['Name'] =row[0]+row[1]
            data['Age']= row[2]
            data['Location']=row[3]
            data['Email']=row[4]
            data['Income']=row[5]
            notmatched=False
            pattern=re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",data['Email'])
            if pattern==None:
                notmatched=True
            if notmatched==True:
                dump_faulty_emails(data['Email'],data['Name'],data['Age'],data['Location'],data['Income'])
            income_in_INR=(data['Income'] * USD_to_INR_rate)
            if(notmatched==False):
                cursor.execute("Insert into migrated_data (Name,Age,Location,Email,Income) VALUES (%s,%s,%s,%s,%s)",(data['Name'],data['Age'],data['Location'],data['Email'],income_in_INR))
                connection.commit()
            
    except mysql.connector.Error as error:
        print("Error while printing data from MySQL {}".format(error))


def dump_faulty_emails(extracted_email,combined_name,extracted_age,extracted_location,extracted_income):
    '''Stores Faulty Emails Into A CSV File'''

    try:
        fieldname=['Email','Name','Age','Location','Income']  #Fieldname list to pass as a parameter in DictWriter
        with open("faulty_emails.csv","w+") as emailfile:
            writer=csv.DictWriter(emailfile, fieldnames=fieldname)  
            writer.writeheader() #Writing data into the CSV file
            writer.writerow({'Email': extracted_email,'Name':combined_name,'Age':extracted_age,'Location': extracted_location,'Income':extracted_income} )
        # writer.writerow({'Name':combined_name})
        # writer.writerow({'Age':extracted_age})
        # writer.writerow({'Location': extracted_location})
        # writer.writerow({'Income':extracted_income})
        print("Printing Faulty Emails Into A CSV File...")
    except:
        print("Error in dumping into csv file")



#Enable only when you want to put data in database
#importdata() 

#Extract Database

get_data()

# dump_faulty_emails()
