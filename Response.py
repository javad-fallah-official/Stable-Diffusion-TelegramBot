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

outputPath = os.getenv('OUTPUT_PATH')


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
            if user_id in generating_status and generating_status[user_id]:
                Telegram.sendMessage("You can only Imagine 1 Text at a time!⚠️", chat_id)
                return None
               
            prompt = text[8:].strip() if isPromptValid(text) else None

            if prompt:
                #changing user state to generating
                generating_status[user_id] = True
                
                #translating prompt
                prompt = translator.translate(prompt, dest='en').text
                
                Telegram.sendMessage("Generating Image...", chat_id)
                file_number = getPhotoNumber(chat_id)
                image = Comfy.gneratePhoto(prompt, chat_id, file_number, outputPath)
                waitForPhotoToGenerate(image, chat_id)
                Telegram.sendMessage("Uploading Image to Telegram...", chat_id)
                Telegram.sendPhoto(image, chat_id)
                Telegram.sendMessage(f"Your {prompt} is Successfully Made!",chat_id, keyboardStart)
                generating_status[user_id] = False
                return None
            
            else:
                Telegram.sendMessage(f"Invalid the prompt can`t be {text}",chat_id)
                return None
        
        elif text == "archive":
                sendArchiveKey(chat_id)  
                
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
    if (len(text) > 8) and not(text == "imagine!" or  text == "/generate" or text == "gen" or text == "\start" or text == "/start" or text == "start" or text == "\help" or text == "/help"):
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
        
def sendArchiveKey(chatId, text = ""):
    print(f"{chatId}")
    number = getPhotoNumber(chatId)
    a = number
    a = int(a)
    a = a - 1
    b = a - 1
    c = b - 1
    d = c - 1
    
    print(a)
    print(d)
    
    keyboardHistory = [['Imagine!']]
    
    while a > 1:
        keyboardHistory = keyboardHistory + [[f'{a}', f'{b}', f'{c}']] 
        a = a - 3
        b = a - 1
        c = '' if b - 1 == 0 else b - 1
    Telegram.sendMessage("histori",chatId, keyboardHistory)
        
        