import logging

logger = logging.getLogger("db locker")

isLock = False


def lock():
    global isLock
    logger.info("lock")
    isLock = True


def unlock():
    global isLock
    logger.info("unlock")
    isLock = False
