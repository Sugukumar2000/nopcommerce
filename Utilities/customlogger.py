import logging
import datetime

tm= datetime.datetime.now()

class  loggen:
    @staticmethod
    def LogGen():
        logging.basicConfig(filename=".\\Logs\\Autotest.log",
                        format='%(asctime)s: %(levelname)s:', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

