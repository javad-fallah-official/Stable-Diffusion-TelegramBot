from googletrans import Translator
import threading
from PIL import Image
import os
import Telegram
from Response import response
from dotenv import load_dotenv

# reading .env variables
load_dotenv()

translator = Translator()
filename= ""
comfyUrl =  os.getenv('COMFY_UI_URL') 
outputPath = os.getenv('OUTPUT_PATH') 




def main():
    offset = 0
    while True:
        #reading all new messages with json
        data = Telegram.Read_message(offset)
        # check if there is any message
        if 'result' in data:
            for Message in data["result"]:
                try:
                    threading.Thread(target=response, args=(Message,offset)).start()
                except:
                    pass
                #Basicly going to next message    
                offset = data["result"][-1]["update_id"] + 1
        else:
            continue


main()






