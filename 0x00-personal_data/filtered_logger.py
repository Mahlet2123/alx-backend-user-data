#!/usr/bin/env python3
""" filtered_logger """
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        log_message = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            log_message,
            self.SEPARATOR,
        )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        pattern = f"{field}=[^{separator}]+"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """
    function that takes no arguments and returns a
    logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Do not propagate messages to other loggers

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    returns a connector to the database
    (mysql.connector.connection.MySQLConnection object).
    """
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")

    connector = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pwd,
        database=db_name
    )

    return connector


def main() -> None:
    """main function"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * from users")
    all_fields = (
        "name",
        "email",
        "phone",
        "ssn",
        "password",
        "ip",
        "last_login",
        "user_agent",
    )
    for msg in cursor:
        # Create a formatted message with field=value pairs
        message = ";".join(
            [f"{field}={value}" for field, value in zip(all_fields, msg)]
        )
        user_log = logging.LogRecord(
            "user_data", logging.INFO, None, None, message, None, None
        )
        formatter = RedactingFormatter(PII_FIELDS)
        print(formatter.format(user_log))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
