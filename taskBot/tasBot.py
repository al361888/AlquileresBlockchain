import telegram
import logging
import telegram.ext

token = '1031956446:AAEqMOHrjTmC5lC0ub6sBbUrX-gY5pzfAdA'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    bot = context.bot
    text = "Hola putos"
    chat_id = update.message.chat_id


if __name__ == '__main__':
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None


   start()
