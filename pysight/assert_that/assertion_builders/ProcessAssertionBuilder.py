class ProcessAssertionBuilder(object):
    def __init__(self, val, description):
        self.val = val
        self.description = description

    def has_count(self):
        raise NotImplementedError

    def is_running(self):
        raise NotImplementedError
