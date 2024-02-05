import os
import google.generativeai as genai
from Template import PDF_CONVERSION
import google.generativeai as palm
import pandas as pd



os.environ['GOOGLE_API_KEY']='AIzaSyB2pkELdV1dA8ylaKlqV4wXN8HPK26sGp0'
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


class conversion:
    def __init__(self,data):
        self.data=data


    def get_profile(self,member_id):

        df=pd.read_csv('Data\club members.csv')
        for row in df.iterrows():
            if row[1]['Member ID'] == member_id:
                content=row
        return content



    def conversion_chat(self):
        self.data=self.data.lower()
        response=palm.chat(messages=self.data,temperature=0.5,context="you are ai bot")
        for message in response.messages:
            if "id" in message['content']:
                id=int(input("Enter your id"))
                data=self.get_profile(id)
                print(data)
                break
            elif "report" in  message["content"]:
                print("i will assist you to create report")
                break
            elif "dues" in  message["content"]:
                print("i will assist you to clear the dues")
                break
            elif "bill" in message["content"]:
                print("i will help for bill generation")
                break
            elif "80G-certificate" in message["content"]:
                print("i will assist you for the")
                break
            else:
                print("How may assist u")






                     








