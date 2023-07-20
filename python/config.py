mod = 'Super'

keybinds = {
        # Main
        f'{mod}-Shift-q': 'quit',
        f'{mod}-Shift-r': 'reload',
        f'{mod}-Shift-c': 'close',
        f'{mod}-Return': 'spawn alacritty',
        f'{mod}-d': 'spawn rofi -show drun',

        # Layout
        f'{mod}-r': 'remove',
        f'{mod}-u': 'split vertical 0.5',
        f'{mod}-o': 'split horizontal 0.5',
        f'{mod}-s': 'floating toggle',
        f'{mod}-f': 'fullscreen toggle',

        # Focus
        f'{mod}-Left':  'focus left',
        f'{mod}-Right': 'focus right',
        f'{mod}-Up':    'focus up',
        f'{mod}-Down':  'focus down',
        f'{mod}-Shift-Left':   'shift left',
        f'{mod}-Shift-Right':  'shift right',
        f'{mod}-Shift-Up':     'shift up',
        f'{mod}-Shift-Down':   'shift down',
        }

# Tag keybindings
kb_tag_use = f'{mod}-'
kb_tag_move = f'{mod}-Shift-'

tags = {
        'main': '1',
        'term': '2',
        'discord': '0',
        }
