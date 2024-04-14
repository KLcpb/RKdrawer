from source import drawer

##CREATE FOLDERS AUTOMATICALLY
PATH = './log2.txt'
SETTING_PATH = './config.txt'
OUTPUT_FOLDER = './OUTPUT'
Drawer = drawer(OUTPUT_FOLDER)
params = Drawer.load_params(SETTING_PATH)
print(f'loaded settings from {SETTING_PATH}')
print(params)
Drawer.load_file(PATH)
print(f'loaded file from {PATH}')
Drawer.process_raw()



