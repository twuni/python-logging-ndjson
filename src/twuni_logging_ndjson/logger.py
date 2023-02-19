"""
This module holds the Logger -- the class you should use for emitting logs.
"""

from datetime import datetime
from json import dumps as to_json


class Logger:
    """
    The `Logger` object is responsible for emitting log events to standard output in NDJSON format.
    Each log event has, at minimum, a `"level"`, `"timestamp"`, and `"event"` properties.
    The `"event"` property is an object that has, at least, a `"type"` property.
    """

    __LogLevel = {"DEBUG": 0, "INFO": 10, "WARNING": 20, "ERROR": 30, "CRITICAL": 40}

    def __init__(self, *, level="INFO"):
        self.level = level

    def __loggable(self, target_level):
        return self.__LogLevel[self.level] <= self.__LogLevel[target_level]

    def __log(self, level, event_type, event_context=None):
        if not self.__loggable(level):
            return

        payload = {}
        payload["event"] = {}
        if event_context is not None:
            payload["event"]["context"] = event_context
        payload["event"]["type"] = event_type
        payload["level"] = level
        payload["timestamp"] = datetime.utcnow().isoformat()
        print(to_json(payload, separators=(",", ":")))

    def debug(self, event_type, event_context=None):
        """
        Emits a log event at the DEBUG level.
        """
        self.__log("DEBUG", event_type, event_context)

    def info(self, event_type, event_context=None):
        """
        Emits a log event at the INFO level.
        """
        self.__log("INFO", event_type, event_context)

    def warning(self, event_type, event_context=None):
        """
        Emits a log event at the WARNING level.
        """
        self.__log("WARNING", event_type, event_context)

    def error(self, event_type, event_context=None):
        """
        Emits a log event at the ERROR level.
        """
        self.__log("ERROR", event_type, event_context)

    def critical(self, event_type, event_context=None):
        """
        Emits a log event at the CRITICAL level.
        """
        self.__log("CRITICAL", event_type, event_context)
