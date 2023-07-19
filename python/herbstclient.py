import os

def call(command):
    os.system("herbstclient " + command)

def quit():
    call("quit")

def reload():
    call("reload")

def keybind(key, command):
    call(f"keybind {key} {command}")

def keyunbind(key):
    call("keyunbind " + key)

def bind_keys(keybinds):
    for key, command in keybinds.items():
        keybind(key, command)
