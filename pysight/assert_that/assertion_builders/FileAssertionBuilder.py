class FileAssertionBuilder(object):
    def __init__(self, val, description):
        self.val = val
        self.description = description

    def is_file(self):
        raise NotImplementedError

    def exists(self):
        raise NotImplementedError

    def is_directory(self):
        raise NotImplementedError

    def is_block_device(self):
        raise NotImplementedError

    def is_character_device(self):
        raise NotImplementedError

    def is_pipe(self):
        raise NotImplementedError

    def is_socket(self):
        raise NotImplementedError

    def is_symlink(self):
        raise NotImplementedError

    def contain(self):
        raise NotImplementedError

    def is_mode(self):
        raise NotImplementedError

    def is_owned_by(self):
        raise NotImplementedError

    def is_grouped_by(self):
        raise NotImplementedError

    def is_linked_to(self):
        raise NotImplementedError

    def is_readable(self):
        raise NotImplementedError

    def is_writable(self):
        raise NotImplementedError

    def is_executable(self):
        raise NotImplementedError

    def is_immutable(self):
        raise NotImplementedError

    def is_mounted(self):
        raise NotImplementedError

    def is_version(self):
        raise NotImplementedError

    def has_md5sum(self):
        raise NotImplementedError

    def has_sha256sum(self):
        raise NotImplementedError

    def has_selinux_label(self):
        raise NotImplementedError

    def has_size_of(self):
        raise NotImplementedError
