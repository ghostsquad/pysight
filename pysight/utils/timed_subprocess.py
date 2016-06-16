import os
from seasalt.utils import to_str
import subprocess
import threading
from seasalt.exceptions import TimedProcTimeoutError
from seasalt.utils.timer import Timer


class TimedProc(object):
    """
    Create a TimedProc object, calls subprocess.Popen with passed args and **kwargs
    """

    command = None
    stdin = None
    stdout = None
    stderr = None
    with_communicate = None
    process = None
    time_elapsed = None

    def __init__(self, args, **kwargs):
        # start the process timer
        self._timer = Timer()
        self._timer.start()

        self.command = args
        self.stdin = kwargs.pop('stdin', None)
        if self.stdin is not None:
            # Translate a newline submitted as '\n' on the CLI to an actual newline character
            self.stdin = self.stdin.replace('\\n', '\n')
            kwargs['stdin'] = subprocess.PIPE
        self.with_communicate = kwargs.pop('with_communicate', True)
        self.process = subprocess.Popen(args, **kwargs)

    def wait(self, timeout=None):
        """
        wait for subprocess to terminate and return subprocess' return code
        If timeout is reached, throw TimedProcTimeoutError
        :param timeout:
        :return:
        """

        def receive():
            if self.with_communicate:
                com_in = self.stdin if self.stdin is None else input(self.stdin)
                self.stdout, self.stderr = map(lambda b: to_str(b), self.process.communicate(com_in))
            else:
                self.process.wait()
                (self.stdout, self.stderr) = (None, None)

        def stoptime():
            self._timer.stop()
            self.time_elapsed = self._timer.elapsed

        if timeout is not None:
            if not isinstance(timeout, (int, float)):
                raise TimedProcTimeoutError('Error: timeout must be a number')

            rt = threading.Thread(target=receive)
            rt.start()
            rt.join(timeout)
            if rt.isAlive():
                # Subprocess cleanup (best effort)
                self.process.kill()

                def terminate():
                    if rt.isAlive():
                        self.process.terminate()

                threading.Timer(0, terminate).start()
                stoptime()
                raise TimedProcTimeoutError(
                    '{0} : Timed out after {1} seconds'.format(
                        self.command,
                        str(timeout)
                    )
                )
        else:
            receive()
        stoptime()

        return self.process.returncode
