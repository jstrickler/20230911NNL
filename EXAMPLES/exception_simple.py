import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="myprogram.log",
    format="%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s",
    datefmt="%x-%X",
    filemode='w',  #  default 'a'
)

logging.info("Start of program")
try:  # Execute code that might have a problem
    x = 5
    y = "cheese"
    logging.debug("Value of y is %s", y)
    z = x + y
    print("Bottom of try")

except Exception as err: #  TypeError as err:    # Catch the expected error; assign error object to err
    logging.exception("Naughty programmer")

logging.info("End of program")

#  -debug   logging.DEBUG
#  -verbose  logging.INFO

