import sys

try:
    import py2exe
except:
    raw_input('Please install py2exe first...')
    sys.exit(-1)
from distutils.core import setup
sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {'bundle_files': 1, 'compressed': True,
                   'includes': ["io", "os", "socket", "struct", "sys", "code", "platform", "getpass", "shutil", "subprocess"]
                   }
    },
    windows=[
    {
            "script": "shellcode.py",                    ### Main Python script    
            # "icon_resources": [(0, "app.ico")]     ### Icon to embed into the PE file.
        }
    ],
    zipfile=None,
    #service=[myservice]
)