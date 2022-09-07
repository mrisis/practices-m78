from os import name as os_name, system as terminal
import logging



def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)-s - %(levelname)-s - %(message)s')

file_handler = logging.FileHandler('file_shop.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logger.addHandler(file_handler)



