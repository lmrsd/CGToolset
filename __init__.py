import os
import json

class Studio():
    def __init__(self, studio_name, mod_root):
        print("Initialize Studio : {}".format(studio_name))

        self.studio_name = studio_name
        self.root = mod_root

        self.c_path = os.path.join(mod_root, 'CGToolset', 'config', '{}.json'.format(studio_name) )

        if os.path.exists(self.c_path):
            with open(self.c_path, 'r') as f:
                self.config = json.load(f)