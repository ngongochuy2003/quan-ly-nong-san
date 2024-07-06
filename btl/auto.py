import os
import time

ui_file = 'home.ui'
py_file = 'home.py'

def convert_ui_to_py(ui_file, py_file):
    command = f'pyuic6 -x {ui_file} -o {py_file}'
    os.system(command)

def watch_file(file_path, callback):
    last_modified = os.path.getmtime(file_path)
    while True:
        time.sleep(1)  # delay between each check
        modified = os.path.getmtime(file_path)
        if modified != last_modified:
            last_modified = modified
            callback()

watch_file(ui_file, lambda: convert_ui_to_py(ui_file, py_file))