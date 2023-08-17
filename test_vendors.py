#### RUN THIS CODE IN CLEAN PYTHON INSTALL #####

import sys
import os

root_package = os.getcwd()

if not root_package in sys.path:

    sys.path.append(root_package)

import vendor


from vendor import yaml

test_file = os.path.join(root_package, 'config', 'test.yaml')

with open(test_file) as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

try :
    from vendor import Qt

except :
    print('If no binding installed Qt.py raise and error please install one Qt binding, '
          'PySide2 or PySide6, PyQt4 or PyQt5, etc...')