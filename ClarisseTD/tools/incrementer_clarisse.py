import sys
import os

mod_roots = [r"/mnt/prod/lbp/tmp/lmarsaud/00_DEV", r"D:\DEV\PROD", r"D:\01_PROD\_DEV"]

for root in mod_roots :
    if os.path.exists(root):
        mod_root = root


if not mod_root in sys.path:
    sys.path.append(mod_root)

from VfxToolset.UtilsTD.tools.incrementer_cdcc import DCC_Incrementer
import ix

class Clarisse_Incrementer(DCC_Incrementer):
    def __init__(self):
        super(Clarisse_Incrementer, self).__init__()
    def get_file_path(self) :
        self.path = ix.application.get_current_project_filename()

    def save_increment_file(self):
        ix.save(self.path)

if __name__ == '__main__':
    saver = Clarisse_Incrementer()
    saver.get_file_path()
    saver.save_up()

