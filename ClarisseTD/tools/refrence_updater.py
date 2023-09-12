import sys
import os
import importlib
from functools import partial


# TODO: update selected only if not last : store data is latest
# TODO: asset non valid , what happens
# TODO : Strange color for strange paths
# TODO : filter only not updated
# TODO : Add version only if file exists

unpiped = 'UnPiped'

mod_roots = [r"/mnt/prod/lbp/tmp/lmarsaud/00_DEV", r"D:\DEV\PROD", r"D:\01_PROD\_DEV"]

for root in mod_roots :
    if os.path.exists(root):
        mod_root = root


if not mod_root in sys.path:
    sys.path.append(mod_root)


from VfxToolset.vendor.Qt import QtCore, QtWidgets, QtGui, QtCompat


import PySide2

import ix
import pyqt_clarisse



from VfxToolset.UtilsTD.lib.dataio import io
from VfxToolset.UtilsTD.lib.logger import log

from VfxToolset.UtilsTD.lib.gui import tools as guitools
from VfxToolset.UtilsTD.lib.paths import path as pth

from VfxToolset.ClarisseTD.lib.context import context


importlib.reload(guitools)
importlib.reload(context)
importlib.reload(pth)


job_green = QtGui.QColor(25,58,29)
job_greener = QtGui.QColor(81,167,40)
job_blue = QtGui.QColor(7,104,152)
job_red = QtGui.QColor(47,27,29)

__file__ = os.path.join(mod_root,r"VfxToolset/ClarisseTD/tools/refrence_updater.py")

class update_referencer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Init Main Layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.ui = guitools.load_ui_in_layout( self.main_layout, guitools.get_ui_file_path(__file__) )
        self.setLayout(self.main_layout)

        #
        self.log = log.simple_log('Version updater Tool')

        # globals of tools
        self.name_list = []

        # Start Tool Routine
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        #self.log.info("Init conformAbcCam ui...")

        root = os.path.join(mod_root,"VfxToolset")
        
        guitools.load_global_css(self)


        guitools.load_icons(self.ui)
        guitools.load_custom_widget_icon(root, self.ui)

        self.resize(1001,516)

        self.ini_table()
        self.ui.pgbar_process.setVisible(False)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def setup_connections(self):
        self.ui.tbtn_updateSelected.clicked.connect(self.process_ref)
        self.ui.cbx_all.stateChanged.connect(self.set_check_state_all)
        self.ui.tbtn_refresh.clicked.connect(self.refresh_table)
        self.ui.lne_search.textChanged.connect(self.filter_name)

    def get_versions_lists(self,filepath):
        file_name = os.path.basename(filepath)
        file_root = os.path.dirname(filepath)
        file_root_name = os.path.basename(file_root)
        file_root_version = os.path.dirname(file_root)

        """print(file_name)
        print(file_root)
        print(file_root_name)
        print(file_root_version)"""

        ver = pth.get_version_folder_list(file_root_version,file_root_name)

        self.current_version = pth.get_file_version(file_name)[0]
        self.version_max = max(ver['version_array'])
        self.version_array = ver['version_array']


        return(self.current_version,self.version_max,self.version_array )
        
    def get_references(self):
        ctx_list = context.get_all_context()
        ctx_ref_list = context.get_refences_context(ctx_list)

        if len(ctx_ref_list) > 0:
            self.tble_data = []

            for ctx in ctx_ref_list:
                ctx_path = ctx
                ctx_name = ctx.get_name()
                ctx_filename = ctx.get_attribute('filename').get_string()
                ctx_id = ctx.get_class_info_id()
                #print(ctx_filename)
                #
                try :
                    versions = self.get_versions_lists(ctx_filename)
                    self.tble_data.append([False, ctx_id, ctx_name, str(ctx_path), ctx_filename, self.version_array, self.version_max, self.current_version])

                except :
                    print(ctx_filename)
                    self.tble_data.append([False, ctx_id, ctx_name, str(ctx_path), ctx_filename, [unpiped], unpiped,unpiped])
                    self.log.warning("{} : Not conform".format(ctx_name))
        else:
            self.log.warning("No Reference Instances founds")

    def set_cell_color(self):
        rows = self.ui.tble_refernces.rowCount()
        cols = self.ui.tble_refernces.columnCount()

        for i in range(rows):
            is_last = self.ui.tble_refernces.cellWidget(i,5).currentText() == self.ui.tble_refernces.item(i,6).text()
            #cur_text = self.ui.tble_refernces.cellWidget(i, 5).currentText()

            for c in range(cols):
                item = (self.ui.tble_refernces.item(i,c))

                if item :
                    if is_last:
                        self.ui.tble_refernces.item(i,c).setBackgroundColor(job_green)

                    else:
                        self.ui.tble_refernces.item(i, c).setBackgroundColor(job_red)


    def set_check_state_all(self):
        state = bool(self.ui.cbx_all.checkState())

        rows = self.ui.tble_refernces.rowCount()
        if rows > 0:
            for r in range(rows):
                self.ui.tble_refernces.cellWidget(r,0).setCheckState(QtCore.Qt.CheckState(state))


    def clear_table(self):
        rows = self.ui.tble_refernces.rowCount()
        cols = self.ui.tble_refernces.columnCount()
        self.ui.tble_refernces.clearContents()
        if rows > 0 :
            for r in range(0,rows) :
                self.ui.tble_refernces.removeRow(r)
                for c in range(0,cols):
                    self.ui.tble_refernces.removeCellWidget(r,c)

    def filter_name(self, filter_text):
        for i in range(self.ui.tble_refernces.rowCount()):
            for j in range(self.ui.tble_refernces.columnCount()):
                item = self.ui.tble_refernces.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.ui.tble_refernces.setRowHidden(i, match)
                    if not match:
                        break

    def init_completers(self):
        ''' inint completer pour le line eidt de recherche'''
        completer_names = QtWidgets.QCompleter(self.name_list)
        completer_names.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lne_search.setCompleter(completer_names)

    def auto_update_version(self,row,state):
        ''' Auto select last version avaiable in qcombobox when state changed'''
        rows = self.ui.tble_refernces.rowCount()
        cell_widget = self.ui.tble_refernces.cellWidget(row, 5)

        if rows > 0:
            AllItems = [cell_widget.itemText(i) for i in range(cell_widget.count())]
            max_version = (max(AllItems))

            #set maximum version avaiable
            cell_widget.setCurrentText(max_version)




    def refresh_table(self):
        ''' refresh the table'''
        self.ui.lne_search.setText('')
        self.clear_table()
        self.ini_table()
        self.set_check_state_all()


    def ini_table(self):
        """ table constructor"""
        # clean_list of name
        self.name_list = list()
        # clean table for refresh
        self.clear_table()


        # get all references in the project context
        self.get_references()

        if len(self.tble_data) > 0:

            # Display
            self.ui.tble_refernces.setSortingEnabled(True)
            self.ui.tble_refernces.setShowGrid(False)
            self.ui.tble_refernces.setAlternatingRowColors(True)
            # Cloumn size
            header = self.ui.tble_refernces.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            #header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


            for r in range(len(self.tble_data)):
                self.ui.tble_refernces.insertRow(r)

                for c in range(len(self.tble_data[r])):

                    #print(self.tble_data[r],self.tble_data[r][c])
                    row = self.tble_data[r]
                    col = self.tble_data[r][c]

                    is_last = self.tble_data[r][7] == self.tble_data[r][6]


                    if isinstance(col,str):
                        text_cell = QtWidgets.QTableWidgetItem()
                        text_cell.setText(col)
                        # making it non editable
                        text_cell.setFlags(QtCore.Qt.ItemIsEnabled)

                        self.ui.tble_refernces.setItem(r, c, text_cell)


                    elif isinstance(col,int):
                        text_cell = QtWidgets.QTableWidgetItem()
                        text_cell.setText(str(col))
                        # making it non editable
                        text_cell.setFlags(QtCore.Qt.ItemIsEnabled)

                        self.ui.tble_refernces.setItem(r, c, text_cell)


                    if isinstance(col,bool):
                        chck_cell = QtWidgets.QCheckBox()
                        chck_cell.setCheckState(QtCore.Qt.CheckState(col))
                        chck_cell.setText("")

                        self.ui.tble_refernces.setCellWidget(r, c, chck_cell)

                        chck_cell.stateChanged.connect(partial(self.auto_update_version,r))


                    elif isinstance(col,list):
                        cbx_cell = QtWidgets.QComboBox()
                        for e in col:
                            cbx_cell.addItem(e)

                        if self.tble_data[r][7] in col:
                            cbx_cell.setCurrentText(self.tble_data[r][7])

                        self.ui.tble_refernces.setCellWidget(r, c, cbx_cell)

                    # force clear checkbox cell text
                    self.ui.tble_refernces.item(r,0).setText("")


                # add name for each row for filter list
                name = self.tble_data[r][2]
                if not name in self.name_list:
                    self.name_list.append(name)

            #init namecompleter for line edit
            self.init_completers()

            self.set_cell_color()

        else:
            self.log.error("No references founded")



    def process_ref(self, rename=True):
        self.ui.pgbar_process.setVisible(True)
        rows = self.ui.tble_refernces.rowCount()
        cols = self.ui.tble_refernces.columnCount()

        p = 0

        for i in range(rows):

            state = bool(self.ui.tble_refernces.cellWidget(i,0).checkState())

            if state:
                sel_version = self.ui.tble_refernces.cellWidget(i,5).currentText()
                filename = self.ui.tble_refernces.item(i,4).text()
                ctx_path = self.ui.tble_refernces.item(i,3).text()

                new_filepath = pth.replace_file_version(filename,sel_version)
                print(new_filepath)

                ref = ix.get_item(ctx_path)

                # Update the reference #
                #change filename
                ref.get_attribute("filename").set_string(new_filepath)

                # reload it
                ref.get_engine().reload()

                """print(rename)
                item_name = self.ui.tble_refernces.item(i, 2).text()
                new_item_name = pth.replace_file_version(item_name,sel_version)
                ix.cmds.RenameItem(ctx_path, new_item_name)"""




            else:
                # else : skip
                self.log.info('Skip {}'.format(self.ui.tble_refernces.item(i,2).text()))


            # Update progress bar
            p+=1
            self.ui.pgbar_process.setValue(p*(100/rows))



        # Hide progress Bar
        #self.ui.pgbar_process.setVisible(False)

        # reset check boxall
        self.ui.cbx_all.setCheckState(QtCore.Qt.CheckState(False))

        # Reset table
        self.ui.lne_search.setText('')
        self.clear_table()
        self.ini_table()



if __name__ == '__main__':

    _app = None

    if not QtWidgets.QApplication.instance():
        # NOTE: tell Windows platform plugin to leave DPI settings alone, otherwise if we have scaling enabled
        # in Windows' settings, Qt will overwrite them, and Clarisse will be resized. See https://doc.qt.io/qt-5/highdpi.html
        # Windoà
        #_app = QtWidgets.QApplication(["Clarisse", "-platform", "windows:dpiawareness=0"])
        _app = QtWidgets.QApplication(["Clarisse"])
    else:
        _app = QtWidgets.QApplication.instance()

    # make sure it was successfully created
    assert _app is not None, "Failed creating a QApplication instance."

    tool = update_referencer()
    tool.show()

    # instead of calling app.exec_() like you would do normally in PyQt,
    # you call pyqt_clarisse.exec_(app).
    pyqt_clarisse.exec_(_app)