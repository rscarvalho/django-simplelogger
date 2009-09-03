import logging
from simplelogger import settings
import os
from django.http import HttpRequest

class LoggingMiddleware(object):
    def process_request(self, request):
        if not settings.ENABLED:
            return
        
        if settings.BACKEND == "file":
            # print "Logging Enabled!"
            dirname = os.path.dirname(settings.FILENAME)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            
            logging.basicConfig(level=settings.LEVEL,
                                filename=settings.FILENAME,
                                format=settings.FORMAT,
                                datefmt=settings.DATE_FORMAT)
            HttpRequest.logger = logging.getLogger(request.path)
