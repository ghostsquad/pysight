class UserAssertionBuilder(object):
    def __init__(self, val, description):
        self.val = val
        self.description = description

    def exists(self):
        raise NotImplementedError

    def belongs_to_group(self):
        raise NotImplementedError

    def belongs_to_primary_group(self):
        raise NotImplementedError

    def has_uid(self):
        raise NotImplementedError

    def has_home_directory(self):
        raise NotImplementedError

    def has_login_shell(self):
        raise NotImplementedError

    def has_authorized_key(self):
        raise NotImplementedError

    def has_encrypted_password(self):
        raise NotImplementedError

    def has_no_password(self):
        raise NotImplementedError

    def has_min_days_between_password_change(self):
        raise NotImplementedError

    def has_max_days_between_password_change(self):
        raise NotImplementedError
