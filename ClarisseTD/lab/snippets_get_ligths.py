### PROTOTYPE ##light exporter
import json
import os


import ix


file_path = r"D:\01_PROD\_DEV\VfxToolset\CLarisseTD\lab\210_VDC_1000-lgt-main-v001.lux"

lgtt_data ={}



# final part serialized json
lgt_object = json.dumps(lgtt_data, indent=4)

# Writing to sample.json
with open(file_path, "w") as outfile:
    outfile.write(lgt_object)


