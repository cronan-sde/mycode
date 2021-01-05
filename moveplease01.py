#!/usr/bin/env python3
import shutil
import os

#get working directory
os.chdir("/home/student/mycode/")

#move file to directory
shutil.move("raynor.obj", "ceph_storage/")

#prompt user for name of new file
xname = input("What is the new name for kerrigan.obj? ").strip()

#rename kerrigan.obj file to user input
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)
