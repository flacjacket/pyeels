# System imports
import os, tempfile
from PyEELS.external.numpy import np

def load_file(file_path):
    file_path = os.path.expandvars(file_path)
    file_path = os.path.expanduser(file_path)
    file_path = os.path.normpath(file_path)

    if not os.path.exists(file_path):
        return

    clean = _clean_file(file_path)
    data = _extract_data(file_path)
    return data, file_path

def _clean_file(file_path):
    dir_name, file_name = os.path.split(file_path)
    file_root, file_ext = os.path.splitext(file_name)
    file_name_new = file_root + " clean" + file_ext

    os.chdir(dir_name)

    with open(file_name, 'rb') as fi:
        data = fi.read()
    with open(file_name_new, 'wb') as fo:
        fo.write(data.replace('\x00', ''))

    return file_name_new

def _extract_data(file_path):
    print np
    print np.loadtxt
    return np.loadtxt(file, delimiter=' ', skiprows=2, usecols=(2,3))
