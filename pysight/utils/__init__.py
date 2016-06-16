import re
import sys
from datetime import datetime


def to_str(s, encoding=None):
    """
    Given str, bytes, bytearray, or unicode (py2), return str
    """
    if s is None:
        return None
    if isinstance(s, str):
        return s
    if isinstance(s, (bytes, bytearray)):
        return s.decode(encoding or sys.getdefaultencoding())

    msg = 'expected str, bytes, or bytearray, but found {0}'.format(str(type(s)))
    raise TypeError(msg)


def to_bytes(s, encoding=None):
    """
    Given bytes, bytearray, str, or unicode (python 2), return bytes (str for
    python 2)
    """

    if isinstance(s, bytes):
        return s
    if isinstance(s, bytearray):
        return bytes(s)
    if isinstance(s, str):
        return s.encode(encoding or sys.getdefaultencoding())
    raise TypeError('expected bytes, bytearray, or str')


def human_size_to_bytes(human_size):
    """
    Convert human-readable units to bytes
    """
    size_exp_map = {'K': 1, 'M': 2, 'G': 3, 'T': 4, 'P': 5}
    human_size_str = str(human_size)
    match = re.match(r'^(\d+)([KMGTP])?$', human_size_str)
    if not match:
        raise ValueError(
            'Size must be all digits, with an optional unit type '
            '(K, M, G, T, or P)'
        )
    size_num = int(match.group(1))
    unit_multiplier = 1024 ** size_exp_map.get(match.group(2), 0)
    return size_num * unit_multiplier


def is_true(value=None):
    """
    Returns a boolean value representing the "truth" of the value passed. The
    rules for what is a "True" value are:
        1. Integer/float values greater than 0
        2. The string values "True" and "true"
        3. Any object for which bool(obj) returns True
    """
    # First, try int/float conversion
    try:
        value = int(value)
    except (ValueError, TypeError):
        pass
    try:
        value = float(value)
    except (ValueError, TypeError):
        pass

    # Now check for truthiness
    if isinstance(value, (int, float)):
        return value > 0
    elif isinstance(value, str):
        return str(value).lower() == 'true'
    else:
        return bool(value)


def concat_strings(values):
    return ''.join([str(value) for value in values])


def is_str_null_or_whitespace(value):
    if not isinstance(value, str):
        return False

    if len(value) > 0 and not value.isspace():
        return False

    return True


_float_regex = re.compile(r'^\d+\.\d+$')
_int_regex = re.compile(r'^\d+$')
_yes_no_regex = re.compile(r'^(yes|no)$', re.IGNORECASE)
_bool_regex = re.compile(r'^(true|false|yes|no)$', re.IGNORECASE)
_datetimeampm_pattern = '%m/%d/%y %I:%M %p'
_datetime_pattern = '%Y-%m-%d %H:%M:%S'
_dateonly_pattern = '%Y-%m-%d'


def to_primitive(value):
    if value is None:
        return None

    if isinstance(value, (float, int, bool, datetime)):
        return value

    value = str(value).strip()

    if is_str_null_or_whitespace(value):
        return None

    if _int_regex.match(value):
        return int(value)

    if _float_regex.match(value):
        return float(value)

    if _yes_no_regex.match(value):
        return value.lower() == 'yes'

    if _bool_regex.match(value):
        return value.lower() == 'true'

    try:
        return datetime.strptime(value, _datetimeampm_pattern)
    except Exception:
        pass

    try:
        return datetime.strptime(value, _datetime_pattern)
    except Exception:
        pass

    try:
        return datetime.strptime(value, _dateonly_pattern)
    except Exception:
        pass

    return str(value)
