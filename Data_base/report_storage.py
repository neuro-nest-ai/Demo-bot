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
                CREATE TABLE IF NOT EXISTS report_generation(
                    DATE_OF_REPORT Date,
                    Service TEXT,
                    Heading TEXT,
                    content TEXT,
                    Duration_in_Hours VARCHAR(100),
                    Cost_of_club_in_Rs_For_Service_Projects_Only INT,
                    Volunteer_hours_For_Service_Projects_Only INT,
                    No_of_beneficiaries_For_Service_Projects_Only INT,
                    Value_to_beneficiaries_in_Rs_For_Service_Projects_Only INT,
                    Members INT,
                    Guest_Rtns INT,
                    Rotaractors INT,
                    Family INT,
                    Public INT,
                    club_For_Service_Projects_Only TEXT
                )
            ''')

            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

    def add_user_profile(self, Date, Service, Heading, content, Duration_in_Hours,
                         Cost_of_club_in_Rs_For_Service_Projects_Only, Volunteer_hours_For_Service_Projects_Only,
                         No_of_beneficiaries_For_Service_Projects_Only, Value_to_beneficiaries_in_Rs_For_Service_Projects_Only,
                         Members, Guest_Rtns, Rotaractors, Family, Public, club_For_Service_Projects_Only):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        if connection.is_connected():
            cursor = connection.cursor()


            cursor.execute("""
    INSERT INTO report_generation
    (DATE_OF_REPORT, Service, Heading, content, Duration_in_Hours,
    Cost_of_club_in_Rs_For_Service_Projects_Only,
    Volunteer_hours_For_Service_Projects_Only,
    No_of_beneficiaries_For_Service_Projects_Only,
    Value_to_beneficiaries_in_Rs_For_Service_Projects_Only, Members,
    Guest_Rtns, Rotaractors, Family, Public, club_For_Service_Projects_Only)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (Date, Service, Heading, content, Duration_in_Hours,
      Cost_of_club_in_Rs_For_Service_Projects_Only,
      Volunteer_hours_For_Service_Projects_Only,
      No_of_beneficiaries_For_Service_Projects_Only,
      Value_to_beneficiaries_in_Rs_For_Service_Projects_Only, Members,
      Guest_Rtns, Rotaractors, Family, Public, club_For_Service_Projects_Only))
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
                add_user_profile(*row)

        print("Data inserted successfully from CSV.")
    except Exception as e:
        print(f"Error inserting data from CSV: {str(e)}")


table = CreateTable()
table.connection_data_base()
print("Database created and Table created")

csv_file_path = Path("Data\\Generation.csv")
insert_data_from_csv(csv_file_path=csv_file_path, add_user_profile=table.add_user_profile)

print("The data inserted successfully")



























































