from twilio.rest import Client
import google.generativeai as genai 
import PIL.Image                                    




account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

board_members=[9791339999,9003535432,9952203666,9786000666,9994496460,9943030700,8667259494,9952705699,
               9894408567,9943434217,9842279290,9787770022,9894727272,9790087484,9894847232,7373200155,
               9443374468,9994200999,9362022255,9047077703,9942872000,9894054354,9843298951,9943515000,
               9841345994,9443081427,9842288883,9842213636,9894646469]
club_members=[7373717788,9994499988,9366629909,9095675000,9894077567,9894061764,9047052848,9360230187,
              9345555663,9894733996,9444999400,9894145962,9843111300,9443388633,9842223788,9843265775,
              9842257423,9600722590,9865036199,9842257106,9366629909,9894840490,984298812,9894747660,
              9600920774,8056765999,8508003335,9443724266,9488836000,8754230343,9486776061,8220870701,
              9003355555,9600978460,9894019019,9443016545,9843040051,9842227273,9994315167,9043390434,
              9865140077,9442533480,9487895554,9443185595,9597075043]




class President:
    def __init__(self):
        pass
    
    def generate_invitation(self,prompt,uploaded_image):
        image=PIL.Image.open(uploaded_image)
        vision_model = genai.GenerativeModel('gemini-pro-vision')
        response = vision_model.generate_content([prompt,image])
        text=response.text()
        return text

    def send_invitation(self,invitation_text, recipient_phone_number):
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=invitation_text,
                                         from_=twilio_phone_number,to=recipient_phone_number)
        print(f"Invitation sent to {recipient_phone_number}! Message SID: {message.sid}")


    
    def send_messages_to_bord_members(self,uploaded_image,prompt):
        for recipient_phone_number in board_members:
            invitation_text = self.generate_invitation(prompt,uploaded_image)
            self.send_invitation(invitation_text, recipient_phone_number)

    def send_messages_to_club_members(self,uploaded_image,prompt):
        for recipient_phone_number in club_members:
            invitation_text = self.generate_invitation(prompt,uploaded_image)
            self.send_invitation(invitation_text, recipient_phone_number) 
    

class President_send_message:
    def __init__(self):
        pass 

    def send_text_to_board_members(self,message):
        president=President()
        for recipient_phone_number in board_members:
            president.send_invitation(message,recipient_phone_number)

    def send_text_to_club_members(self,message):
        president=President()
        for recipient_phone_number in club_members:
            president.send_invitation(message,recipient_phone_number)




