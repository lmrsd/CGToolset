import sys
import imp

mod_root = r"D:\01_PROD\_DEV"

if not mod_root in sys.path:
    sys.path.append(mod_root)

import VfxToolset
import VfxToolset.UtilsTD

from VfxToolset.CLarisseTD.tools import incrementer_clarisse as saver


imp.reload(VfxToolset)
imp.reload(saver)

fup = saver.Clarisse_Incrementer()
fup.save_up()
