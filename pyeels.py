#!/usr/bin/env python

import os, sys

def main():
    this_dir = os.path.dirname(sys.argv[0])
    sys.path.insert(0, this_dir)

    execfile(os.path.join(this_dir, 'PyEELS', 'scripts', 'pyeels'))

if __name__ == "__main__":
    main()
