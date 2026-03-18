import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler("Logs_assignment.txt"), logging.StreamHandler()])


filename ="example_assignment.txt"

try:
    with open(filename,"w") as file:
        file.write("Hello we are writing in the file\n")
        file.write("We are learning file handling with logging")
    logging.info(f"Data written successfully to '{filename}'")
except Exception as e:
    logging.error(f"Error writing to file: {e}")


try:
    with open(filename,"a") as file:
        file.write("This is a appended at the end")
    logging.info(f"Data appended successfully to the file '{filename}'")
except Exception as e:
    logging.error("Error while appending to file: {e}")


try:
    with open(filename,"r") as file:
       logging.info(f"Reading file contents '{filename}'")

       for line in file:
        print(line.strip())
except FileNotFoundError:
    logging.error(f"File '{filename}' is not found!!")

except Exception as e:
    logging.error("Error while reading file: {e}")

      

logging.info("File processing Successfully")