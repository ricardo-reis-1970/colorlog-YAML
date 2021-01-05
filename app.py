from logger.logger import logger


# Get the specific configured logger
sample_logger = logger('appLogger')
sample_logger.warning('This is a warning message with appLogger. It\'s getting dangerous...')