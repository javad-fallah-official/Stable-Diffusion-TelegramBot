import Telegram

def response(Message,offset):
        # extrating datas from json
        text =     Message["message"]["text"].lower()
        chat_id =  Message["message"]["chat"]["id"]
        user_id =  Message["message"]["from"]["id"]
        username = Message["message"]["from"]["username"]
        
        #printing the message to console
        print(username+": "+text)


        if text == "\start" or text == "/start" or text == "start":
            Telegram.Say("Welcum!💦\nTo Text to Image!📸\nHow to use?🤔\nJust simply send your prompt and I will genarate your image!\nFor more info how to make a better photo tap \\help\nWhen ever stuck somewhere just type start to restart!\n\nMade by @nikobalek", id=chat_id)
        
        
        elif text == "hi" or text == "hello" or text == "bye":
            Telegram.Say(f"What the FUCK is {text}?!\nGIVE ME PROMPT BITCH!", chat_id)

        else :
            Telegram.Say(f"Invalid", chat_id)
            
        
        # elif text == "generate" or text =="/generate" or text =="gen":
            
    #         sendMessage("Enter your prompt", chat_id)
    #         prompt = Read_input_message(chat_id, offset)
            
    #         if prompt.lower() == "generate" or prompt.lower() =="/generate" or prompt.lower() =="gen":
    #             return 0
                
    #         translated = translator.translate(prompt, dest='en')
    #         prompt = translated.text
    #         print(prompt)

    #         sendMessage("Generating Image...", chat_id)
    #         if os.path.isdir(f"{outputPath}\\{chat_id}"):
    #             print("dir exists")
    #             if os.path.isfile(f'{outputPath}\\{chat_id}\\{chat_id}.txt'):
    #                 print("file exists")
    #                 with open(f'{outputPath}\\{chat_id}\\{chat_id}.txt','r') as f:
    #                     file_number = f.read()
    #                     print(file_number)
    #             else:
    #                 print("file doesnt exist")
    #                 file_number = 1
    #         else:
    #             print("dir doesnt exist")
    #             file_number = 1
                    
    #         image = gneratePhoto(prompt, chat_id, file_number)
    #         time.sleep(15)
    #         sendMessage("Image Generated!", chat_id)

    #         sendMessage("Uploading Image to Telegram...", chat_id)
    #         sendPhoto(image, chat_id)
    #         sendMessage(f"Your {prompt} is Successfully Made!", chat_id, keyboardStart)
    

