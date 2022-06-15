import config
import telebot
from random import randint


bot = telebot.TeleBot(config.TOKEN)
secretNum = 0
inGame = False
TRY = 1
@bot.message_handler(commands=["start"])
def start(message):
	text = "Привет, "+str(message.from_user.first_name)+"!\n Чтобы начать игру, нажми /game"
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["game"])
def game(message):
	global secretNum,inGame
	secretNum = randint(1,100)
	inGame = True
	bot.send_message(message.chat.id,"Я загадал число от 1 до 100 угадай его")

@bot.message_handler(func = lambda message:message.text.isdigit()== True and inGame==True )
def game(message):
	global secretNum,inGame,TRY
	usernum = int(message.text)
	if usernum > secretNum:
		bot.send_message(message.chat.id,"Моё число меньше")
		TRY += 1
	if usernum < secretNum:
		bot.send_message(message.chat.id,"Моё число больше")
		TRY += 1
	if usernum == secretNum:
		bot.send_message(message.chat.id,"Ты угадал!!!")
		bot.send_message(message.chat.id,"Тебе потребовалось "+ str(TRY) +" попытки(-ок)")
		inGame = False
		TRY = 1

if __name__ == '__main__':
	bot.infinity_polling()

