#!/usr/bin/env python3
""" filtered_logger """
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format method """
        log_message = super().format(record)
        return self.filter_datum(
                self.fields,
                self.REDACTION,
                log_message,
                self.SEPARATOR
                )

    def filter_datum(
            self,
            fields: List[str],
            redaction: str,
            message: str,
            separator: str) -> str:
        """ returns the log message obfuscated """
        for field in fields:
            pattern = f'{field}=[^{separator}]+'
            message = re.sub(pattern, f'{field}={redaction}', message)
        return message
