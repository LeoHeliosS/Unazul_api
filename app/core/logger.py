import sys

from loguru import logger

logger.remove()
logger.add(
    sys.stdout,
    format="{time} | {level} | {message}",
    level="INFO",
    #rotation="10 MB",
    #  retention="10 days"
)