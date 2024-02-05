import mysql.connector
import pdfkit


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Girish@1997',
    'database': 'chat_bot'
}
import mysql.connector
import pdfkit

class ChatBotPDFGenerator:
    def __init__(self, db_config):
        self.db_config = db_config

    def get_details(self, phone_number):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)

            print("Connected to MySQL database")
            query = "SELECT * FROM rotaryclubmembers WHERE PhoneNumber = %s"
            cursor.execute(query, (phone_number,))

            student = cursor.fetchone()
            print(student)
            return student
        except mysql.connector.Error as err:
            print(f"Error fetching student data: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    def generate_pdf(self, html_content, output_pdf):
        try:
            # Corrected path
            path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            pdfkit.from_string(html_content, output_pdf, configuration=config, options={"enable-local-file-access": ""})
            print("PDF generation successful")
            return output_pdf
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return None

    def generate_student_pdf(self, phone_number,html_path):
        data = self.get_student_data(phone_number)

        if data:
            try:
                # Render HTML template (Replace with your own HTML template)

                print("HTML rendering successful")

                # Generate PDF from the rendered HTML
                pdf_content = self.generate_pdf(html_path, 'new_file.pdf')

                if pdf_content:
                    print("PDF generation successful")
                    # You can save the PDF or return it as needed
                    return pdf_content
                else:
                    print("Error generating PDF")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No data found for the provided WhatsApp number")
            return None

# Example usage:
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Girish@1997',
    'database': 'chat_bot'
}

chatbot_pdf_generator = ChatBotPDFGenerator(db_config)
pdf_content = chatbot_pdf_generator.generate_student_pdf('your_phone_number','html_path')

# You can then use pdf_content as needed (e.g., send it as a response, save it, etc.)


    

    