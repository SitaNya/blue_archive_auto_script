stage_data = {
    '7-1-sss-present': {
        'start': {
            'burst1': (820, 387),
            'burst2': (780, 563),
        },
        'action': [
            {'t': 'click', 'p': (653, 227), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (572, 494), 'wait-over': True, 'ec': True, "desc": "2 left"},

            {'t': 'click', 'p': (557, 289), 'ec': True, "desc": "1 left"},
            {'t': 'click_and_teleport', 'p': (503, 504), 'wait-over': True, 'ec': True, "desc": "2 left and tp"},

            {'t': 'choose_and_change', 'p': (668, 335), "desc": "swap 1 2"},
            {'t': 'click_and_teleport', 'p': (667, 355), "desc": "1 choose self and tp"},
            {'t': 'click', 'p': (527, 364), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (525, 268), 'ec': True, 'wait-over': True, "desc": "2 left"},

            {'t': 'click', 'p': (486, 388), "desc": "1 upper left"},
        ]
    },
    '7-1-task': {
        'start': {
            'burst1': (820, 387),
        },
        'action': [
            {'t': 'click_and_teleport', 'wait-over': True, 'p': (658, 387), "desc": "1 left and tp"},
            {'t': 'click', 'p': (553, 335), 'wait-over': True, "desc": "upper left"},
            {'t': 'click', 'p': (473, 274), "desc": "upper left"},
        ]
    },
    '7-2-sss-present': {
        'start': {
            'burst1': (469, 229),
            'burst2': (650, 296),
        },
        'action': [
            {'t': 'click', 'p': (583, 474), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (760, 394), 'ec': True, 'wait-over': True, "desc": "2 right"},
            {'t': 'click_and_teleport', 'ec': True, 'p': (523, 560), "desc": "1 lower left and tp"},
            {'t': 'click', 'p': (758, 365), 'wait-over': True, "desc": "2 lower right"},
            {'t': 'click', 'p': (737, 411), "desc": "1 upper right"},
            {'t': 'end-turn'},
        ]
    },
    '7-2-task': {
        'start': {
            'burst1': (469, 229),
            'burst2': (650, 296),
        },
        'action': [
            {'t': 'exchange_and_click', 'p': (578, 473), 'ec': True, "desc": "2 lower left"},
            {'t': 'choose_and_change', 'p': (578, 473), "desc": "swap 1 2"},
            {'t': 'click_and_teleport', 'p': (520, 560), 'wait-over': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (716, 378), "desc": "1 upper right"},
            {'t': 'end-turn'},
        ]
    },
    '7-3-sss-present-task': {
        'start': {
            'burst1': (943, 471),
            'burst2': (182, 260),
        },
        'action': [
            {'t': 'click', 'p': (659, 433), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (626, 350), 'wait-over': True, 'ec': True, "desc": "2 right"},
            {'t': 'click_and_teleport', 'ec': True, 'p': (667, 384), "desc": "1 left and tp"},
            {'t': 'click_and_teleport', 'ec': True, 'wait-over': True, 'p': (596, 382), "desc": "2 lower right and tp"},
            {'t': 'exchange_and_click', 'p': (451, 494), "wait-over": True, "desc": "2 left"},
            {'t': 'click', 'p': (841, 294), "desc": "1 right"},
        ]
    },
}
