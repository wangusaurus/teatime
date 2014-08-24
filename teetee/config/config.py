import yaml

from os import path
from UserDict import UserDict

from teetee import root


class TeeTeeConfig(UserDict):
    _default_file_location = 'etc/teetee.yml'

    @classmethod
    def from_string(cls, config_str):
        return cls(yaml.load(config_str))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            loaded = f.read().decode('utf-8')
        return cls.from_string(loaded)

    @classmethod
    def from_default_file(cls):
        config_path = path.join(root, cls._default_file_location)
        return cls.from_file(config_path)
