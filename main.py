from log import getLogger
from module import printHelloWorld


logger = getLogger()
logger.debug("Start main")
printHelloWorld()
logger.debug("[*] End main")
