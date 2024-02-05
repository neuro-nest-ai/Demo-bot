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
                            CREATE TABLE Club_payments (
                                        Date DATE,
                                        Name VARCHAR(255) NOT NULL,
                                        Amount INTEGER,
                                        Subscription VARCHAR(400),
                                        Phone_number VARCHAR(300),
                                        Bank_number VARCHAR(255),
                                        UPI_transaction_id VARCHAR(300),
                                        Invoice_No INTEGER)
                                ''')
            
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def add_user_profile(self, 
                         Date, Name, Amount, Subscription, Phone_number, Bank_number, UPI_transaction_id, Invoice_No):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
        if connection.is_connected():
            cursor = connection.cursor() 
            
            cursor.execute("""
                INSERT INTO Club_payments (Date, Name, Amount, Subscription, Phone_number, Bank_number, UPI_transaction_id, Invoice_No)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (Date, Name, Amount, Subscription, Phone_number, Bank_number, UPI_transaction_id, Invoice_No))
            
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
                (Date, Name, Amount, Subscription, Phone_number, Bank_number, UPI_transaction_id, Invoice_No) = row
                add_user_profile(Date, Name, Amount, Subscription, Phone_number, Bank_number, UPI_transaction_id, Invoice_No)

        print("Data inserted successfully from CSV.")
    except Exception as e:
        print(f"Error inserting data from CSV: {str(e)}")


table = CreateTable()
table.connection_data_base()
print("Database created and Table created")

# Update the CSV file path to point to the correct location
csv_file_path = Path(r"Data\Club_payments.csv")
insert_data_from_csv(csv_file_path=csv_file_path, add_user_profile=table.add_user_profile)

print("The data inserted successfully")















































































