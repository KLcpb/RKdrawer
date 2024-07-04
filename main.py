from source import drawer
import os

##CREATE FOLDERS AUTOMATICALLY
PATH = './telem.TXT'
SETTING_PATH = './config.txt'
OUTPUT_FOLDER = './OUTPUT'

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


Drawer = drawer(OUTPUT_FOLDER)
params = Drawer.load_params()
print(f'loaded settings from {SETTING_PATH}')
print(params)
val = Drawer.load_file()
print(f'found {val} strs')
print(f'loaded file from {PATH}')
Drawer.process_raw()



