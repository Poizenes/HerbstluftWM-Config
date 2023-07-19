#!/usr/bin/env python3

import herbstclient as hc

keybinds = {
        'Mod4-Return': 'spawn alacritty',
        'Mod4-d': 'spawn rofi -show drun',
        }

hc.bind_keys(keybinds)
