#!/usr/bin/env python3
import shutil
import os

#move into working directory
os.chdir("/home/student/mycode/")

#copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")
