import os
import logging

# Try import PyAml if not installed
try :
    import yaml
except :
    import VfxToolset.vendor.yaml
    logging.info("VfxToolSet : yaml module imported")


# Try import Qt.py if not existting
try :
    import Qt
except :
    import VfxToolset.vendor.Qt
    logging.info("VfxToolSet : Qt  module imported")

