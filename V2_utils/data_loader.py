# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:29:00 2019

@author: wpineda
"""
import os
import re
import arcpy
date = "201812"
regexp = "({})+([a-zA-Z0-9\s_\\.\-\(\):])+(.tif|.tiff)".format(date)
in_dir=r'C:\Users\WPINEDA\Documents\Python Scripts\drafts\Downloads'
dir_files = os.listdir(in_dir)
files = [elem for elem in dir_files if re.search(regexp, elem) is not None]
aprx = arcpy.mp.ArcGISProject("CURRENT")
mp = aprx.listMaps()[0]
print(files) 
for file in files:
    mp.addDataFromPath(os.path.join(in_dir, file))