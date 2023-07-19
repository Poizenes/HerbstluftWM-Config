#!/usr/bin/env python3

import herbstclient as hc
import config

hc.call('keyunbind --all')
hc.configure('keybind', config.keybinds)
hc.add_tags(config.tags, config.kb_tag_use, config.kb_tag_move)
