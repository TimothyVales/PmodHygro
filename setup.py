from setuptools import setup
import os
import shutil
import sys

#get effective user ID of current process
#if ID doesnt equal 0, exit
if os.geteuid() != 0:
    print("This command must be run as root. Aborting.")
    sys.exit(1)

#mapping object represents string environment 
#checks if board is PynqZ2, if not exit
if os.environ['BOARD'] != 'Pynq-Z2':
    print("Only supported on a Pynq-Z2 Board")
    exit(1)

#Setup information
setup(
	name = "PmodHygro",
	version = 1.0,
	url = 'https://github.com/TimothyVales/PmodHygro.git',
	license = 'BSD 3-Clause License',
	author = "Timothy Vales",
	author_email = "timothyv@xilinx.com",

	include_package_data = True,
	packages = ['PmodHygro'],
	package_data = {
	'' : ['*.bit','*.tcl','*.py','*.bin','*.txt', '*.cpp', '*.h', '*.sh'],
	},
	description = "Pynq Z2 board and Pmod Hygro",
    install_requires=[
        'pynq', 'matplotlib'
    ],
)

#working directory (Host COmputer)
WORK_DIR = os.path.dirname(os.path.realpath(__file__))

#shutil is a lib for working with files or collection of files
#copy2 copies file from first arg to second arg AND preserves metadata
#takes files from working directory and copies it target dir
shutil.copy2(WORK_DIR + "/PmodHygro.ipynb","/PmodHygro")

#if there exists a file called "PmodHygro" already in the Pynq Jupyter Notebook dir, delete it and redownload it 
if 'install' in sys.argv:
    if os.path.isdir(os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/PmodHygro/"):
        shutil.rmtree(os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/PmodHygro/")
    shutil.copytree(WORK_DIR + "/PmodHygro.ipynb/",os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/PmodHygro/")