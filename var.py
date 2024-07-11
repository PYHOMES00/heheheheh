import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "28243586"))
    API_HASH = os.getenv("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7199826962:AAHlDShAuSI01ywwo-r_gEYWN5hW9QUrHas")
    sudo = os.getenv("SUDO", "5340652544")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
