#This file is the logic of The logic of the Bot
import Telegram


def response(Message,offset):
        # extrating datas from json
        text =     Message["message"]["text"].lower()
        chat_id =  Message["message"]["chat"]["id"]
        user_id =  Message["message"]["from"]["id"]
        username = Message["message"]["from"]["username"]
        print(Message)
        
        #printing the message to console
        print(username+": "+text)
        
        keyboardStart = [['Generate']]
        keyboardModes = [['Easy Mode', 'Advanced Mode'], ['Costume']]


        if text == "\start" or text == "/start" or text == "start":
            Telegram.sendMessage("Welcum!💦\nTo Text to Image!📸\nHow to use?🤔\nJust simply send your prompt and I will genarate your image!\nFor more info how to make a better photo tap \\help\nWhen ever stuck somewhere just type start to restart!\n\nMade by @nikobalek", id=chat_id)
        
        elif text == "hi" or text == "hello" or text == "bye":
            Telegram.sendMessage(f"What the FUCK is {text}?!\nGIVE ME PROMPT BITCH!", chat_id)

        elif text == "generate" or text =="/generate" or text =="gen":
            Telegram.sendMessage("choose the mode",chat_id,keyboardModes)
            
        else :
            Telegram.sendMessage(f"Invalid", chat_id)
            
        
            


