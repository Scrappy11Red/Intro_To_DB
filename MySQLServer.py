import mysql.connector

try: 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="JackOfTheWest_11"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as error:
    print(f"{error}")

finally:
    if "mycursor" in locals():
        mycursor.close()
    if "mydb" in locals():
        mydb.close()