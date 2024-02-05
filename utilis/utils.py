import os
import mysql.connector
import pdfkit
from flask import render_template
import cv2
from PIL import Image
import pytesseract


# Specify the path to the wkhtmltopdf executable
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  

# Configure pdfkit with the path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# MySQL Database Configuration
class Database_config:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.db_config = {
            'host': self.host,
            'user': self.user,
            'password': self.password,
            'database': self.database}
        
    def connection_database(self,id):
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor(dictionary=True)

    # Query the database
        query = "SELECT * FROM WHERE 'MemberID' ={}".format(id)
        cursor.execute(query)
        data = cursor.fetchone()
    # Close the database connection
        cursor.close()
        conn.close()
        return data
    
    def convert_to_pdf(self,file_path):
        
        student_data=self.connection_database
        
        rendered_template = render_template(file_path, student_data=student_data)

    # Convert rendered template to PDF
        pdf_content = pdfkit.from_string(rendered_template, False, configuration=config)
        
        return pdf_content
    
class Check_data_image:
    def __init__(self):
        pass

    def is_image(self,image_path):
        try:
            img = cv2.imread(image_path)
            if img:
                return True
        except Exception as e:
            return False

    def is_text(text_path):
        try:
            with open(text_path, 'r') as file:
                text_content = file.read()
            return any(char.isalpha() for char in text_content)
        except Exception as e:
            return False




































