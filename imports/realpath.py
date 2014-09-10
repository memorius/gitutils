#!/usr/bin/env python

# Substitute for gnu 'readlink -f' to work on MacOS
# See http://stackoverflow.com/questions/1055671/how-can-i-get-the-behavior-of-gnus-readlink-f-on-a-mac

import os,sys
print os.path.realpath(sys.argv[1])
