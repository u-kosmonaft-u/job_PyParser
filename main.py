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
    logging.error(f"There is no config file! {e}")

if __name__ == '__main__':
    # Main entrypoint
    while True:
        try:
            req = request_hh('https://api.hh.ru/vacancies')
            time.sleep(3600)
        except Exception as e:
            logging.debug(f"Some error occurred in main script! Error: {e}")
