#This file is the logic of The logic of the Bot
import Telegram
import  os
from dotenv import load_dotenv
from googletrans import Translator
import Comfy

# reading .env variables
load_dotenv()
generating_status = {}
translator = Translator()

outputPath = os.envget('OUTPUT_PATH')


def response(Message,offset):
        # extrating datas from json
        text =     str(Message["message"]["text"].lower())
        chat_id =  Message["message"]["chat"]["id"]
        user_id =  Message["message"]["from"]["id"]
        username = Message["message"]["from"]["username"]
        print(Message)
        
        #printing the message to console
        print(username+": "+text)
        

        keyboardStart = [['Imagine!'], ['Archive']]
        keyboardCancel = [['Cancel']]
        keyboardModes = [['Easy Mode', 'Advanced Mode'], ['Costume']]


        if text == "\start" or text == "/start" or text == "start":
            Telegram.sendMessage("welcome!\nTo Text to Image!📸\nHow to use?🤔\nJust simply send your text and I will imagine your text!\nFor more info how to make a better photo tap /help\nWhen ever stuck somewhere just type start to restart!\n\nMade by @nikobalek", chat_id, keyboardStart)
        
        elif text == "hi" or text == "hello" or text == "bye":
            Telegram.sendMessage(f"What the FUCK is {text}?!\nGIVE ME PROMPT BITCH!", chat_id)

        elif text.startswith("/generate") :   
            
            #check if user generating
            if generating_status[user_id]:
                Telegram.sendMessage("You can only Imagine 1 Text at a time!⚠️", chat_id)
                return None

            #asking for prompt
            Telegram.sendMessage("Enter your Text for me to Imagine!",chat_id, keyboardCancel)
            
            
            prompt = text[8:].strip() if isPromptValid(text) else None

            if prompt:
                
                #changing user state to generating
                generating_status[user_id] = True
                prompt = translator.translate(prompt, dest='en').text
                Telegram.sendMessage("Generating Image...", chat_id)
                file_number = getPhotoNumber(chat_id)
                image = Comfy.gneratePhoto(prompt, chat_id, file_number, outputPath)
                waitForPhotoToGenerate(image, chat_id)
                with open(f"{outputPath}\\{chat_id}\\isGenerating.txt", 'w') as f:
                    f.write("0")
                Telegram.sendMessage("Uploading Image to Telegram...", chat_id)
                Telegram.sendPhoto(image, chat_id)
                Telegram.sendMessage(f"Your {prompt} is Successfully Made!",chat_id, keyboardStart)
                return 0
            
            else:
                Telegram.sendMessage(f"Invalid the prompt can`t be {text}",chat_id)
                return None
      
        
        
           
            
            
            
            
            
            
        else :
            Telegram.sendMessage(f"Invalid", chat_id)
            
            
def isGenerating(chat_id):
    if os.path.exists(f"{outputPath}\\{chat_id}"):
        if os.path.exists(f"{outputPath}\\{chat_id}\\isGenerating.txt"):
            with open(f"{outputPath}\\{chat_id}\\isGenerating.txt", 'r') as f:
                status = f.read()
                return status
        else:
            return False
    else:
        return False
    
    
    
def isPromptValid(text):
    if (text.len() > 8) and not(text == "imagine!" or  text == "/generate" or text == "gen" or text == "\start" or text == "/start" or text == "start" or text == "\help" or text == "/help"):
        return True
    else:
        return False
    
def getPhotoNumber(chat_id):
    if os.path.isdir(f"{outputPath}\\{chat_id}"):
                if os.path.isfile(f'{outputPath}\\{chat_id}\\{chat_id}.txt'):
                    with open(f'{outputPath}\\{chat_id}\\{chat_id}.txt', 'r') as f:
                        photoNumber = f.read()
                        return photoNumber
                else:
                    return True
    else:
        return True
    
def waitForPhotoToGenerate(photoPath, userWhoRequested):
    #must add a timeout
    while True:
        if os.path.exists(photoPath):
            Telegram.sendMessage("Image Generated!", userWhoRequested)
            break