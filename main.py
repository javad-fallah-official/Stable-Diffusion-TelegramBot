import threading
import Telegram
from Response import response


def main():
    offset = 0
    while True:
        #reading all new messages with json
        data = Telegram.getUpdates(offset)
        # check if there is any message
        if 'result' in data:
            for Message in data["result"]:
                try:
                    threading.Thread(target=response, args=(Message,offset)).start()
                except Exception as e:
                    print(f"ERROR: {e}")
                #Basicly going to next message    
                offset = data["result"][-1]["update_id"] + 1
        else:
            continue


main()






