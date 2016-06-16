class PackageAssertionBuilder(object):
    def __init__(self, val, description):
        self.val = val
        self.description = description

    def is_installed(self):
        raise NotImplementedError

    def is_not_installed(self):
        raise NotImplementedError
