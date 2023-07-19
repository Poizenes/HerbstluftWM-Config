import os

def call(command):
    os.system("herbstclient " + command)

def configure(command, configuration):
    for key, value in configuration.items():
        call(f"{command} {key} {value}")
