# -*- coding: utf-8 -*-
"""
helper utility to run subprocesses
"""

import os
import subprocess
import sys

from seasalt.utils import to_str, timed_subprocess

from seasalt.exceptions import CommandExecutionError, TimedProcTimeoutError


def run_cmd(cmd,
            cwd=os.getcwd(),
            stdin=None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            with_communicate=True,
            timeout=None,
            rstrip=True):
    """
    Execute the passed command and return a dict of return data
    :param rstrip:
    :param with_communicate:
    :param stderr:
    :param stdout:
    :param cwd:
    :param cmd:
    :param stdin:
    :param timeout:
    :return:
    """

    ret = {}

    kwargs = {
        'cwd': cwd,
        'stdin': str(stdin) if stdin is not None else stdin,
        'stdout': stdout,
        'stderr': stderr,
        'with_communicate': with_communicate,
        'universal_newlines': True
    }

    if not os.path.isabs(cwd) or not os.path.isdir(cwd):
        raise CommandExecutionError(
            'Specified cwd {0!r} either not absolute or does not exist'.format(cwd)
        )

    try:
        proc = timed_subprocess.TimedProc(cmd, **kwargs)
        ret['pid'] = proc.process.pid
    except (OSError, IOError) as exc:
        raise CommandExecutionError(
            'Unable to run command {0!r} with the context {1!r}, reason: {2}'.format(cmd, kwargs, exc)
        )

    proc_timed_out = True

    try:
        proc.wait(timeout)
        proc_timed_out = False
    except TimedProcTimeoutError as exc:
        ret['stdout'] = ''
        ret['stderr'] = str(exc)
        # in order to avoid other normal exit codes, we'll set this to something obscure
        ret['retcode'] = -sys.maxsize - 1

    ret['elapsed'] = proc.time_elapsed

    if not proc_timed_out:
        out, err = proc.stdout, proc.stderr

        if rstrip:
            if out is not None:
                out = to_str(out).rstrip()
            if err is not None:
                err = to_str(err).rstrip()

        ret['retcode'] = proc.process.returncode
        ret['stdout'] = out
        ret['stderr'] = err

    return ret
