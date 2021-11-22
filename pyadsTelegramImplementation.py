import pyads
from telebot import telegramBot

bot = telegramBot(botToken = "2117034745:AAEKKB-RV1l_vZr17NH9GNEZhBBG3HwKMIQ", chatID = "1124730952", graphDirectory= '')

AMSNETID = "10.123.67.6.1.1"

plc = pyads.Connection(AMSNETID, pyads.PORT_TC3PLC1)
plc.open()
print(f"Connected?: {plc.is_open}") #debugging statement, optional
print(f"Local Address? : {plc.get_local_address()}") #debugging statement, optional

# plc.write_by_name("MAIN.sWord", 'yeyeyeyyeye')
# print(plc.read_by_name("Main.sWord"))
while True:
    if plc.read_by_name("Main.bDUmmy"):
        bot.sendText("hello!!!")
    else:
        pass

plc.close()
