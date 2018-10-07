from os import environ as os_environ

class Env(object):
    def parse_key(self, key):
        return str(key)

    def __setitem__(self, key, val):
        if (key is Ellipsis):
            raise KeyError("Cannot set Ellipsis")
        key = self.parse_key(key)
        os_environ[key] = val

    def __getitem__(self, key):
        if (key is Ellipsis):
            return self
        key = self.parse_key(key)
        return os_environ[key]

    def __delitem__(self, key):
        if (key is Ellipsis):
            raise KeyError("Cannot delete Ellipsis")
        key = self.parse_key(key)
        del os_environ[key]

    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default

    def __iter__(self):
        yield from set(os_environ)

    def __contains__(self, key):
        if (key is Ellipsis):
            return False
        key = self.parse_key(key)
        return key in os_environ

    def __len__(self):
        return len(os_environ)

    def __str__(self):
        return str(os_environ)

    def __repr__(self):
        return "{0}.{1}(...)".format(
            self.__class__.__module__, self.__class__.__name__, os_environ
        )
