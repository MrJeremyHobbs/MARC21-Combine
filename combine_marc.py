#!/bin/usr/python3
import glob
import shutil

# get list of all MRC files in Downloads folder
files = glob.glob("c:\\users\\jthobbs\\downloads\\*.mrc")

# generate combined MARC file
with open('c:\\users\\jthobbs\\Desktop\\KANOPY_RECORDS.mrc','wb') as wfd:
    for f in files:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd, 1024*1024*10)
            #10MB per writing chunk to avoid reading big file into memory.
            
# finish
print("Done.")