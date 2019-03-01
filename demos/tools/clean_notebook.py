#!/usr/bin/env python
# coding: utf-8

# In[31]:


from shutil import copyfile

copyfile("DataScienceMeetsSoftwareData.css", "DataScienceMeetsSoftwareData_empty.css")

import json

json_data = ""
with open("DataScienceMeetsSoftwareData.ipynb", encoding='utf-8', mode='r') as f:
    json_data = json.load(f)

cells = json_data['cells']

for cell in cells:
    metadata = cell['metadata']
    if "tags" in metadata.keys() and "delete" in metadata['tags']:
        cell['source'] = []
        cell['outputs'] = []
        
with open('DataScienceMeetsSoftwareData_empty.ipynb', encoding='utf-8', mode='w') as outfile:
    json.dump(json_data, outfile, indent=4)

