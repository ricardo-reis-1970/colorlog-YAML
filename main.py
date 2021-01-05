from logger.logger import logger


# Get the default fallback root logger
default_logger = logger(__name__)
default_logger.debug('This is a debug message with a non-configured logger name. It will default to root config.')

# Get the specific configured logger
sample_logger = logger('sampleLogger')
sample_logger.debug('This is a debug message with sampleLogger. See the difference?')
sample_logger.warning('This is a warning message with appLogger. It\'s getting dangerous...')