import pythonmonkey as pm
from glob import iglob
import subprocess
import shutil
import glob
import os

def formatFile(path):
    formatter = pm.require('./formatter')
    f = open(path, "r", encoding='utf-8-sig')
    content = formatter.stringify(f.read(), {"maxLength": 200})
    f.close()
    f = open(path, "w", encoding='utf-8-sig')
    f.write(content)
    f.close()
    
def formatFolder(folder):
    rootdir_glob = f'assets/nightvisiondeviceswitch/{folder}/**/*.json'
    file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]
    for f in file_list:
        print(f'Formatting: {f}')
        formatFile(f)

os.chdir(r'../')

formatFolder("blocktypes")
formatFolder("entities")
formatFolder("itemtypes")
formatFolder("patches")

try:
    os.remove('nightvisiondeviceswitch.zip')
except OSError as e:
    pass

shutil.copytree('assets', 'temp/assets')
shutil.copy('modicon.png', 'temp')
shutil.copy('modinfo.json', 'temp')
shutil.make_archive('nightvisiondeviceswitch', 'zip', 'temp')
shutil.rmtree('temp')

os.chdir(r'scripts')