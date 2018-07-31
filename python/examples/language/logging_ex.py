import logging

# There are 5 logging levels
logging.basicConfig(filename='C:\\temp\\log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s = %(message)s')
logging.disable(logging.CRITICAL)

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s)')
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is {}, total is {}'.format(i, total))
    logging.debug('Return value is {}'.format(total))
    return total

factorial(10)
