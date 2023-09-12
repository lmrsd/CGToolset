import sys
import os
import json
import logging

mod_roots = [r"/mnt/prod/lbp/tmp/lmarsaud/00_DEV", r"D:\DEV\PROD", r"D:\01_PROD\_DEV"]

for root in mod_roots :
    if os.path.exists(root):
        mod_root = root


if not mod_root in sys.path:
    sys.path.append(mod_root)


from VfxToolset.vendor.Qt import QtCore, QtWidgets, QtGui, QtCompat
from VfxToolset.vendor import pyperclip
from VfxToolset.UtilsTD.tools.shared_clipboard import SharedClipboard

import PySide2

import ix
import pyqt_clarisse

class Clarisse_sharedClipboard(SharedClipboard):
    def __init__(self,parent):
        super(Clarisse_sharedClipboard, self).__init__()
        self.log.setLevel(logging.ERROR)

    def call_paste_shared_clipboard(self):

        paste_path = os.path.join(self.paste_dir, self.paste_file_name)

        with open(paste_path, 'r') as open_clip:
            # Reading from json file
            paste_json = json.load(open_clip)

        paste_data = paste_json['clipboard']

        ix.application.set_clipboard(str(paste_data))

        print(paste_data)

        QtWidgets.QApplication.clipboard().setText(paste_data)
        ix.api.SdkHelpers.paste(ix.application)
        ix.api.SdkHelpers.paste(ix.application)

        # Gui_paste_from_selection_buffer
        # SdkHelpers_paste




if __name__ == '__main__':

    _app = None

    if not QtWidgets.QApplication.instance():
        # NOTE: tell Windows platform plugin to leave DPI settings alone, otherwise if we have scaling enabled
        # in Windows' settings, Qt will overwrite them, and Clarisse will be resized. See https://doc.qt.io/qt-5/highdpi.html
        # Windoà
        # _app = QtWidgets.QApplication(["Clarisse", "-platform", "windows:dpiawareness=0"])
        _app = QtWidgets.QApplication(["Clarisse"])
    else:
        _app = QtWidgets.QApplication.instance()

    # make sure it was successfully created
    assert _app is not None, "Failed creating a QApplication instance."

    tool = Clarisse_sharedClipboard(_app)
    tool.show()

    # instead of calling app.exec_() like you would do normally in PyQt,
    # you call pyqt_clarisse.exec_(app).
    pyqt_clarisse.exec_(_app)



