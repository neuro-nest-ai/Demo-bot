
from image_to_text import Image_model_config
from pdf_generation import PdfConfigModel
from utilis.utils import Check_data_image
import google.generativeai as palm



class Generative_answer:
    def __init__(self,data):
        self.data=data
    def generate_answer(self,data):
        text_image=Check_data_image()
        image=text_image.is_image(data)
        return image
    def text_generation(self,data):
        data = data.lower()
        response = palm.chat(messages=data, temperature=0.7, context="you act like ai bot")
        for message in response.messages:
            if "report_genertion" in  message["content"]:
                print("i will assist you to create report")
            elif "dues" in  message["content"]:
                print("i will assist you to clear the dues")
            else:
               data=PdfConfigModel()
               data=data.user_input(message)
               content = ""
        for message in response.messages:
            content += message['content']
        return content
    