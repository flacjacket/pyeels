# Local imports
from PyEELS.utils.data_files import load_file
class DataSet(object):
    def __init__(self):
        self._data = {}

    def load_data(self, file_name):
        data, name = load_file(file_name)
        self._data[name] = data
        return name

    def get_data(self, name=None):
        if name in self._data:
            return self._data[name]
