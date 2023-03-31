import requests, telebot, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_KEY"))

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "/all - all games;\n/sr - Shopify rebelion;\n/gg - Gaiming gladiators;\n/tundra - Tundra;")

@bot.message_handler(commands=['all'])
def send_all(message):

    url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        

    for game in soup.find_all('table', {'class': 'wikitable'}):
        mainData = game.find('tbody')
        
        if((mainData.find_all('tr')[0].get("style") == "background-color:#ffffcc;")):
            try:
                team_left = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[0].find("span").find("span").find("a").text.split())
                pass
            except:
                team_left = "TBD"
                pass

            try:
                team_right = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[2].find("span").find_all("span")[2].find("a").text.split())
                pass
            except:
                team_right = "TBD"
                pass
            
            try:
                countdown = ' '.join(str(e) for e in mainData.find_all('tr')[1].find("td").find("span").find("span").text.split())
                pass
            except:
                countdown = "TDB"
                pass

            gameData = f"{team_left} vs {team_right} on {countdown}"
            if(len(gameData) != 0):
                bot.send_message(message.chat.id, gameData)

@bot.message_handler(commands=["sr"])
def send_shopify(message):
    url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        

    for game in soup.find_all('table', {'class': 'wikitable'}):
        mainData = game.find('tbody')
        
        if((mainData.find_all('tr')[0].get("style") == "background-color:#ffffcc;")):
            try:
                team_left = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[0].find("span").find("span").find("a").text.split())
                pass
            except:
                team_left = "TBD"
                pass

            try:
                team_right = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[2].find("span").find_all("span")[2].find("a").text.split())
                pass
            except:
                team_right = "TBD"
                pass
            
            try:
                countdown = ' '.join(str(e) for e in mainData.find_all('tr')[1].find("td").find("span").find("span").text.split())
                pass
            except:
                countdown = "TDB"
                pass

            if(team_left == "SR" or team_right == "SR"):
                gameData = f"{team_left} vs {team_right} on {countdown}"
                if(len(gameData) != 0):
                    bot.send_message(message.chat.id, gameData)

@bot.message_handler(commands=["gg"])
def send_gg(message):
    url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        

    for game in soup.find_all('table', {'class': 'wikitable'}):
        mainData = game.find('tbody')
        
        if((mainData.find_all('tr')[0].get("style") == "background-color:#ffffcc;")):
            try:
                team_left = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[0].find("span").find("span").find("a").text.split())
                pass
            except:
                team_left = "TBD"
                pass

            try:
                team_right = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[2].find("span").find_all("span")[2].find("a").text.split())
                pass
            except:
                team_right = "TBD"
                pass
            
            try:
                countdown = ' '.join(str(e) for e in mainData.find_all('tr')[1].find("td").find("span").find("span").text.split())
                pass
            except:
                countdown = "TDB"
                pass

            if(team_left == "GG" or team_right == "GG"):
                gameData = f"{team_left} vs {team_right} on {countdown}"
                if(len(gameData) != 0):
                    bot.send_message(message.chat.id, gameData)

@bot.message_handler(commands=["tundra"])
def send_tundra(message):
    url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        

    for game in soup.find_all('table', {'class': 'wikitable'}):
        mainData = game.find('tbody')
        
        if((mainData.find_all('tr')[0].get("style") == "background-color:#ffffcc;")):
            try:
                team_left = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[0].find("span").find("span").find("a").text.split())
                pass
            except:
                team_left = "TBD"
                pass

            try:
                team_right = ''.join(str(e) for e in mainData.find_all('tr')[0].find_all("td")[2].find("span").find_all("span")[2].find("a").text.split())
                pass
            except:
                team_right = "TBD"
                pass
            
            try:
                countdown = ' '.join(str(e) for e in mainData.find_all('tr')[1].find("td").find("span").find("span").text.split())
                pass
            except:
                countdown = "TDB"
                pass

            if(team_left == "Tundra" or team_right == "Tundra"):
                gameData = f"{team_left} vs {team_right} on {countdown}"
                if(len(gameData) != 0):
                    bot.send_message(message.chat.id, gameData)

bot.infinity_polling()
