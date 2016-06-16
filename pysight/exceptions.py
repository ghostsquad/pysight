# -*- coding: utf-8 -*-
"""
This module is a central location for all seasalt exceptions
"""


class SeasaltException(Exception):
    """
    Base exception class; all seasalt-specific exceptions should subclass this
    """
    strerror = None

    def __init__(self, message=''):
        super(SeasaltException, self).__init__(message)
        self.strerror = message


class TimedProcTimeoutError(SeasaltException):
    """
    Thrown when a timed subprocess does not terminate within the timeout,
    or if the specified timeout is not an int or a float
    """


class CommandExecutionError(SeasaltException):
    """
    Used when a command which returns an error and wants
    to show the user the output gracefully instead of dying
    """
