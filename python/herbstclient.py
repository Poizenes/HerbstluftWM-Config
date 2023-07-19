import os

def call(command):
    return os.system('herbstclient ' + command)

def configure(command, configuration):
    for key, value in configuration.items():
        call(f'{command} {key} {value}')

def add_tags(tags, use_key, move_key):
    for tag, key in tags.items():
        call(f'add {tag}')
        call(f'keybind {use_key}{key} use {tag}')
        call(f'keybind {move_key}{key} move {tag}')
