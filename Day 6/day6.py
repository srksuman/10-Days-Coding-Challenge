from mysql.connector import connection
#CRUD Operation
info = {
    'username':'root',
    'database':'student',
}

try:
    conn = connection.MySQLConnection(**info)
    print(conn)
except:
    print("Unable to connect to the database")

myc = conn.cursor()
#creating a table
try:
    create = "create table student_info(id int auto_increment primary key,FullName varchar(20) not null,class int not null );"
    myc.execute(create)
    print("Table created!!!")
    myc.close()
except:
    print("Table exists")

#inserting data into table:
user_choice = input("Do you want to add Student information\npress 'Y' \n")
if user_choice == 'Y' or user_choice == 'y':
    name = input("Enter your Full Name\n")
    cls = int(input("Enter your Class\n"))
    insert = f"Insert into student_info values('','{name}',{cls});"

    try:
        myc.execute(insert)
        conn.commit()
        print("Data inserted!!!",myc.rowcount)
        print("Last row ID",myc.lastrowid)
    except:
        conn.rollback()
        print("Unable to insert data!!!")

# deleting data
user_choice = input("Do you want to Delete information\npress 'Y' \n")
if user_choice == 'Y' or user_choice == 'y':
    id = int(input("Enter the id to delete\n"))
    delete = f"Delete from student_info where id = {id};"
    try:
        myc.execute(delete)
        conn.commit()
        print(f"Data deleted!!")
    except:
        conn.rollback()
        print("Unable to delete!!")

#updating data
user_choice = input("Do you want to Update information\npress 'Y' \n")
if user_choice == 'Y' or user_choice == 'y':
    id = int(input("Enter the id to update\n"))
    name = input("Enter fullname\n")
    cls = int(input("Enter class\n"))
    delete = f"update student_info set fullname = '{name}',class = {cls} where id = {id};"
    try:
        myc.execute(delete)
        conn.commit()
        print(f"Data Updated!!")
    except:
        conn.rollback()
        print("Unable to update!!")

