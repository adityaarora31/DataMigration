import mysql.connector as mc

def get_connection():
    '''Makes a connection to the specified database and returns a cursor'''
    
    try: 
        connection = mc.connect(host='127.0.0.1',
                                            user='root',
                                            password='igdefault',
                                            database='DataMigration')
        
        return connection
    
    except mc.Error as error:
        
        print("You have some error while connecting to the database {}". format(error))