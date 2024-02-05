import mysql.connector
from docraptor import DocApi, Doc
from jinja2 import Template
from financial.check_message import check_message_config

class DatabaseManager:
    def __init__(self, db_config, doc_raptor_api_key):
        self.db_config = db_config
        self.doc_raptor_api_key = doc_raptor_api_key

    def get_data_by_date(self, target_date, query_tb):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)

            print("Connected to MySQL database")
            query = query_tb
            cursor.execute(query, (target_date,))

            data = cursor.fetchall()
            print(data)
            return data
        except mysql.connector.Error as err:
            print(f"Error fetching data: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    def generate_pdf(self, html_content, pdf_name):
        try:
            configuration = DocApi.Configuration()
            configuration.api_key['apiKey'] = self.doc_raptor_api_key
            api_client = DocApi.ApiClient(configuration)

            doc_api = DocApi.DocApi(api_client)
            create_response = doc_api.create_doc(Doc.DocCreate(
                test=True,
                document_content=html_content,
                name=pdf_name,
                document_type="pdf",
            ))

            return create_response
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return None

    def render_html_template(self, template_content, data):
        template = Template(template_content)
        rendered_html = template.render(data=data)
        return rendered_html

class PdfGenerationPipeline:
    def __init__(self):
        pass
    def main(self, db_config, target_date, doc_raptor_api_key, html_path, query_tb, pdf_name):
        pdf_config = DatabaseManager(db_config, doc_raptor_api_key)
        data = pdf_config.get_data_by_date(target_date, query_tb)

        with open(html_path, 'r') as html_file:
            html_content = pdf_config.render_html_template(html_file.read(), data)

        pdf = pdf_config.generate_pdf(html_content, pdf_name=pdf_name)
        return pdf

class InvoiceGenerationPipeline:
    def main(self, db_config, doc_raptor_api_key, message, html_path, pdf_name):
        check_config = check_message_config()
        # Assuming check_message_config is a separate function
        data = check_config.main(db_config, message)  # You need to define this function

        manager = DatabaseManager(db_config, doc_raptor_api_key)
        html_content = manager.render_html_template(html_path.read_text(), data)
        pdf = manager.generate_pdf(html_content, pdf_name=pdf_name)
        return pdf

# You should define the missing check_message_config function

# Example usage:
# pdf_pipeline = PdfGenerationPipeline()
# pdf_result = pdf_pipeline.main(db_config, '2024-02-01', 'your_doc_raptor_api_key', 'your_template.html', 'your_query', 'output.pdf')
#
# invoice_pipeline = InvoiceGenerationPipeline()
# invoice_result = invoice_pipeline.main(db_config, 'your_doc_raptor_api_key', 'your_message', 'your_template.html', 'output_invoice.pdf')
