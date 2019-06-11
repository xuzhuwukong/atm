import logging
import unittest
class lgtest(unittest.TestCase):
    logging.basicConfig(filename='./'+__name__+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                        level = logging.NOTSET,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p')
    def main(self):
        logging.error("这是一条error信息的打印")
        logging.info("这是一条info信息的打印")
        logging.warning("这是一条warn信息的打印")
        logging.debug("这是一条debug信息的打印")
if __name__=='__main__':
    unittest.main()
