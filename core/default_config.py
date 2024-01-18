EVENT_DEFAULT_CONFIG = """

[
  {
    "enabled": true,
    "priority": 0,
    "interval": 10800,
    "next_tick": 0,
    "event_name": "咖啡厅",
    "func_name": "cafe_reward"
  },
  {
    "enabled": true,
    "priority": 1,
    "interval": 0,
    "next_tick": 0,
    "event_name": "日程",
    "func_name": "lesson"
  },
  {
    "enabled": true,
    "priority": 4,
    "interval": 0,
    "next_tick": 0,
    "event_name": "收集每日体力",
    "func_name": "collect_daily_power"
  },
  {
    "event_name": "收集小组体力",
    "func_name": "group",
    "next_tick": 0,
    "priority": 2,
    "enabled": true,
    "interval": 0
  },
  {
    "enabled": true,
    "priority": 3,
    "interval": 0,
    "next_tick": 0,
    "event_name": "查收邮箱",
    "func_name": "mail"
  },
  {
    "enabled": true,
    "priority": 5,
    "interval": 0,
    "next_tick": 0,
    "event_name": "商店购买",
    "func_name": "common_shop"
  },
  {
    "enabled": true,
    "priority": 6,
    "interval": 0,
    "next_tick": 0,
    "event_name": "竞技场商店购买",
    "func_name": "tactical_challenge_shop"
  },
  {
    "enabled": true,
    "priority": 8,
    "interval": 0,
    "next_tick": 0,
    "event_name": "普通关清体力",
    "func_name": "normal_task"
  },
  {
    "enabled": true,
    "priority": 9,
    "interval": 0,
    "next_tick": 0,
    "event_name": "困难关清体力",
    "func_name": "hard_task"
  },
  {
    "enabled": true,
    "priority": 11,
    "interval": 0,
    "next_tick": 0,
    "event_name": "每日特别委托",
    "func_name": "clear_special_task_power"
  },
  {
    "enabled": true,
    "priority": 7,
    "interval": 0,
    "next_tick": 0,
    "event_name": "悬赏通缉",
    "func_name": "rewarded_task"
  },
  {
    "enabled": true,
    "priority": -1,
    "interval": 0,
    "next_tick": 0,
    "event_name": "竞技场",
    "func_name": "arena"
  },
  {
    "enabled": true,
    "priority": 14,
    "interval": 0,
    "next_tick": 0,
    "event_name": "自动制造",
    "func_name": "create"
  },
  {
    "enabled": true,
    "priority": 15,
    "interval": 0,
    "next_tick": 0,
    "event_name": "总力战",
    "func_name": "total_force_fight"
  },
  {
    "enabled": true,
    "priority": 13,
    "interval": 10800,
    "next_tick": 0,
    "event_name": "自动MomoTalk",
    "func_name": "momo_talk"
  },
  {
    "enabled": true,
    "priority": 12,
    "interval": 0,
    "next_tick": 0,
    "event_name": "收集奖励",
    "func_name": "collect_reward"
  },
  {
    "enabled": true,
    "priority": 10,
    "interval": 0,
    "next_tick": 0,
    "event_name": "学院交流会",
    "func_name": "scrimmage"
  },
  {
    "enabled": true,
    "priority": -2,
    "interval": 0,
    "next_tick": 0,
    "event_name": "凌晨四点重启",
    "func_name": "restart"
  },
  {
    "enabled": true,
    "priority": -3,
    "interval": 10700,
    "next_tick": 0,
    "event_name": "定时刷新U2",
    "func_name": "refresh_uiautomator2"
  }
]
"""

DISPLAY_DEFAULT_CONFIG = """
{
  "running": "Empty",
  "queue": [
    "每日特别委托",
    "悬赏通缉",
    "竞技场",
    "收集每日体力",
    "收集小组体力",
    "商店购买",
    "日程",
    "主线清除体力",
    "自动MomoTalk",
    "咖啡厅",
    "查收邮箱",
    "自动制造",
    "收集奖励"
  ]
}
"""

DEFAULT_CONFIG = """
{
    "purchase_arena_ticket_times": "0",
    "screenshot_interval": "0.3",
    "ArenaLevelDiff": 5,
    "maxArenaRefreshTimes": 10,
    "createPriority": "花>Mo>情人节>果冻>色彩>灿烂>光芒>玲珑>白金>黄金>铜>白银>金属>隐然",
    "createTime": "3",
    "totalForceFightDifficulty": "NORMAL",
    "hardPriority": "1-1-1",
    "mainlinePriority": "5-1-1",
    "rewarded_task_times": "2,2,2",
    "purchase_rewarded_task_ticket_times": "0",
    "special_task_times": "1,1",
    "purchase_scrimmage_ticket_times": "0",
    "scrimmage_times": "2,2,2",
    "patStyle": "拖动礼物",
    "antiHarmony": true,
    "bannerVisibility": true,
    "favorStudent": [
        "爱丽丝"
    ],
    "server": "官服",
    "adbPort": "5555",
    "lesson_times": [
        1,
        1,
        1,
        1,
        1,
        1
    ],
    "purchase_lesson_ticket_times": "0",
    "explore_normal_task_regions": [

    ],
    "explore_hard_task_list": "此处填写需要推图的关卡",
    "manual_boss": false,
    "explore_activity": false,
    "burst1": "1",
    "burst2": "2",
    "pierce1": "1",
    "pierce2": "2",
    "mystic1": "1",
    "mystic2": "2",
    "activity_sweep": false,
    "activity_sweep_task_number": 1,
    "activity_sweep_times": 0,
    "activity_exchange_reward": false,
    "activity_exchange_50_times_at_once": false,
    "explore_hard_task_need_sss": true,
    "explore_hard_task_need_present": true,
    "explore_hard_task_need_task": true,
    "TacticalChallengeShopRefreshTime": "0",
    "TacticalChallengeShopList": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "CommonShopRefreshTime": "0",
    "CommonShopList": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "activity_list": [
        "arena",
        "cafe_reward",
        "lesson",
        "group",
        "mail",
        "collect_daily_power",
        "common_shop",
        "tactical_challenge_power",
        "rewarded_task",
        "normal_task",
        "hard_task",
        "scrimmage",
        "clear_special_task_power",
        "collect_reward",
        "momo_talk",
        "create",
        "total_force_fight"
    ]
}
"""

SWITCH_DEFAULT_CONFIG = '''
[
    {
        "config": "featureSwitch",
        "name": "功能开关",
        "sort": 0,
        "tip": "重要，此处为功能开关，控制各功能是否开启，启动前请检查是否开启。",
        "type": "SwitchSettingCard"
    },
    {
        "config": "cafeInvite",
        "name": "咖啡厅",
        "sort": 1,
        "tip": "帮助你收集咖啡厅体力和信用点",
        "type": "TextSettingCard"
    },
    {
        "config": "schedulePriority",
        "name": "日程",
        "sort": 2,
        "tip": "自动每日日程",
        "type": "TextSettingCard"
    },
    {
        "config": "shopPriority",
        "name": "商店购买",
        "sort": 6,
        "tip": "商店里买东西",
        "type": "CheckboxSettingCard"
    },
    {
        "config": "arenaShopPriority",
        "name": "竞技场商店购买",
        "sort": 7,
        "tip": "竞技场商店里买东西",
        "type": "CheckboxSettingCard"
    },
    {
        "config": "mainlinePriority",
        "name": "主线清除体力",
        "sort": 8,
        "tip": "主线关卡自动清除体力与每日困难",
        "type": "StageSettingCard"
    },
    {
        "config": "specialDaily",
        "name": "悬赏通缉",
        "sort": 10,
        "tip": "帮助你打每日悬赏通缉",
        "type": "SpecStageSettingCard"
    },
    {
        "config": "arenaPriority",
        "name": "竞技场",
        "sort": 11,
        "tip": "帮助你自动打竞技场",
        "type": "ComboSettingCard"
    },
    {
        "config": "createPriority",
        "name": "自动制造",
        "sort": 12,
        "tip": "帮助你自动制造",
        "type": "ComboSettingCard"
    },
    {
        "config": "totalForceFightPriority",
        "name": "总力战",
        "sort": 13,
        "tip": "总力战期间自动打总力战",
        "type": "BasicSettingCard"
    }
]

'''
STATIC_DEFAULT_CONFIG = '''
{
    "Global_student_name": [
                            "Akane (Bunny)",
                            "Ako",
                            "Aris",
                            "Aris (Maid)",
                            "Aru",
                            "Aru (New Year)",
                            "Asuna (Bunny)",
                            "Atsuko",
                            "Azusa",
                            "Azusa (Swimsuit)",
                            "Cherino",
                            "Cherino (Hot Spring)",
                            "Chihiro",
                            "Chinatsu (Hot Spring)",
                            "Chise (Swimsuit)",
                            "Eimi",
                            "Fuuka (New Year)",
                            "Hanae (Christmas)",
                            "Hanako (Swimsuit)",
                            "Haruka (New Year)",
                            "Haruna",
                            "Haruna (New Year)",
                            "Haruna (Track)",
                            "Hatsune Miku",
                            "Hibiki",
                            "Hifumi",
                            "Hifumi (Swimsuit)",
                            "Himari",
                            "Hina",
                            "Hina (Swimsuit)",
                            "Hinata",
                            "Hinata (Swimsuit)",
                            "Hiyori",
                            "Hoshino",
                            "Hoshino (Swimsuit)",
                            "Ichika",
                            "Iori",
                            "Iori (Swimsuit)",
                            "Iroha",
                            "Izumi",
                            "Izuna",
                            "Izuna (Swimsuit)",
                            "Kaede",
                            "Kaho",
                            "Kanna",
                            "Karin",
                            "Karin (Bunny)",
                            "Kasumi",
                            "Kayoko (New Year)",
                            "Kazusa",
                            "Koharu",
                            "Kokona",
                            "Kotori (Cheer Squad)",
                            "Koyuki",
                            "Maki",
                            "Mari (Track)",
                            "Marina",
                            "Mashiro",
                            "Mashiro (Swimsuit)",
                            "Megu",
                            "Meru",
                            "Midori",
                            "Mika",
                            "Mimori",
                            "Mimori (Swimsuit)",
                            "Mina",
                            "Mine",
                            "Minori",
                            "Misaka Mikoto",
                            "Misaki",
                            "Miyako",
                            "Miyako (Swimsuit)",
                            "Miyu",
                            "Moe",
                            "Mutsuki (New Year)",
                            "Nagisa",
                            "Natsu",
                            "Neru",
                            "Neru (Bunny)",
                            "Noa",
                            "Nodoka (Hot Spring)",
                            "Nonomi (Swimsuit)",
                            "Reisa",
                            "Rumi",
                            "Saki",
                            "Saki (Swimsuit)",
                            "Sakurako",
                            "Saori",
                            "Saya",
                            "Saya (Casual)",
                            "Sena",
                            "Serina (Christmas)",
                            "Shigure",
                            "Shigure (Hot Spring)",
                            "Shiroko",
                            "Shiroko (Cycling)",
                            "Shiroko (Swimsuit)",
                            "Shokuhou Misaki",
                            "Shun",
                            "Shun (Small)",
                            "Sumire",
                            "Toki",
                            "Toki (Bunny)",
                            "Tsukuyo",
                            "Tsurugi",
                            "Ui",
                            "Ui (Swimsuit)",
                            "Utaha (Cheer Squad)",
                            "Wakamo",
                            "Wakamo (Swimsuit)",
                            "Yuuka (Track)",
                            "Yuzu",
                            "Airi",
                            "Akane",
                            "Akari",
                            "Ayane",
                            "Chise",
                            "Fuuka",
                            "Hanae",
                            "Hanako",
                            "Hare",
                            "Hasumi",
                            "Junko",
                            "Kayoko",
                            "Kirino",
                            "Mari",
                            "Momiji",
                            "Momoi",
                            "Mutsuki",
                            "Nonomi",
                            "Serika",
                            "Shizuko",
                            "Tsubaki",
                            "Utaha",
                            "Yuuka",
                            "Asuna",
                            "Asuna (Bunny)",
                            "Ayane (Swimsuit)",
                            "Chinatsu",
                            "Fubuki",
                            "Haruka",
                            "Hasumi (Track)",
                            "Hibiki (Cheer Squad)",
                            "Izumi (Swimsuit)",
                            "Junko (New Year)",
                            "Juri",
                            "Koharu (Swimsuit)",
                            "Kotama",
                            "Kotori",
                            "Michiru",
                            "Miyu (Swimsuit)",
                            "Nodoka",
                            "Pina",
                            "Saten Ruiko",
                            "Serina",
                            "Shimiko",
                            "Shizuko (Swimsuit)",
                            "Suzumi",
                            "Tomoe",
                            "Tsurugi (Swimsuit)",
                            "Yoshimi",
                            "Yuzu (Maid)"
                            ],
    "CN_student_name": [
                        "切里诺(温泉)",
                        "和香(温泉)",
                        "千夏(温泉)",
                        "小夏",
                        "亚子",
                        "玛丽",
                        "瞬(小)",
                        "桐乃",
                        "伊织(泳装)",
                        "日奈(泳装)",
                        "纱绫(便服)",
                        "日富美(泳装)",
                        "真白(泳装)",
                        "鹤城(泳装)",
                        "白子(骑行)",
                        "梓(泳装)",
                        "爱丽丝",
                        "切里诺",
                        "志美子",
                        "日富美",
                        "佳代子",
                        "明日奈",
                        "菲娜",
                        "艾米",
                        "真纪",
                        "泉奈",
                        "明里",
                        "芹香",
                        "优香",
                        "小春",
                        "花江",
                        "纯子",
                        "千世",
                        "干世",
                        "莲见",
                        "爱理",
                        "睦月",
                        "野宫",
                        "绫音",
                        "歌原",
                        "芹娜",
                        "小玉",
                        "铃美",
                        "朱莉",
                        "好美",
                        "千夏",
                        "琴里",
                        "春香",
                        "真白",
                        "鹤城",
                        "爱露",
                        "晴奈",
                        "日奈",
                        "伊织",
                        "星野",
                        "白子",
                        "柚子",
                        "花凛",
                        "妮露",
                        "纱绫",
                        "静子",
                        "花子",
                        "风香",
                        "和香",
                        "茜",
                        "泉",
                        "梓",
                        "绿",
                        "堇",
                        "瞬",
                        "桃",
                        "椿",
                        "晴",
                        "响"
                        ],
    "current_game_activity": {
        "CN": "no_68_spring_wild_dream",
        "Global": null,
        "JP": null
    },
    "common_shop_price_list": {
        "CN": [30,30,30,30,10000,40000,96000,128000,10000,40000,96000,128000,8000,8000,25000,25000],
        "JP": [12500, 125000, 300000, 500000, 10000, 40000, 96000, 128000, 10000, 40000, 96000, 128000, 20000, 80000, 192000, 256000, 8000, 8000, 25000, 25000],
        "Global": [12500, 125000, 300000, 500000, 10000, 40000, 96000, 128000, 10000, 40000, 96000, 128000, 20000, 80000, 192000, 256000, 8000, 8000, 25000, 25000]
    },
    "tactical_challenge_shop_price_list": {
        "CN": [50, 50, 50, 50, 15, 30, 5, 25, 60, 100, 4, 20, 60, 100],
        "JP": [50, 50, 50, 50, 50, 15, 30, 5, 25, 60, 100, 4, 20, 60, 100],
        "Global": [50, 50, 50, 50, 50, 15, 30, 5, 25, 60, 100, 4, 20, 60, 100]
    },
    "package_name": {
        "官服": "com.RoamingStar.BlueArchive",
        "B服": "com.RoamingStar.BlueArchive.bilibili",
        "国际服": "com.nexon.bluearchive",
        "日服": "com.YostarJP.BlueArchive"
    },
    "activity_name": {
        "官服": "com.yostar.sdk.bridge.YoStarUnityPlayerActivity",
        "B服": "com.yostar.sdk.bridge.YoStarUnityPlayerActivity",
        "国际服": ".MxUnityPlayerActivity",
        "日服": "com.yostarjp.bluearchive.MxUnityPlayerActivity"
    }
}
'''
