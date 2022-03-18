from make_req_hh import request_hh
import logging
import time
import yaml

# Python script to parse $ currency vacancy from hh.ru


try:
    with open("config.yml", "r") as config:
        cfg = yaml.safe_load(config)
except Exception as e:
    print("There is no file as config.yml!")
    logging.error("There is no config file!")

while True:
    # Main entrypoint
    if __name__ == '__main__':
        try:
            req = request_hh('https://api.hh.ru/vacancies')
            time.sleep(3600)
        except Exception as e:
            logging.debug("Some error occurred in main script" + e)



