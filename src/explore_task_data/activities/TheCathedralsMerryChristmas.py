stage_data = {
    "challenge2_sss": {
        "start": [
            ["pierce1", (525, 298)],
            ["burst1", (822, 308)]
        ],
        "action": [
            {"t": "click", "p": [647, 328], "ec": True, "desc": "1 upper right"},
            {"t": "click", "p": [710, 477], "ec": True, "wait-over": True, "desc": "2 lower right"},

            {"t": "click", "p": [444, 444], "ec": True, "desc": "1 lower left"},
            {"t": "click", "p": [690, 522], "ec": True, "wait-over": True, "desc": "2 lower left"},

            {"t": "click", "p": [555, 499], "ec": True, "desc": "1 lower right"},
            {"t": "choose_and_change", "p": [555, 499], "desc": "swap 1 2"},
            {"t": "click", "p": [502, 572], "ec": True, "wait-over": True, "desc": "2 lower left"},

            {"t": "click", "p": [647, 416], "ec": True, "desc": "1 upper right"},
            {"t": "click", "p": [417, 473], "desc": "2 left"}
        ]
    },

    "challenge2_task": {
        "start": [
            ["burst1", [702, 226]]
        ],
        "action": [
            {"t": "click", "p": [745, 340], "wait-over": True, "desc": "lower right"},
            {"t": "click", "p": [486, 454], "wait-over": True, "desc": "lower left"},
            {"t": "click", "p": [420, 477], "wait-over": True, "desc": "left"},
            {"t": "click", "p": [470, 547], "wait-over": True, "desc": "lower left"},
            {"t": "click", "p": [440, 487], "desc": "left"}
        ]
    },

    "challenge4_sss": {
        "start": [
            ["burst1", [370, 517]],
            ["pierce1", [648, 115]],
            ["burst2", [938, 347]]
        ],
        "action": [
            {"t": "click", "p": (437, 487), "ec": True, "desc": "1 left"},
            {"t": "click", "p": (397, 328), "ec": True, "desc": "2 left"},
            {"t": "click", "p": (841, 332), "ec": True, "wait-over": True, "desc": "3 upper right"},

            {"t": "click", "p": [492, 401], "ec": True, "desc": "1 upper left"},
            {"t": "click_and_teleport", "p": [602, 192], "ec": True, "desc": "2 upper left teleport"},
            {"t": "click_and_teleport", "p": [598, 192], "ec": True, "wait-over": True, "desc": "3 upper left teleport"},

            {"t": "click_and_teleport", "p": [555, 489], "wait-over": True, "desc": "1 teleport"},
            {"t": "click", "p": [705, 237], "ec": True, "desc": "1 right"},
            {"t": "click", "p": [847, 487], "ec": True, "desc": "2 lower right"},
            {"t": "choose_and_change", "p": [882, 444], "desc": "swap 2 3"},
            {"t": "click", "p": [903, 417], "ec": True, "wait-over": True, "desc": "3 right"},

            {"t": ["exchange", "click_and_teleport"], "p": [755, 457], "wait-over": True, "desc": "2 teleport"},
            {"t": "click", "p": [582, 149], "ec": True, "desc": "2 upper left"},
            {"t": "click", "p": [615, 418], "ec": True, "desc": "1 right"},
            {"t": "click_and_teleport", "p": [767, 444], "wait-over": True, "desc": "3 teleport"},
            {"t": "click", "p": [587, 503], "ec": True, "wait-over": True, "desc": "3 lower right"},

            {"t": "exchange_twice_and_click", "p": [557, 507], "ec": True, "wait-over": True, "desc": "3 left"},
            {"t": "exchange_and_click", "p": [650, 362], "ec": True, "desc": "2 left"},
            {"t": "choose_and_change", "p": [650, 362], "desc": "swap 1 2"},
            {"t": "click", "p": [592, 447], "desc": "1 lower left"}
        ]
    },
    "challenge4_task": {
        "start": [
            ["burst1", [370, 519]],
            ["burst2", [938, 196]]
        ],
        "action": [
            {"t": "click", "p": [405, 458], "ec": True, "desc": "1 left"},
            {"t": "end-turn", "p": []},

            {"t": "click_and_teleport", "p": [456, 365], "ec": True, "wait-over": True, "desc": "1 upper left teleport"},
            {"t": "end-turn", "p": []},

            {"t": "click", "p": [561, 269], "ec": True, "desc": "1 upper right"},
            {"t": "end-turn", "p": []},

            {"t": "click_and_teleport", "p": [512, 330], "wait-over": True, "desc": "1 teleport"},
            {"t": "click", "p": [831, 484], "ec": True, "desc": "1 lower right"},
            {"t": "end-turn", "p": []},

            {"t": "click_and_teleport", "p": [782, 406], "ec": True, "wait-over": True, "desc": "1 right teleport"},
            {"t": "end-turn", "p": []},

            {"t": "click", "p": [506, 574], "ec": True, "desc": "1 lower left"},
            {"t": "click", "p": [572, 281], "ec": True, "wait-over": True, "desc": "2 left"},

            {"t": "exchange_and_click", "p": [565, 358], "ec": True, "desc": "2 lower left"},
            {"t": "end-turn", "p": []}
        ]
    }

}