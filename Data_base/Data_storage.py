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
                  CREATE TABLE RotaryClubMembers (
                           Name VARCHAR(255) NOT NULL,
                           Location VARCHAR(255) NOT NULL,
                           OriginalJoinDate varchar(200),
                           CurrentClubJoinDate varchar(200),
                           YearsOfService varchar(300),
                           ROLES VARCHAR(255),
                           Sponser Text,
                           MemberID INT PRIMARY KEY,
                           Address Text,
                           MobilePhone VARCHAR(15),
                           PersonalEmail VARCHAR(255),
                           Classification VARCHAR(255))''')
            
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def add_user_profile(self, 
                         Name, Location, OriginalJoinDate, CurrentClubJoinDate, YearsOfService, ROLES,
                         Sponser, MemberID, Address, MobilePhone, PersonalEmail, Classification):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
        if connection.is_connected():
            cursor = connection.cursor() 
            
            cursor.execute("""
                INSERT INTO RotaryClubMembers
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (Name, Location, OriginalJoinDate, CurrentClubJoinDate, YearsOfService, ROLES,
                  Sponser, MemberID, Address, MobilePhone, PersonalEmail, Classification))
            
            connection.commit()
            
            # Close the cursor and connection
            cursor.close()
            connection.close()


def insert_data_from_csv(csv_file_path, add_user_profile):
    try:
        with open(csv_file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row

            for row in csvreader:
                (Name, Location, OriginalJoinDate, CurrentClubJoinDate, YearsOfService, ROLES,
                 Sponser, MemberID, Address, MobilePhone, PersonalEmail, Classification) = row
                add_user_profile(Name, Location, OriginalJoinDate, CurrentClubJoinDate, YearsOfService, ROLES,
                                 Sponser, MemberID, Address, MobilePhone, PersonalEmail, Classification)

        print("Data inserted successfully from CSV.")
    except Exception as e:
        print(f"Error inserting data from CSV: {str(e)}")


table = CreateTable()
table.connection_data_base()
print("Database created and Table created")

csv_file_path = Path(r"Data\oginal_profile_data.csv")
insert_data_from_csv(csv_file_path=csv_file_path, add_user_profile=table.add_user_profile)

print("The data inserted successfully")

    
    
    
        
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    
    
    
    
        
    
    
    
    
        
    
    
            
    
    
        
    
        
                                                





































































































































































































