from threading import Thread

from bots.stupid import bot
import data

def run():
    cmd = data.game_commads.get()
    print("do:", cmd)

t_bot = Thread(target=bot.bot)
t_bot.daemon = True
t_bot.start()


t_game = Thread(target=run)
t_game.daemon = True
t_game.start()
