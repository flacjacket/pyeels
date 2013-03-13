# System imports
import os, tempfile
from PyEELS.external.np import np

def load_file(file_path):
    file_path = os.path.expandvars(file_path)
    file_path = os.path.expanduser(file_path)
    file_path = os.path.normpath(file_path)

    if not os.path.exists(file_path):
        return

    data = _read_file(file_path)
    array = _extract_array(data)
    return array, os.path.basename(file_path)

def _read_file(file_path):
    dir_name, file_name = os.path.split(file_path)
    file_root, file_ext = os.path.splitext(file_name)
    file_name_new = file_root + " clean" + file_ext

    os.chdir(dir_name)

    with open(file_name, 'rb') as fi:
        data = fi.read().replace('\x00', '')
    return data

def _extract_array(data):
    import StringIO
    return np.loadtxt(StringIO.StringIO(data), delimiter=' ', skiprows=2, usecols=(2,3))
