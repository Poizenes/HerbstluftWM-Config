import os

def call(command):
    return os.system('herbstclient ' + command)

def configure(command, configuration):
    for key, value in configuration.items():
        call(f'{command} {key} {value}')

def set_tags(tags, use_key, move_key):
    default_tag = list(tags.keys())[0]
    call(f'rename default {default_tag}')
    for tag, key in tags.items():
        call(f'add {tag}')
        call(f'keybind {use_key}{key} use {tag}')
        call(f'keybind {move_key}{key} move {tag}')
