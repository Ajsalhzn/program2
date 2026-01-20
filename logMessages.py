import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug("This is DEBUG message.")
logger.info("This is an INFO messege.")
logger.warning("This is a WARNING messege.")
logger.error("This is an ERROR messege.")
logger.critical("This is an CRITICAL messege")