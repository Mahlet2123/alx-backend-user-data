#!/bin/usr/env python3
""" filtered_logger """
from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str):
    """ returns the log message obfuscated """
    for field in fields:
        pattern = f'{field}=[^{separator}]+'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message

