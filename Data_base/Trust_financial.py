import mysql.connector
import csv
import os
from pathlib import Path

class CreateTable:
    def __init__(self):
        self.host = "localhost"
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = "chat_bot"

    def connection_data_base(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
        if connection.is_connected():
            print("The connection is established")
            
            cursor = connection.cursor()
            
            cursor.execute('''
                            CREATE TABLE Trust_payments (
                                        Date DATE,
                                        Name VARCHAR(255) NOT NULL,
                                        Amount INTEGER,
                                        Project VARCHAR(400),
                                        Mobile_number varchar(300),
                                        Bank_number VARCHAR(255),
                                        UPI_traction_id VARCHAR(300),
                                        Receipt_No integer)
                                ''')
            
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def add_user_profile(self, 
                         Date,Name, Amount,Project,Mobile_number,Bank_number,UPI_traction_id,Receipt_No):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
        if connection.is_connected():
            cursor = connection.cursor() 
            
            cursor.execute("""
                INSERT INTO Club_payments
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
            """, (Date,Name, Amount,Project,Mobile_number,Bank_number,UPI_traction_id,Receipt_No))
            
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()


def insert_data_from_csv(csv_file_path, add_user_profile):
    try:
        with open(str(csv_file_path), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row

            for row in csvreader:
                (Date,Name, Amount,Project,Mobile_number,Bank_number,UPI_traction_id,Receipt_No) = row
                add_user_profile(Date,Name, Amount,Project,Mobile_number,Bank_number,UPI_traction_id,Receipt_No)

        print("Data inserted successfully from CSV.")
    except Exception as e:
        print(f"Error inserting data from CSV: {str(e)}")


table = CreateTable()
table.connection_data_base()
print("Database created and Table created")

csv_file_path = Path(r"Data\Trust_financial.csv")
insert_data_from_csv(csv_file_path=csv_file_path, add_user_profile=table.add_user_profile)

print("The data inserted successfully")
