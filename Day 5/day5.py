from mysql.connector import connection

try:
    connect = {
        'user':'root',
        'host':'localhost',
        'database':'student',
    }
    #connecting to the server
    connecting = connection.MySQLConnection(**connect)
    print(connecting)
   
except:
    print("Unable to connect to the database")

#creating cursor 
myc = connecting.cursor()
try:
# #sql query to create table in database
    sql = ' create table class(id int auto_increment primary key, ClassName varchar(10) not null );'
    myc.execute(sql)
    myc.close()
except:
# #SHOW ALL TABLES
    print("Table exists!")
connecting.close()