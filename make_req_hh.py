import requests
from tinydb import TinyDB, Query
import telebot
import logging
import yaml


logging.debug("Try to read config.yml")
try:
    with open("config.yml", "r") as config:
        cfg = yaml.safe_load(config)
except Exception as e:
    print("There is no file as config.yml!")

logging.basicConfig(filename=cfg['log']['path'],
                    level=cfg['log']['level'],
                    filemode=cfg['log']['filemode'])

# Init TinyDB as database
db = TinyDB(cfg['database']['name'])
logging.debug("Init database file")
# Init database query
q = Query()
logging.debug("Init database query")
# Init telegram bot
bot = telebot.TeleBot(token=(cfg['telegram']['token']),
                      parse_mode=None)
logging.debug("Init telegram bot")


def request_hh(url):
    # Init parameters for request
    job_name = cfg['job']
    parameters = {
        'text': f'NAME:{job_name}'
    }
    logging.debug("Init parameters for request")
    # make request to api and jsonify it
    r = requests.get(url, params=parameters).json()
    logging.debug("init request object")
    # get only vacancy from json
    only_items = r['items']
    logging.debug("Create list of vacancies")
    # init new empty list for vacancy with usd
    vacancy_with_usd = []
    logging.debug("Create empty list of vacancies only $ payment")
    # For cycle to find only vacancies with usd
    logging.debug("start cycle for in vacancies list")
    for i in range(len(only_items)):
        salary = only_items[i]['salary']
        try:
            currency = salary.get('currency')
            if currency == "USD":
                vacancy_with_usd.append(only_items[i])
        except Exception as e:
            logging.error("None type object occurred! It's probably empty salary item in api json answer")
    # Checkout that id vacancy already has been added
    logging.debug("Start for cycle to checkout vacancy is new")
    for vacancy in vacancy_with_usd:
        if db.search(q.id.matches(vacancy['id'])):
            pass
        else:
            # If no such vacancy in database, add vacancy in db and send message in telegram
            db.insert({'id': vacancy['id'], 'name': vacancy['name'], 'url': vacancy['alternate_url']})
            logging.debug("Send telegramm message")
            bot.send_message(chat_id=cfg['telegram']['chat_id'],
                             text='Hello! There is a new vacancy for you! \n'
                                  + vacancy['name'] + '\n'
                                  + 'link: '
                                  + vacancy['alternate_url'])
