class GroupAssertionBuilder(object):
    def __init__(self, val, description):
        self.val = val
        self.description = description

    def exists(self):
        raise NotImplementedError

    def has_gid(self):
        raise NotImplementedError
