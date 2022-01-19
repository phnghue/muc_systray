
APP_NAME    = "Muc Systray";      ## < Your App's name
Python_File = "muc_systray.py";     ## < Main Python file to run
Icon_Path   = "./muc_s.ico"; ## < Icon
UseFile     = ["muc_l.ico","muc_m.ico","muc_s.ico"];
Import      = ["infi","time","webbrowser"];  ## < Your Imported modules (cv2,numpy,PIL,...)

Import+=["pkg_resources","xml","email","urllib","ctypes"]
################################### CX_FREEZE IGNITER ###################################
import sys, pkgutil;
from cx_Freeze import setup, Executable;

BasicPackages=["collections","encodings","importlib"] + Import;
def AllPackage(): return [i.name for i in list(pkgutil.iter_modules()) if i.ispkg]; # Return name of all package
#Z=AllPackage();Z.sort();print(Z);
#while True:pass;
def notFound(A,v): # Check if v outside A
    try: A.index(v); return False;
    except: return True;
build_exe_options = {
    "includes": BasicPackages,
    "excludes": [i for i in AllPackage() if notFound(BasicPackages,i)],
    "include_files":UseFile
}
setup(  name = APP_NAME,
        options = {"build_exe": build_exe_options},
        executables = [Executable(
            Python_File,
            base='Win32GUI',#Win64GUI
            icon=Icon_Path,
            targetName=APP_NAME,
            copyright="Copyright (C) 3000AD Muc",
            )]
);
  

    
    
#setup(version = "1.1",description = "help tool.");

    
'''
    
from cx_Freeze import setup, Executable
import subprocess
import sys


NAME = 'EXE NAME'
VERSION = '1.0'
PACKAGES = ['pygame', ('import_name', 'package_name')]
# if names are same just have a string not a tuple
installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
installed_packages = installed_packages.split('\r\n')
EXCLUDES = {pkg.split('==')[0] for pkg in installed_packages if pkg != ''}
EXCLUDES.add('tkinter')
for pkg in PACKAGES:
    if type(pkg) == str: EXCLUDES.remove(pkg)
    else: EXCLUDES.remove(pkg[1])


executables = [Executable('main.py', base='Win32GUI', icon='Resources/Jungle Climb Icon.ico', targetName=NAME)]

setup(
    name=NAME,
    version=VERSION,
    description=f'{NAME} Copyright 2019 AUTHOR',
    options={'build_exe': {'packages': [pkg for pkg in PACKAGES if type(pkg) == str else pkg[0]],
                           'include_files': ['FOLDER'],
                           'excludes': EXCLUDES,
                           'optimize': 2}},
    executables=executables)
    
'''
    