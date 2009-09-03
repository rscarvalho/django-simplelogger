from django.conf import settings
import logging

# Python logging reference:
# http://docs.python.org/library/logging.html

ENABLED = getattr(settings, "LOGGER_ENABLED", False)
BACKEND = getattr(settings, "LOGGER_BACKEND", "file")
FILENAME = getattr(settings, "LOGGER_FILENAME", "log/django.log")
LEVEL = getattr(settings, "LOGGER_LOGLEVEL", logging.DEBUG)

# Should contains a dictionary containing keys for RotatingFileHandler
ROTATE = getattr(settings, "LOGGER_ROTATE", None)

FORMAT = getattr(settings, "LOGGER_FORMAT", 
                           "[%(asctime)s][%(levelname)s] %(name)s: %(message)s")
                           
DATE_FORMAT = getattr(settings, "LOGGER_DATE_FORMAT", "%Y-%m-%d %H:%M:%S")
