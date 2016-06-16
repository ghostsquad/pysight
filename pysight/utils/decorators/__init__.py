# -*- coding: utf-8 -*-
"""
Various decorators
"""
from functools import wraps


def memoize(func):
    """
    Memoize aka cache the return output of a function
    given a specific set of arguments
    """
    cache = {}

    @wraps(func)
    def _memoize(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return _memoize
