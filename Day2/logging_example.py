import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("logs.txt"),logging.StreamHandler()])

logging.debug("This is aDEBUG message")
logging.info("General info about the program flow")
logging.warning("Low disk space warning")
logging.error("An error occured!")
logging.critical("There is a critical issue!")

try:
    x = int(input("Enter the number: "))
    result = 100/x
    logging.info(f"100 divided by {x} is {result}")
except ZeroDivisionError:
    logging.error("Cannot divided by zero")
except ValueError:
    logging.info("Invalid Input.")
logging.info("Program finished...............")