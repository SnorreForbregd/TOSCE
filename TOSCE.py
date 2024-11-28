'''TOSCE, if you dare even harder'''

import random as r
import copy
from time import sleep
import sys

winDictTeam = {}
winDictRole = {}
def setGlobals(debug = False):

    global CPUGame
    global DebugGame
    global Cycles
    global NightmareTrigger
    global Nightmare
    global ERampageTrigger
    global WRampageTrigger
    global PRampageTrigger
    global GRampageTrigger
    global PBRampageTrigger
    global PoisonerSaver
    global Snorre
    global PlayersAlive
    global DrawCount
    global PlayerRevived
    global Day
    global Night
    global Win
    global Jester
    global AssistingDog
    global Bulleter
    global PestilenceInGame
    global DrageTrigger
    global HunterList
    global TotalRoleStats
    global RoleStats
    global Template
    global RoleStatuses
    global RoleList
    global Teams
    global MainKillingRoles
    global ArsonistKilling
    global CrazyKilling
    global DogKilling
    global FreezerKilling
    global MafiaKilling
    global PoisonerKilling
    global SerialKilling
    global StupidoKilling
    global TerroristKilling
    global VampireKilling
    global WerewolfKilling
    global AmneList
    global InvestList
    global NonVisitList
    global GoodList
    global SurvivalList
    global Night_action_order
    global Players
    global PlayerNames
    global PlayerSequence
    global RoleSequence
    global PromoteList
    global VoteList
    global VoteList2
    global TurnList
    
    CPUGame = True
    DebugGame = debug
    Cycles = 0
    NightmareTrigger = False
    Nightmare = False
    ERampageTrigger = False
    WRampageTrigger = False
    PRampageTrigger = False
    GRampageTrigger = False
    PBRampageTrigger = False
    PoisonerSaver = False
    Snorre = False
    PlayersAlive = 0
    DrawCount = 0
    PlayerRevived = False
    Day = 1
    Night = 0
    Win = False
    Jester = False
    AssistingDog = False
    Bulleter = False
    PestilenceInGame = False
    DrageTrigger = 0

    HunterList = ["Freezer_hunter", "Creator_hunter", "FBI_hunter", "Crazy_knight_hunter", "Coven_hunter",
            "Terrorist_hunter", "Police_hunter", "SK_hunter", "Mafia_hunter", "Stupido_hunter",
            "Crazy_hunter", "Hunter_hunter", "Combo_hunter", "Pestilence_hunter_H", "Pestilence_hunter_K",
            "Pestilence_hunter_R", "Vampire_hunter", "Werewolf_hunter", "Dog_mauler", "Firefighter", "Poisoner_hunter"]

    '''Dictionary with all of the info tied to the specific roles. Indexes and explanations below:
0 - Current role
1 - Alive?
2 - Attack
3 - Immunity
4 - Team
5 - Hunter?
6 - Hunting?
7 - Hunter hunter?
8 - Type (Killing, Investigating, Supporting, Protecting, Hunting, Existing)
9 - Alignment (Town, Mafia or Neutral)
10 - Alignment2 (Killing, Protective, Support, Investigative, Deception, Evil, Benign, Chaos)
11 - Suspicious?
12 - Investigative-result (List with 3/4 roles)
13 - Target-type (explanation below list) (list)
14 - Roleblock-immune?
15 - Rage?
16 - Control-immune?
17 - Control-effect-immune?
18 - Unique?
19 - Good?
20 - CPU?
21 - Countdown1 (Nikkiller has 3 here)
22 - Countdown2
23 - Countdown3 (Will reset)
24 - Already-checked (list)
25 - Healed amount
26 - Target (list)
27 - Log (For non-Cpu games)
28 - Results (For investigative-roles)
29 - Visiting (List of people visited by current target of lookout, or target of tracker visited)
30 - Already won?
31 - Youngest? (Vampires only)
32 - ContactWithMurderer? (Mafia-members only) 
33 - Has Necronomicon
34 - Check (bool, begins at False)
35 - Turnable (Mafiturner and Jesper) Starts at True
36 - Countdown4 (for special needs)
37 - Killed by (list)
38 - Currently identifying (for identifier) (lists with name, number of identifications)

Target-type defines who the role will choose as a target in a CPU-game:
0 - First
1 - First non-team
2 - First team
3 - Second
4 - Second non-team
5 - Second team
6 - Next
7 - Next non-team
8 - Dead
9 - Behind
10 - Behind non-team
11 - Next team
12 - Dead good (not combo)
This is a list, as roles can have multiple targets.
'''

    TotalRoleStats = {
    "Arsonist" : ["Arsonist", True, 5, 2, "Arsonists", False, "", False, "Killing", "Neutral", "Killing", True, ["Arsonist", "Poisoner", "Transporter"], [7], False, False, False, False, False, False, False, 1, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Gasthrower" : ["Gasthrower", True, 0, 0, "Arsonists", False, "", False, "Support", "Neutral", "Evil", True, ["Revengetaker", "Agent", "Gasthrower"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Incinerator" : ["Incinerator", True, 5, 0, "Arsonists", False, "", False, "Killing", "Neutral", "Killing", True, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [0], False, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Freezer_hunter" : ["Freezer_hunter", True, 0, 0, "Arsonists", True, "Freezers", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Washer" : ["Washer", True, 0, 0, "Arsonists", False, "", False, "Protective", "Neutral", "Evil", False, ["Washer", "Security_guard", "Mikael"], [2], False, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [],[]],
    "Amnescriff" : ["Amnescriff", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Amnesiac", "Amneshiff", "Amnescriff"], [6], False, False, True, True, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Amneshiff" : ["Amneshiff", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Amnesiac", "Amneshiff", "Amnescriff"], [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Amnesiac" : ["Amnesiac", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Amnesiac", "Amneshiff", "Amnescriff"], [8], False, False, True, True, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Creator_hunter" : ["Creator_hunter", True, 0, 0, "Combo", True, "Creators", False, "Hunting", "Neutral", "Benign", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Guardian_angel" : ["Guardian_angel", True, 0, 0, "Combo", False, "", False, "Protecting", "Neutral", "Benign", False, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [0], False, False, True, True, False, True, False, 2, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jester" : ["Jester", True, 7, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Clown", "Jester", "Nighter"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Killager" : ["Killager", True, 3, 0, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Johannes", "Jailwolf", "Killager"], [0], False, False, False, False, False, True, False, 1, 3, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Librarian" : ["Librarian", True, 5, 5, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Librarian", "Writer", "Idiot"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Magicmaker" : ["Magicmaker", True, 7, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Immunist", "Magicmaker", "Hex_master"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Nighter" : ["Nighter", True, 7, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Clown", "Jester", "Nighter"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Nightmare" : ["Nightmare", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Nightmare", "Trapper", "Targeter", "Digger"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pirate" : ["Pirate", True, 3, 0, "Combo", False, "", False, "Killing", "Neutral", "Chaos", False, ["Oliver", "Identifier", "Pirate", "Werepup"], [0], False, False, True, True, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Scared" : ["Scared", True, 3, 0, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Scared", "Vampire", "Lookout"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Survivor" : ["Survivor", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Villager", "Villargeter", "Survivor"], [0], False, False, True, True, False, True, False, 4, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Villager" : ["Villager", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Villager", "Villargeter", "Survivor"], [0], False, False, True, True, False, True, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Villargeter" : ["Villargeter", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Villager", "Villargeter", "Survivor"], [0], False, False, True, True, False, True, False, 4, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Writer" : ["Writer", True, 7, 0, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Librarian", "Writer", "Idiot"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Coven_leader" : ["Coven_leader", True, 2, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Hypnotist", "Coven_leader", "Remover"], [1,4], True, False, True, True, True, False, False, 0, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "FBI_hunter" : ["FBI_hunter", True, 0, 0, "Coven", True, "FBI", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Hex_master" : ["Hex_master", True, 5, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Immunist", "Magicmaker", "Immunist"], [7], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Medusa" : ["Medusa", True, 4, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Veteran", "Medusa", "Pestilence"], [1], False, False, False, False, False, False, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Necromancer" : ["Necromancer", True, 0, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Retributionist", "Necromancer", "Medium"], [0], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Potion_master" : ["Potion_master", True, 3, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Doctor", "Potion_master", "Pollutifier"], [8], False, False, False, False, False, False, False, 2, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy" : ["Crazy", True, 4, 0, "Crazies", False, "", False, "Killing", "Neutral", "Killing", True, ["Haunter", "Crazy", "Assisting_dog"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy_king" : ["Crazy_king", True, 6, 1, "Crazies", False, "", False, "Killing", "Neutral", "Killing", False, ["General", "King", "Queen", "Crazy_king"], [1], False, True, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy_knight_hunter" : ["Crazy_knight_hunter", True, 0, 0, "Crazies", True, "Knights", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Targeter" : ["Targeter", True, 3, 0, "Crazies", False, "", False, "Killing", "Neutral", "Killing", True, ["Nightmare", "Trapper", "Targeter"], [1], True, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Thief" : ["Thief", True, 0, 0, "Crazies", False, "", False, "Supporting", "Neutral", "Evil", True, ["Escort", "Consort", "Thief"], [1], True, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Elias" : ["Elias", True, 0, 0, "Creators", False, "", False, "Killing", "Neutral", "Killing", True, ["Worker", "Elias", "Nikkiller"], [4], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jesper" : ["Jesper", True, 0, 0, "Creators", False, "", False, "Supporting", "Neutral", "Evil", True, ["Jesper", "Mafiturner", "Spy"], [1], False, False, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Johannes" : ["Johannes", True, 2, 0, "Creators", False, "", False, "Killing", "Neutral", "Killing", True, ["Johannes", "Jailwolf", "Killager"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Kristian" : ["Kristian", True, 0, 0, "Creators", False, "", False, "Protecting", "Neutral", "Evil", True, ["Kristian", "Bodyguard", "Police"], [11], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mikael" : ["Mikael", True, 0, 0, "Creators", False, "", False, "Protecting", "Neutral", "Evil", True, ["Washer", "Security_guard", "Mikael"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Ole_bjorn" : ["Ole_bjorn", True, 0, 0, "Creators", False, "", False, "Investigating", "Neutral", "Evil", True, ["Ole_bjorn", "Journalist", "Consigliere"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Oliver" : ["Oliver", True, 3, 0, "Creators", False, "", False, "Killing", "Neutral", "Killing", True, ["Oliver", "Identifier", "Pirate", "Werepup"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Snorre" : ["Snorre", True, 0, 0, "Creators", False, "", False, "Supporting", "Neutral", "Evil", True, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Assassin_dog" : ["Assassin_dog", True, 3, 0, "Dogs", False, "", False, "Killing", "Neutral", "Killing", False, ["Sniper", "Archer", "Murderer", "Assassin_dog"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Assisting_dog" : ["Assisting_dog", True, 0, 0, "Dogs", False, "", False, "Supporting", "Neutral", "Evil", True, ["Haunter", "Crazy", "Assisting_dog"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Digger" : ["Digger", True, 0, 0, "Dogs", False, "", False, "Supporting", "Neutral", "Evil", True, ["Nightmare", "Targeter", "Trapper", "Digger"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Herman" : ["Herman", True, 2, 1, "Dogs", False, "", False, "Killing", "Neutral", "Killing", True, ["Statuschecker", "Herman", "Werewolf"], [7], False, False, False, False, False, False, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Token" : ["Token", True, 1, 0, "Dogs", False, "", False, "Killing", "Neutral", "Killing", True, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Agent" : ["Agent", True, 1, 0, "FBI", False, "", False, "Killing", "Neutral", "Killing", False, ["Revengetaker", "Agent", "Gasthrower"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Agent_ZK" : ["Agent_ZK", True, 4, 1, "FBI", False, "", False, "Killing", "Neutral", "Killing", False, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Coven_hunter" : ["Coven_hunter", True, 0, 0, "FBI", True, "Coven", False, "Hunting", "Neutral", "Benign", False, HunterList, [7], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "FBI" : ["FBI", True, 7, 0, "FBI", False, "", False, "Killing", "Neutral", "Killing", False, ["FBI", "Godfather", "Dracula"], [1], False, False, False, False, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Cooler" : ["Cooler", True, 0, 0, "Freezers", False, "", False, "Supporting", "Neutral", "Evil", True, ["Sculpturer", "Waller", "Armorer", "Cooler"], [7], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0 ,[], []],
    "Eskimo" : ["Eskimo", True, 0, 0, "Freezers", False, "", False, "Protecting", "Neutral", "Evil", True, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [2], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Freezer" : ["Freezer", True, 4, 2, "Freezers", False, "", False, "Killing", "Neutral", "Killing", True, ["Tracker", "Freezer", "Ambusher"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Polar_bear" : ["Polar_bear", True, 4, 3, "Freezers", False, "", False, "Killing", "Neutral", "Killing", True, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [1], False, False, False, False, False, False, False, 0, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Sculpturer" : ["Sculpturer", True, 0, 0, "Freezers", False, "", False, "Supporting", "Neutral", "Evil", False, ["Sculpturer", "Waller", "Armorer", "Cooler"], [0], False, False, False, False, False, False, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Terrorist_hunter" : ["Terrorist_hunter", True, 0, 0, "Freezers", True, "Terrorists", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Archer" : ["Archer", True, 4, 0, "Knights", False, "", False, "Killing", "Neutral", "Killing", True, ["Sniper", "Archer", "Murderer", "Assassin_dog"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "King" : ["King", True, 0, 0, "Knights", False, "", False, "Existing", "Neutral", "Benign", False, ["General", "King", "Queen", "Crazy_king"], [1], False, False, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Knight" : ["Knight", True, 4, 3, "Knights", False, "", False, "Killing", "Neutral", "Killing", True, ["Crusader", "Serial_killer", "Knight"], [1], False, True, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Lifeguard1" : ["Lifeguard1", True, 0, 0, "Knights", False, "", False, "Protecting", "Neutral", "Benign", False, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Lifeguard2" : ["Lifeguard2", True, 0, 0, "Knights", False, "", False, "Protecting", "Neutral", "Benign", False, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Police_hunter" : ["Police_hunter", True, 0, 0, "Knights", True, "Police", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Queen" : ["Queen", True, 0, 0, "Knights", False, "", False, "Existing", "Neutral", "Benign", False, ["General", "King", "Queen", "Crazy_king"], [1], False, False, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Ambusher" : ["Ambusher", True, 1, 0, "Mafia", False, "", False, "Killing", "Mafia", "Killing", True, ["Tracker", "Freezer", "Ambusher"], [4], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Consigliere" : ["Consigliere", True, 0, 0, "Mafia", False, "", False, "Investigating", "Mafia", "Support", True, ["Ole_bjorn", "Journalist", "Consigliere"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Consort" : ["Consort", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Support", True, ["Escort", "Consort", "Thief"], [1], True, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Framer" : ["Framer", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", True, ["Framer", "Unframer", "Robber"], [4], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Godfather" : ["Godfather", True, 2, 2, "Mafia", False, "", False, "Killing", "Mafia", "Killing", False, ["FBI", "Godfather", "Dracula"], [1], False, False, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Hypnotist" : ["Hypnotist", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", True, ["Hypnotist", "Coven_leader", "Remover"], [0], True, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Janitor" : ["Janitor", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", True, ["Sheriff", "Investigator", "Janitor"], [0], False, False, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafioso" : ["Mafioso", True, 1, 0, "Mafia", False, "", False, "Killing", "Mafia", "Killing", True, ["Vigilante", "Terrorist", "Mafioso"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafiturner" : ["Mafiturner", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Support", True, ["Jesper", "Mafiturner", "Spy"], [7], False, False, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Murderer" : ["Murderer", True, 3, 0, "Mafia", False, "", False, "Killing", "Mafia", "Killing", True, ["Sniper", "Archer" "Murderer", "Assassin_dog"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "SK_hunter" : ["SK_hunter", True, 0, 0, "Mafia", True, "Serial_killers", False, "Hunting", "Mafia", "Support", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Unframer" : ["Unframer", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", False, ["Framer", "Unframer", "Robber"], [2], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafia_hunter" : ["Mafia_hunter", True, 0, 0, "Poisoners", True, "Mafia", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Poisoner" : ["Poisoner", True, 5, 2, "Poisoners", False, "", False, "Killing", "Neutral", "Killing", True, ["Arsonist", "Poisoner", "Transporter"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Poisoner_saver" : ["Poisoner_saver", True, 6, 0, "Poisoners", False, "", False, "Protecting", "Neutral", "Evil", True, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pollutifier" : ["Pollutifier", True, 5, 0, "Poisoners", False, "", False, "Killing", "Neutral", "Killing", True, ["Doctor", "Potion_master", "Pollutifier"], [4], False, False, False, False, False, False, False, 1, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "General" : ["General", True, 0, 1, "Police", False, "", False, "Existing", "Neutral", "Benign", False, ["General", "King", "Queen", "Crazy_king"], [1], False, False, False, False, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Identifier" : ["Identifier", True, 0, 0, "Police", False, "", False, "Investigating", "Neutral", "Benign", False, ["Oliver", "Identifier", "Pirate", "Werepup"], [7], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Police" : ["Police", True, 1, 0, "Police", False, "", False, "Protecting", "Neutral", "Benign", False, ["Kristian", "Bodyguard", "Police"], [3], False, False, False, False, False, True, False, 1, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 3, [], []],
    "Sniper" : ["Sniper", True, 4, 0, "Police", False, "", False, "Killing", "Neutral", "Killing", False, ["Sniper", "Archer", "Murderer", "Assassin_dog"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Soldier" : ["Soldier", True, 4, 0, "Police", False, "", False, "Killing", "Neutral", "Killing", False, ["Stupido", "Soldier", "Huntrustiff"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Stupido_hunter" : ["Stupido_hunter", True, 0, 0, "Police", True, "Stupidos", False, "Hunting", "Neutral", "Benign", False, HunterList, [7], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Tankman" : ["Tankman", True, 5, 1, "Police", False, "", False, "Killing", "Neutral", "Killing", False, ["Suicide_bomber", "Grenadethrower", "Tankman"], [1], False, False, False, False, False, True, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy_hunter" : ["Crazy_hunter", True, 0, 0, "Serial_killers", True, "Crazies", False, "Hunting", "Neutral", "Evil", True, ["Crusader", "Serial_killer", "Knight"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Daylight_killer" : ["Daylight_killer", True, 0, 0, "Serial_killers", False, "", False, "Killing", "Neutral", "Killing", True, ["Mayor", "Dayriff", "Daylight_killer"], [1], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Nikkiller" : ["Nikkiller", True, 5, 0, "Serial_killers", False, "", False, "Killing", "Neutral", "Killing", True, ["Worker", "Elias", "Nikkiller"], [7], False, True, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Robber" : ["Robber", True, 0, 0, "Serial_killers", False, "", False, "Supporting", "Neutral", "Evil", True, ["Framer", "Unframer", "Robber"], [0], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Serial_killer" : ["Serial_killer", True, 2, 2, "Serial_killers", False, "", False, "Killing", "Neutral", "Killing", True, ["Crusader", "Serial_killer", "Knight"], [1], False, True, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Clown" : ["Clown", True, 0, 0, "Stupidos", False, "", False, "Supporting", "Neutral", "Evil", True, ["Clown", "Jester", "Nighter"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Hunter_hunter" : ["Hunter_hunter", True, 0, 0, "Stupidos", True, "", True, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Idiot" : ["Idiot", True, 0, 0, "Stupidos", False, "", False, "Supporting", "Neutral", "Evil", True, ["Librarian", "Writer", "Idiot"], [0], True, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Remover" : ["Remover", True, 0, 0, "Stupidos", False, "", False, "Supporting", "Neutral", "Evil", True, ["Hypnotist", "Coven_leader", "Remover"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Stupido" : ["Stupido", True, 4, 0, "Stupidos", False, "", False, "Killing", "Neutral", "Killing", True, ["Stupido", "Soldier", "Huntrustiff"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Armorer" : ["Armorer", True, 0, 0, "Terrorists", False, "", False, "Protecting", "Neutral", "Evil", True, ["Sculpturer", "Waller", "Armorer", "Cooler"], [11], False, False, False, False, False, False, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Bulleter" : ["Bulleter", True, 0, 0, "Terrorists", False, "", False, "Supporting", "Neutral", "Evil", True, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [0], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Combo_hunter" : ["Combo_hunter", True, 0, 0, "Terrorists", True, "Combo", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Grenadethrower" : ["Grenadethrower", True, 5, 0, "Terrorists", False, "", False, "Killing", "Neutral", "Killing", True, ["Suicide_bomber", "Grenadethrower", "Tankman"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Suicide_bomber" : ["Suicide_bomber", True, 7, 0, "Terrorists", False, "", False, "Killing", "Neutral", "Killing", True, ["Suicide_bomber", "Grenadethrower", "Tankman"], [0], False, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Terrorist" : ["Terrorist", True, 4, 0, "Terrorists", False, "", False, "Killing", "Neutral", "Killing", True, ["Vigilante", "Terrorist", "Mafioso"], [7], False, True, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Bodyguard" : ["Bodyguard", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Kristian", "Bodyguard", "Police"], [3], False, False, False, False, False, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crusader" : ["Crusader", True, 1, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Crusader", "Serial_killer", "Knight"], [3], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Dayriff" : ["Dayriff", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Mayor", "Dayriff", "Daylight_killer"], [6], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Doctor" : ["Doctor", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Doctor", "Potion_master", "Pollutifier"], [3], False, False, False, False, False, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Escort" : ["Escort", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Escort", "Consort", "Thief"], [0], True, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Haunter" : ["Haunter", True, 7, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Haunter", "Crazy", "Assisting_dog"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Huntrustiff" : ["Huntrustiff", True, 1, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Stupido", "Soldier", "Huntrustiff"], [6], False, False, False, False, True, True, False, 3, 3, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Immunist" : ["Immunist", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Immunist", "Magicmaker", "Hex_master"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Investigator" : ["Investigator", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Sheriff", "Investigator", "Janitor"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jailor" : ["Jailor", True, 7, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Jailor", "Frenzied_thrall", "Drage"], [0], False, False, True, True, True, True, False, 3, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Journalist" : ["Journalist", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Ole_bjorn", "Journalist", "Consigliere"], [6], False, False, False, False, False, True, False, 1, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Lookout" : ["Lookout", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Scared", "Vampire", "Lookout"], [3], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mayor" : ["Mayor", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Mayor", "Dayriff", "Daylight_killer"], [0], False, False, True, True, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mayorguarder" : ["Mayorguarder", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Medium" : ["Medium", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Retributionist", "Necromancer", "Medium"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence_hunter_H" : ["Pestilence_hunter_H", True, 0, 0, "Town", True, "Pestilences", False, "Hunting", "Town", "Protective", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence_hunter_K" : ["Pestilence_hunter_K", True, 1, 0, "Town", True, "Pestilences", False, "Hunting", "Town", "Killing", False, HunterList, [6], False, False, False, False, False, True, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence_hunter_R" : ["Pestilence_hunter_R", True, 0, 0, "Town", True, "Pestilences", False, "Hunting", "Town", "Investigative", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Retributionist" : ["Retributionist", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Retributionist", "Necromancer", "Medium"], [12], False, False, True, True, True, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Revengetaker" : ["Revengetaker", True, 7, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Revengetaker", "Agent", "Gasthrower"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Security_guard" : ["Security_guard", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Washer", "Security_guard", "Mikael"], [3], True, False, True, True, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Sheriff" : ["Sheriff", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Sheriff", "Investigator", "Janitor"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Spy" : ["Spy", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Jesper", "Mafiturner", "Spy"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Statuschecker" : ["Statuschecker", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Statuschecker", "Herman", "Werewolf"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Tracker" : ["Tracker", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Tracker", "Freezer", "Ambusher"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Transporter" : ["Transporter", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Arsonist", "Poisoner", "Transporter"], [6], True, False, True, True, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Trapper" : ["Trapper", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Nightmare", "Trapper", "Targeter", "Digger"], [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Vampire_hunter" : ["Vampire_hunter", True, 0, 0, "Town", True, "Vampires", False, "Hunting", "Town", "Killing", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Veteran" : ["Veteran", True, 6, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Veteran", "Medusa", "Pestilence"], [0], False, False, True, True, True, True, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Vigilante" : ["Vigilante", True, 3, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Vigilante", "Terrorist", "Mafioso"], [0], False, False, False, False, False, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Waller" : ["Waller", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Sculpturer", "Waller", "Armorer", "Cooler"], [3], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Worker" : ["Worker", True, 8, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Worker", "Elias", "Nikkiller"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Dracula" : ["Dracula", True, 2, 1, "Vampires", False, "", False, "Killing", "Neutral", "Chaos", False, ["FBI", "Godfather", "Dracula"], [1], False, False, False, False, True, False, False, 3, 1, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 1, [], []],
    "Frenzied_thrall" : ["Frenzied_thrall", True, 1, 0, "Vampires", False, "", False, "Killing", "Neutral", "Chaos", True, ["Jailor", "Frenzied_thrall", "Drage"], [4], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Vampire" : ["Vampire", True, 1, 0, "Vampires", False, "", False, "Killing", "Neutral", "Chaos", True, ["Scared", "Vampire", "Lookout"], [1], False, False, False, False, False, False, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Werewolf_hunter" : ["Werewolf_hunter", True, 0, 0, "Vampires", True, "Werewolves", False, "Hunting", "Neutral", "Chaos", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Dog_mauler" : ["Dog_mauler", True, 0, 0, "Werewolves", True, "Dogs", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Firefighter" : ["Firefighter", True, 0, 0, "Werewolves", True, "Arsonists", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jailwolf" : ["Jailwolf", True, 4, 0, "Werewolves", False, "", False, "Killing", "Neutral", "Killing", True, ["Johannes", "Jailwolf", "Killager"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Poisoner_hunter" : ["Poisoner_hunter", True, 0, 0, "Werewolves", True, "Poisoners", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Werepup" : ["Werepup", True, 0, 0, "Werewolves", False, "", False, "Existing", "Neutral", "Evil", True, ["Oliver", "Identifier", "Pirate", "Werepup"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Werewolf" : ["Werewolf", True, 4, 3, "Werewolves", False, "", False, "Killing", "Neutral", "Killing", True, ["Statuschecker", "Herman", "Werewolf"], [1], False, True, False, False, False, False, False, 0, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Drage" : ["Drage", True, 0, 0, "Dragons", False, "", False, "Killing", "Neutral", "Killing", True, ["Jailor", "Frenzied_thrall", "Drage"], [7], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence" : ["Pestilence", True, 6, 5, "Pestilences", False, "", False, "Killing", "Neutral", "Killing", True, ["Veteran", "Medusa", "Pestilence"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafia_villager" : ["Mafia_villager", True, 0, 0, "Mafia", False, "", False, "Existing", "Mafia", "Support", True, ["Ingenting", "Mafia_villager", "Creator_villager"], [0], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Creator_villager" : ["Creator_villager", True, 0, 0, "Creators", False, "", False, "Existing", "Neutral", "Evil", True, ["Ingenting", "Mafia_villager", "Creator_villager"], [0], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Ingenting" : ["Ingenting", True, 0, 0, "Ingenting", False, "", False, "Existing", "Neutral", "Benign", False, ["Ingenting", "Mafia_villager", "Creator_villager"], [0], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []]
}



    '''Same as above, but will change during the game'''

    RoleStats = {
    "Arsonist" : ["Arsonist", True, 5, 2, "Arsonists", False, "", False, "Killing", "Neutral", "Killing", True, ["Arsonist", "Poisoner", "Transporter"], [7], False, False, False, False, False, False, False, 1, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Gasthrower" : ["Gasthrower", True, 0, 0, "Arsonists", False, "", False, "Support", "Neutral", "Evil", True, ["Revengetaker", "Agent", "Gasthrower"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Incinerator" : ["Incinerator", True, 5, 0, "Arsonists", False, "", False, "Killing", "Neutral", "Killing", True, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [0], False, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Freezer_hunter" : ["Freezer_hunter", True, 0, 0, "Arsonists", True, "Freezers", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Washer" : ["Washer", True, 0, 0, "Arsonists", False, "", False, "Protective", "Neutral", "Evil", False, ["Washer", "Security_guard", "Mikael"], [2], False, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [],[]],
    "Amnescriff" : ["Amnescriff", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Amnesiac", "Amneshiff", "Amnescriff"], [6], False, False, True, True, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Amneshiff" : ["Amneshiff", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Amnesiac", "Amneshiff", "Amnescriff"], [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Amnesiac" : ["Amnesiac", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Amnesiac", "Amneshiff", "Amnescriff"], [8], False, False, True, True, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Creator_hunter" : ["Creator_hunter", True, 0, 0, "Combo", True, "Creators", False, "Hunting", "Neutral", "Benign", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Guardian_angel" : ["Guardian_angel", True, 0, 0, "Combo", False, "", False, "Protecting", "Neutral", "Benign", False, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [0], False, False, True, True, False, True, False, 2, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jester" : ["Jester", True, 7, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Clown", "Jester", "Nighter"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Killager" : ["Killager", True, 3, 0, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Johannes", "Jailwolf", "Killager"], [0], False, False, False, False, False, True, False, 1, 3, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Librarian" : ["Librarian", True, 5, 5, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Librarian", "Writer", "Idiot"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Magicmaker" : ["Magicmaker", True, 7, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Immunist", "Magicmaker", "Hex_master"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Nighter" : ["Nighter", True, 7, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Clown", "Jester", "Nighter"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Nightmare" : ["Nightmare", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Evil", False, ["Nightmare", "Trapper", "Targeter", "Digger"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pirate" : ["Pirate", True, 3, 0, "Combo", False, "", False, "Killing", "Neutral", "Chaos", False, ["Oliver", "Identifier", "Pirate", "Werepup"], [0], False, False, True, True, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Scared" : ["Scared", True, 3, 0, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Scared", "Vampire", "Lookout"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Survivor" : ["Survivor", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Villager", "Villargeter", "Survivor"], [0], False, False, True, True, False, True, False, 4, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Villager" : ["Villager", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Villager", "Villargeter", "Survivor"], [0], False, False, True, True, False, True, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Villargeter" : ["Villargeter", True, 0, 0, "Combo", False, "", False, "Existing", "Neutral", "Benign", False, ["Villager", "Villargeter", "Survivor"], [0], False, False, True, True, False, True, False, 4, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Writer" : ["Writer", True, 7, 0, "Combo", False, "", False, "Killing", "Neutral", "Killing", False, ["Librarian", "Writer", "Idiot"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Coven_leader" : ["Coven_leader", True, 2, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Hypnotist", "Coven_leader", "Remover"], [1,4], True, False, True, True, True, False, False, 0, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "FBI_hunter" : ["FBI_hunter", True, 0, 0, "Coven", True, "FBI", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Hex_master" : ["Hex_master", True, 5, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Immunist", "Magicmaker", "Immunist"], [7], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Medusa" : ["Medusa", True, 4, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Veteran", "Medusa", "Pestilence"], [1], False, False, False, False, False, False, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Necromancer" : ["Necromancer", True, 0, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Retributionist", "Necromancer", "Medium"], [0], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Potion_master" : ["Potion_master", True, 3, 0, "Coven", False, "", False, "Killing", "Neutral", "Killing", True, ["Doctor", "Potion_master", "Pollutifier"], [8], False, False, False, False, False, False, False, 2, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy" : ["Crazy", True, 4, 0, "Crazies", False, "", False, "Killing", "Neutral", "Killing", True, ["Haunter", "Crazy", "Assisting_dog"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy_king" : ["Crazy_king", True, 6, 1, "Crazies", False, "", False, "Killing", "Neutral", "Killing", False, ["General", "King", "Queen", "Crazy_king"], [1], False, True, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy_knight_hunter" : ["Crazy_knight_hunter", True, 0, 0, "Crazies", True, "Knights", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Targeter" : ["Targeter", True, 3, 0, "Crazies", False, "", False, "Killing", "Neutral", "Killing", True, ["Nightmare", "Trapper", "Targeter"], [1], True, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Thief" : ["Thief", True, 0, 0, "Crazies", False, "", False, "Supporting", "Neutral", "Evil", True, ["Escort", "Consort", "Thief"], [1], True, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Elias" : ["Elias", True, 0, 0, "Creators", False, "", False, "Killing", "Neutral", "Killing", True, ["Worker", "Elias", "Nikkiller"], [4], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jesper" : ["Jesper", True, 0, 0, "Creators", False, "", False, "Supporting", "Neutral", "Evil", True, ["Jesper", "Mafiturner", "Spy"], [1], False, False, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Johannes" : ["Johannes", True, 2, 0, "Creators", False, "", False, "Killing", "Neutral", "Killing", True, ["Johannes", "Jailwolf", "Killager"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Kristian" : ["Kristian", True, 0, 0, "Creators", False, "", False, "Protecting", "Neutral", "Evil", True, ["Kristian", "Bodyguard", "Police"], [11], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mikael" : ["Mikael", True, 0, 0, "Creators", False, "", False, "Protecting", "Neutral", "Evil", True, ["Washer", "Security_guard", "Mikael"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Ole_bjorn" : ["Ole_bjorn", True, 0, 0, "Creators", False, "", False, "Investigating", "Neutral", "Evil", True, ["Ole_bjorn", "Journalist", "Consigliere"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Oliver" : ["Oliver", True, 3, 0, "Creators", False, "", False, "Killing", "Neutral", "Killing", True, ["Oliver", "Identifier", "Pirate", "Werepup"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Snorre" : ["Snorre", True, 0, 0, "Creators", False, "", False, "Supporting", "Neutral", "Evil", True, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Assassin_dog" : ["Assassin_dog", True, 3, 0, "Dogs", False, "", False, "Killing", "Neutral", "Killing", False, ["Sniper", "Archer", "Murderer", "Assassin_dog"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Assisting_dog" : ["Assisting_dog", True, 0, 0, "Dogs", False, "", False, "Supporting", "Neutral", "Evil", True, ["Haunter", "Crazy", "Assisting_dog"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Digger" : ["Digger", True, 0, 0, "Dogs", False, "", False, "Supporting", "Neutral", "Evil", True, ["Nightmare", "Targeter", "Trapper", "Digger"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Herman" : ["Herman", True, 2, 1, "Dogs", False, "", False, "Killing", "Neutral", "Killing", True, ["Statuschecker", "Herman", "Werewolf"], [7], False, False, False, False, False, False, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Token" : ["Token", True, 1, 0, "Dogs", False, "", False, "Killing", "Neutral", "Killing", True, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Agent" : ["Agent", True, 1, 0, "FBI", False, "", False, "Killing", "Neutral", "Killing", False, ["Revengetaker", "Agent", "Gasthrower"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Agent_ZK" : ["Agent_ZK", True, 4, 1, "FBI", False, "", False, "Killing", "Neutral", "Killing", False, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Coven_hunter" : ["Coven_hunter", True, 0, 0, "FBI", True, "Coven", False, "Hunting", "Neutral", "Benign", False, HunterList, [7], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "FBI" : ["FBI", True, 7, 0, "FBI", False, "", False, "Killing", "Neutral", "Killing", False, ["FBI", "Godfather", "Dracula"], [1], False, False, False, False, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Cooler" : ["Cooler", True, 0, 0, "Freezers", False, "", False, "Supporting", "Neutral", "Evil", True, ["Sculpturer", "Waller", "Armorer", "Cooler"], [7], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0 ,[], []],
    "Eskimo" : ["Eskimo", True, 0, 0, "Freezers", False, "", False, "Protecting", "Neutral", "Evil", True, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [2], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Freezer" : ["Freezer", True, 4, 2, "Freezers", False, "", False, "Killing", "Neutral", "Killing", True, ["Tracker", "Freezer", "Ambusher"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Polar_bear" : ["Polar_bear", True, 4, 3, "Freezers", False, "", False, "Killing", "Neutral", "Killing", True, ["Token", "Agent_ZK", "Snorre", "Polar_bear"], [1], False, False, False, False, False, False, False, 0, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Sculpturer" : ["Sculpturer", True, 0, 0, "Freezers", False, "", False, "Supporting", "Neutral", "Evil", False, ["Sculpturer", "Waller", "Armorer", "Cooler"], [0], False, False, False, False, False, False, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Terrorist_hunter" : ["Terrorist_hunter", True, 0, 0, "Freezers", True, "Terrorists", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Archer" : ["Archer", True, 4, 0, "Knights", False, "", False, "Killing", "Neutral", "Killing", True, ["Sniper", "Archer", "Murderer", "Assassin_dog"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "King" : ["King", True, 0, 0, "Knights", False, "", False, "Existing", "Neutral", "Benign", False, ["General", "King", "Queen", "Crazy_king"], [1], False, False, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Knight" : ["Knight", True, 4, 3, "Knights", False, "", False, "Killing", "Neutral", "Killing", True, ["Crusader", "Serial_killer", "Knight"], [1], False, True, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Lifeguard1" : ["Lifeguard1", True, 0, 0, "Knights", False, "", False, "Protecting", "Neutral", "Benign", False, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Lifeguard2" : ["Lifeguard2", True, 0, 0, "Knights", False, "", False, "Protecting", "Neutral", "Benign", False, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Police_hunter" : ["Police_hunter", True, 0, 0, "Knights", True, "Police", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Queen" : ["Queen", True, 0, 0, "Knights", False, "", False, "Existing", "Neutral", "Benign", False, ["General", "King", "Queen", "Crazy_king"], [1], False, False, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Ambusher" : ["Ambusher", True, 1, 0, "Mafia", False, "", False, "Killing", "Mafia", "Killing", True, ["Tracker", "Freezer", "Ambusher"], [4], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Consigliere" : ["Consigliere", True, 0, 0, "Mafia", False, "", False, "Investigating", "Mafia", "Support", True, ["Ole_bjorn", "Journalist", "Consigliere"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Consort" : ["Consort", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Support", True, ["Escort", "Consort", "Thief"], [1], True, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Framer" : ["Framer", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", True, ["Framer", "Unframer", "Robber"], [4], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Godfather" : ["Godfather", True, 2, 2, "Mafia", False, "", False, "Killing", "Mafia", "Killing", False, ["FBI", "Godfather", "Dracula"], [1], False, False, False, False, True, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Hypnotist" : ["Hypnotist", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", True, ["Hypnotist", "Coven_leader", "Remover"], [0], True, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Janitor" : ["Janitor", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", True, ["Sheriff", "Investigator", "Janitor"], [0], False, False, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafioso" : ["Mafioso", True, 1, 0, "Mafia", False, "", False, "Killing", "Mafia", "Killing", True, ["Vigilante", "Terrorist", "Mafioso"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafiturner" : ["Mafiturner", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Support", True, ["Jesper", "Mafiturner", "Spy"], [7], False, False, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Murderer" : ["Murderer", True, 3, 0, "Mafia", False, "", False, "Killing", "Mafia", "Killing", True, ["Sniper", "Archer" "Murderer", "Assassin_dog"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "SK_hunter" : ["SK_hunter", True, 0, 0, "Mafia", True, "Serial_killers", False, "Hunting", "Mafia", "Support", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Unframer" : ["Unframer", True, 0, 0, "Mafia", False, "", False, "Supporting", "Mafia", "Deception", False, ["Framer", "Unframer", "Robber"], [2], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafia_hunter" : ["Mafia_hunter", True, 0, 0, "Poisoners", True, "Mafia", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Poisoner" : ["Poisoner", True, 5, 2, "Poisoners", False, "", False, "Killing", "Neutral", "Killing", True, ["Arsonist", "Poisoner", "Transporter"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Poisoner_saver" : ["Poisoner_saver", True, 6, 0, "Poisoners", False, "", False, "Protecting", "Neutral", "Evil", True, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pollutifier" : ["Pollutifier", True, 5, 0, "Poisoners", False, "", False, "Killing", "Neutral", "Killing", True, ["Doctor", "Potion_master", "Pollutifier"], [4], False, False, False, False, False, False, False, 1, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "General" : ["General", True, 0, 1, "Police", False, "", False, "Existing", "Neutral", "Benign", False, ["General", "King", "Queen", "Crazy_king"], [1], False, False, False, False, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Identifier" : ["Identifier", True, 0, 0, "Police", False, "", False, "Investigating", "Neutral", "Benign", False, ["Oliver", "Identifier", "Pirate", "Werepup"], [7], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Police" : ["Police", True, 1, 0, "Police", False, "", False, "Protecting", "Neutral", "Benign", False, ["Kristian", "Bodyguard", "Police"], [3], False, False, False, False, False, True, False, 1, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 3, [], []],
    "Sniper" : ["Sniper", True, 4, 0, "Police", False, "", False, "Killing", "Neutral", "Killing", False, ["Sniper", "Archer", "Murderer", "Assassin_dog"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Soldier" : ["Soldier", True, 4, 0, "Police", False, "", False, "Killing", "Neutral", "Killing", False, ["Stupido", "Soldier", "Huntrustiff"], [1], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Stupido_hunter" : ["Stupido_hunter", True, 0, 0, "Police", True, "Stupidos", False, "Hunting", "Neutral", "Benign", False, HunterList, [7], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Tankman" : ["Tankman", True, 5, 1, "Police", False, "", False, "Killing", "Neutral", "Killing", False, ["Suicide_bomber", "Grenadethrower", "Tankman"], [1], False, False, False, False, False, True, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crazy_hunter" : ["Crazy_hunter", True, 0, 0, "Serial_killers", True, "Crazies", False, "Hunting", "Neutral", "Evil", True, ["Crusader", "Serial_killer", "Knight"], [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Daylight_killer" : ["Daylight_killer", True, 0, 0, "Serial_killers", False, "", False, "Killing", "Neutral", "Killing", True, ["Mayor", "Dayriff", "Daylight_killer"], [1], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Nikkiller" : ["Nikkiller", True, 5, 0, "Serial_killers", False, "", False, "Killing", "Neutral", "Killing", True, ["Worker", "Elias", "Nikkiller"], [7], False, True, False, False, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Robber" : ["Robber", True, 0, 0, "Serial_killers", False, "", False, "Supporting", "Neutral", "Evil", True, ["Framer", "Unframer", "Robber"], [0], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Serial_killer" : ["Serial_killer", True, 2, 2, "Serial_killers", False, "", False, "Killing", "Neutral", "Killing", True, ["Crusader", "Serial_killer", "Knight"], [1], False, True, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Clown" : ["Clown", True, 0, 0, "Stupidos", False, "", False, "Supporting", "Neutral", "Evil", True, ["Clown", "Jester", "Nighter"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Hunter_hunter" : ["Hunter_hunter", True, 0, 0, "Stupidos", True, "", True, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Idiot" : ["Idiot", True, 0, 0, "Stupidos", False, "", False, "Supporting", "Neutral", "Evil", True, ["Librarian", "Writer", "Idiot"], [0], True, False, True, True, False, False, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Remover" : ["Remover", True, 0, 0, "Stupidos", False, "", False, "Supporting", "Neutral", "Evil", True, ["Hypnotist", "Coven_leader", "Remover"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Stupido" : ["Stupido", True, 4, 0, "Stupidos", False, "", False, "Killing", "Neutral", "Killing", True, ["Stupido", "Soldier", "Huntrustiff"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Armorer" : ["Armorer", True, 0, 0, "Terrorists", False, "", False, "Protecting", "Neutral", "Evil", True, ["Sculpturer", "Waller", "Armorer", "Cooler"], [11], False, False, False, False, False, False, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Bulleter" : ["Bulleter", True, 0, 0, "Terrorists", False, "", False, "Supporting", "Neutral", "Evil", True, ["Guardian_angel", "Incinerator", "Bulleter", "Eskimo"], [0], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Combo_hunter" : ["Combo_hunter", True, 0, 0, "Terrorists", True, "Combo", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Grenadethrower" : ["Grenadethrower", True, 5, 0, "Terrorists", False, "", False, "Killing", "Neutral", "Killing", True, ["Suicide_bomber", "Grenadethrower", "Tankman"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Suicide_bomber" : ["Suicide_bomber", True, 7, 0, "Terrorists", False, "", False, "Killing", "Neutral", "Killing", True, ["Suicide_bomber", "Grenadethrower", "Tankman"], [0], False, False, True, True, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Terrorist" : ["Terrorist", True, 4, 0, "Terrorists", False, "", False, "Killing", "Neutral", "Killing", True, ["Vigilante", "Terrorist", "Mafioso"], [7], False, True, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Bodyguard" : ["Bodyguard", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Kristian", "Bodyguard", "Police"], [3], False, False, False, False, False, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Crusader" : ["Crusader", True, 1, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Crusader", "Serial_killer", "Knight"], [3], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Dayriff" : ["Dayriff", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Mayor", "Dayriff", "Daylight_killer"], [6], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Doctor" : ["Doctor", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Doctor", "Potion_master", "Pollutifier"], [3], False, False, False, False, False, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Escort" : ["Escort", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Escort", "Consort", "Thief"], [0], True, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Haunter" : ["Haunter", True, 7, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Haunter", "Crazy", "Assisting_dog"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Huntrustiff" : ["Huntrustiff", True, 1, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Stupido", "Soldier", "Huntrustiff"], [6], False, False, False, False, True, True, False, 3, 3, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Immunist" : ["Immunist", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Immunist", "Magicmaker", "Hex_master"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Investigator" : ["Investigator", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Sheriff", "Investigator", "Janitor"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jailor" : ["Jailor", True, 7, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Jailor", "Frenzied_thrall", "Drage"], [0], False, False, True, True, True, True, False, 3, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Journalist" : ["Journalist", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Ole_bjorn", "Journalist", "Consigliere"], [6], False, False, False, False, False, True, False, 1, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Lookout" : ["Lookout", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Scared", "Vampire", "Lookout"], [3], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mayor" : ["Mayor", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Mayor", "Dayriff", "Daylight_killer"], [0], False, False, True, True, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mayorguarder" : ["Mayorguarder", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Mayorguarder", "Poisoner_saver", "Lifeguard1", "Lifeguard2"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Medium" : ["Medium", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Retributionist", "Necromancer", "Medium"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence_hunter_H" : ["Pestilence_hunter_H", True, 0, 0, "Town", True, "Pestilences", False, "Hunting", "Town", "Protective", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence_hunter_K" : ["Pestilence_hunter_K", True, 1, 0, "Town", True, "Pestilences", False, "Hunting", "Town", "Killing", False, HunterList, [6], False, False, False, False, False, True, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence_hunter_R" : ["Pestilence_hunter_R", True, 0, 0, "Town", True, "Pestilences", False, "Hunting", "Town", "Investigative", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Retributionist" : ["Retributionist", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Retributionist", "Necromancer", "Medium"], [12], False, False, True, True, True, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Revengetaker" : ["Revengetaker", True, 7, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Revengetaker", "Agent", "Gasthrower"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Security_guard" : ["Security_guard", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Washer", "Security_guard", "Mikael"], [3], True, False, True, True, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Sheriff" : ["Sheriff", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Sheriff", "Investigator", "Janitor"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Spy" : ["Spy", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Jesper", "Mafiturner", "Spy"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Statuschecker" : ["Statuschecker", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Statuschecker", "Herman", "Werewolf"], [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Tracker" : ["Tracker", True, 0, 0, "Town", False, "", False, "Investigating", "Town", "Investigative", False, ["Tracker", "Freezer", "Ambusher"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Transporter" : ["Transporter", True, 0, 0, "Town", False, "", False, "Supporting", "Town", "Support", False, ["Arsonist", "Poisoner", "Transporter"], [6], True, False, True, True, True, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Trapper" : ["Trapper", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Nightmare", "Trapper", "Targeter", "Digger"], [6], False, False, False, False, False, True, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Vampire_hunter" : ["Vampire_hunter", True, 0, 0, "Town", True, "Vampires", False, "Hunting", "Town", "Killing", False, HunterList, [6], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Veteran" : ["Veteran", True, 6, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Veteran", "Medusa", "Pestilence"], [0], False, False, True, True, True, True, False, 3, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Vigilante" : ["Vigilante", True, 3, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Vigilante", "Terrorist", "Mafioso"], [0], False, False, False, False, False, True, False, 1, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Waller" : ["Waller", True, 0, 0, "Town", False, "", False, "Protecting", "Town", "Protective", False, ["Sculpturer", "Waller", "Armorer", "Cooler"], [3], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Worker" : ["Worker", True, 8, 0, "Town", False, "", False, "Killing", "Town", "Killing", False, ["Worker", "Elias", "Nikkiller"], [0], False, False, False, False, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Dracula" : ["Dracula", True, 2, 1, "Vampires", False, "", False, "Killing", "Neutral", "Chaos", False, ["FBI", "Godfather", "Dracula"], [1], False, False, False, False, True, False, False, 3, 1, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 1, [], []],
    "Frenzied_thrall" : ["Frenzied_thrall", True, 1, 0, "Vampires", False, "", False, "Killing", "Neutral", "Chaos", True, ["Jailor", "Frenzied_thrall", "Drage"], [4], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Vampire" : ["Vampire", True, 1, 0, "Vampires", False, "", False, "Killing", "Neutral", "Chaos", True, ["Scared", "Vampire", "Lookout"], [1], False, False, False, False, False, False, False, 3, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Werewolf_hunter" : ["Werewolf_hunter", True, 0, 0, "Vampires", True, "Werewolves", False, "Hunting", "Neutral", "Chaos", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Dog_mauler" : ["Dog_mauler", True, 0, 0, "Werewolves", True, "Dogs", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Firefighter" : ["Firefighter", True, 0, 0, "Werewolves", True, "Arsonists", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Jailwolf" : ["Jailwolf", True, 4, 0, "Werewolves", False, "", False, "Killing", "Neutral", "Killing", True, ["Johannes", "Jailwolf", "Killager"], [1], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Poisoner_hunter" : ["Poisoner_hunter", True, 0, 0, "Werewolves", True, "Poisoners", False, "Hunting", "Neutral", "Evil", True, HunterList, [7], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Werepup" : ["Werepup", True, 0, 0, "Werewolves", False, "", False, "Existing", "Neutral", "Evil", True, ["Oliver", "Identifier", "Pirate", "Werepup"], [0], False, False, True, True, False, True, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Werewolf" : ["Werewolf", True, 4, 3, "Werewolves", False, "", False, "Killing", "Neutral", "Killing", True, ["Statuschecker", "Herman", "Werewolf"], [1], False, True, False, False, False, False, False, 0, 0, 2, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Drage" : ["Drage", True, 0, 0, "Dragons", False, "", False, "Killing", "Neutral", "Killing", True, ["Jailor", "Frenzied_thrall", "Drage"], [7], False, False, True, True, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Pestilence" : ["Pestilence", True, 6, 5, "Pestilences", False, "", False, "Killing", "Neutral", "Killing", True, ["Veteran", "Medusa", "Pestilence"], [1], False, False, False, False, False, False, False, 0, 0, 1, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Mafia_villager" : ["Mafia_villager", True, 0, 0, "Mafia", False, "", False, "Existing", "Mafia", "Support", True, ["Ingenting", "Mafia_villager", "Creator_villager"], [0], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Creator_villager" : ["Creator_villager", True, 0, 0, "Creators", False, "", False, "Existing", "Neutral", "Evil", True, ["Ingenting", "Mafia_villager", "Creator_villager"], [0], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []],
    "Ingenting" : ["Ingenting", True, 0, 0, "Ingenting", False, "", False, "Existing", "Neutral", "Benign", False, ["Ingenting", "Mafia_villager", "Creator_villager"], [0], False, False, False, False, False, False, False, 0, 0, 0, [], 0, [], [], [], [], False, False, False, False, False, True, 0, [], []]
    
}




    '''Dictionary that tracks the statuses of the roles during nights. Mostly resets every night. Indexes and explanation below:
0 - Votable death (if target died that night by anything that could interest Tracker or Lookout)
1 - Protected
2 - ProtectedBy (list)
3 - ProtectedImmunity
4 - Walled
5 - Bulletproof
6 - Lifeguarded
7 - LifeguardImmunity
8 - Roleblocked
9 - Cooled
10 - Pied
11 - Transported
12 - Secured
13 - Alert
14 - Ambushed
15 - Crusaded
16 - Thralled
17 - WRampaged
18 - VisitWRampaged
19 - PRampaged
20 - VisitPRampaged
21 - ERampaged
22 - VisitERampaged
23 - GRampaged
24 - VisitGRampaged
25 - Guardian-angeled
26 - Doused
27 - Framed
28 - Unframed
29 - Controlled
30 - Controlledby
31 - Hexed
32 - Stoned
33 - Cleaned
34 - Removed
35 - Hypnotized (Is int) (night number)
36 - Hypnotized by
37 - Digged
38 - Jailed
39 - Polar beared
40 - PBRampaged
41 - VisitPBRampaged
42 - Sculpted
43 - Bitten by dracula
44 - Poisoned
45 - Trapped
46 - Trapped by
47 - Huntrustiff found evil (list with True, Target)'''

    Template = [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []]

    RoleStatuses = {
    "Arsonist" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Gasthrower" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Incinerator" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Freezer_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Washer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Amnescriff" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Amneshiff" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Amnesiac" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Creator_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Guardian_angel" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Jester" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Killager" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Librarian" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Magicmaker" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Nighter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Nightmare" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Pirate" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Scared" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Survivor" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Villager" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Villargeter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Writer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Coven_leader" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "FBI_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Hex_master" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Medusa" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Necromancer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Potion_master" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Crazy" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Crazy_king" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Crazy_knight_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Targeter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Thief" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Elias" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Jesper" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Johannes" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Kristian" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mikael" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Ole_bjorn" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Oliver" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Snorre" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Assassin_dog" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Assisting_dog" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Digger" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Herman" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Token" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Agent" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Agent_ZK" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Coven_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "FBI" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Cooler" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Eskimo" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Freezer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Polar_bear" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Sculpturer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Terrorist_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Archer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "King" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Knight" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Lifeguard1" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Lifeguard2" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Police_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Queen" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Ambusher" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Consigliere" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Consort" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Framer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Godfather" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Hypnotist" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Janitor" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mafioso" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mafiturner" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Murderer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "SK_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Unframer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mafia_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Poisoner" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Poisoner_saver" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Pollutifier" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "General" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Identifier" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Police" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Sniper" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Soldier" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Stupido_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Tankman" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Crazy_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Daylight_killer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Nikkiller" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Robber" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Serial_killer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Clown" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Hunter_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Idiot" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Remover" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Stupido" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Armorer" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Bulleter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Combo_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Grenadethrower" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Suicide_bomber" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Terrorist" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Bodyguard" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Crusader" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Dayriff" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Doctor" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Escort" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Haunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Huntrustiff" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Immunist" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Investigator" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Jailor" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Journalist" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Lookout" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mayor" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mayorguarder" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Medium" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Pestilence_hunter_H" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Pestilence_hunter_K" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Pestilence_hunter_R" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Retributionist" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Revengetaker" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Security_guard" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Sheriff" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Spy" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Statuschecker" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Tracker" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Transporter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Trapper" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Vampire_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Veteran" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Vigilante" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Waller" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Worker" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Dracula" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Frenzied_thrall" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Vampire" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Werewolf_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Dog_mauler" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Firefighter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Jailwolf" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Poisoner_hunter" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Werepup" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Werewolf" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Drage" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Pestilence" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Mafia_villager" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Creator_villager" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []],
    "Ingenting" : [False, False, [], 0, False, False, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, "", False, False, False, False, False, "", False, False, False, False, False, False, False, False, False, "", []]
} 




    '''List that contains all of the roles in the game'''

    RoleList = ["Arsonist", "Gasthrower", "Incinerator", "Freezer_hunter", "Washer", "Amnescriff", "Amneshiff", "Amnesiac", "Creator_hunter",
            "Guardian_angel", "Jester", "Killager", "Librarian", "Magicmaker", "Nighter", "Nightmare", "Pirate", "Scared", "Survivor",
            "Villager", "Villargeter", "Writer", "Coven_leader", "FBI_hunter", "Hex_master", "Medusa", "Necromancer", "Potion_master",
            "Crazy", "Crazy_king", "Crazy_knight_hunter", "Targeter", "Thief", "Elias", "Jesper", "Johannes", "Kristian", "Mikael",
            "Ole_bjorn", "Oliver", "Snorre", "Assassin_dog", "Assisting_dog", "Digger", "Herman", "Token", "Agent", "Agent_ZK",
            "Coven_hunter", "FBI", "Cooler", "Eskimo", "Freezer", "Polar_bear", "Sculpturer", "Terrorist_hunter", "Archer", "King",
            "Knight", "Lifeguard1", "Lifeguard2", "Police_hunter", "Queen", "Ambusher", "Consigliere", "Consort", "Framer",
            "Godfather", "Hypnotist", "Janitor", "Mafioso", "Mafiturner", "Murderer", "SK_hunter", "Unframer", "Mafia_hunter", "Poisoner",
            "Poisoner_saver", "Pollutifier", "General", "Identifier", "Police", "Sniper", "Soldier", "Stupido_hunter", "Tankman",
            "Crazy_hunter", "Daylight_killer", "Nikkiller", "Robber", "Serial_killer", "Clown", "Hunter_hunter", "Idiot",
            "Remover", "Stupido", "Armorer", "Bulleter", "Combo_hunter", "Grenadethrower", "Suicide_bomber", "Terrorist", "Bodyguard",
            "Crusader", "Dayriff", "Doctor", "Escort", "Haunter", "Huntrustiff", "Immunist", "Investigator", "Jailor", "Journalist",
            "Lookout", "Mayor", "Mayorguarder", "Medium", "Pestilence_hunter_H", "Pestilence_hunter_K", "Pestilence_hunter_R",
            "Revengetaker", "Retributionist", "Security_guard", "Sheriff", "Spy", "Statuschecker", "Tracker", "Transporter", "Trapper",
            "Vampire_hunter", "Veteran", "Vigilante", "Waller", "Worker", "Dracula", "Frenzied_thrall", "Vampire", "Werewolf_hunter",
            "Dog_mauler", "Firefighter", "Jailwolf", "Poisoner_hunter", "Werepup", "Werewolf", "Ingenting", "Drage", "Pestilence"]


    '''Dictionary with all the teams and their respective roles. Is also used as a promotion-sequence'''

    Teams = { "Arsonists" : ["Arsonist", "Gasthrower", "Incinerator", "Freezer_hunter", "Washer"],
          "Combo" : ["Amnescriff", "Amneshiff", "Amnesiac", "Creator_hunter", "Guardian_angel", "Jester",
                    "Killager", "Librarian", "Magicmaker", "Nighter", "Nightmare", "Pirate", "Scared", "Survivor",
                    "Villager", "Villargeter", "Writer", "Ingenting"],
          "Coven" : ["Coven_leader", "FBI_hunter", "Hex_master", "Medusa", "Necromancer", "Potion_master"],
          "Crazies" : ["Crazy", "Crazy_king", "Crazy_knight_hunter", "Targeter", "Thief"],
          "Creators" : ["Elias", "Jesper", "Johannes", "Kristian", "Mikael", "Ole_bjorn", "Oliver", "Snorre", "Creator_villager"],
          "Dogs" : ["Assassin_dog", "Assisting_dog", "Digger", "Herman", "Token"],
          "FBI" : ["Agent", "Agent_ZK", "Coven_hunter", "FBI"],
          "Freezers" : ["Cooler", "Eskimo", "Freezer", "Polar_bear", "Sculpturer", "Terrorist_hunter"],
          "Knights" : ["Archer", "King", "Knight", "Lifeguard1", "Lifeguard2", "Police_hunter", "Queen"],
          "Mafia" : ["Ambusher", "Consigliere", "Consort", "Framer",
                     "Godfather", "Hypnotist", "Janitor", "Mafioso", "Mafiturner", "Murderer", "SK_hunter", "Unframer", "Mafia_villager"],
          "Poisoners" : ["Mafia_hunter", "Poisoner", "Poisoner_saver", "Pollutifier"],
          "Police" : ["General", "Identifier", "Police", "Sniper", "Soldier", "Stupido_hunter", "Tankman"],
          "Serial_killers" : ["Crazy_hunter", "Daylight_killer", "Nikkiller", "Robber", "Serial_killer"],
          "Stupidos" : ["Clown", "Hunter_hunter", "Idiot", "Remover", "Stupido"],
          "Terrorists" : ["Armorer", "Bulleter", "Combo_hunter", "Grenadethrower", "Suicide_bomber", "Terrorist"],
          "Town" : ["Bodyguard", "Crusader", "Dayriff", "Doctor", "Escort", "Haunter", "Huntrustiff", "Immunist", "Investigator", "Jailor", "Journalist",
            "Lookout", "Mayor", "Mayorguarder", "Medium", "Pestilence_hunter_H", "Pestilence_hunter_K", "Pestilence_hunter_R",
            "Revengetaker", "Retributionist", "Security_guard", "Sheriff", "Spy", "Statuschecker", "Tracker", "Transporter", "Trapper",
            "Vampire_hunter", "Veteran", "Vigilante", "Waller", "Worker"],
          "Vampires" : ["Dracula", "Frenzied_thrall", "Vampire", "Werewolf_hunter"],
          "Werewolves" : ["Dog_mauler", "Firefighter", "Jailwolf", "Poisoner_hunter", "Werewolf"],
          "Pestilences" : ["Pestilence"],
          "Dragons" : ["Drage"]
}

    '''Dictionary with the main killing roles on each team in order. Used in voting'''

    MainKillingRoles = { "Arsonists" : ["Arsonist", "Freezer_hunter"],
"Combo" : [],
"Coven" : ["Coven_leader", "Hex_master","Medusa", "Necromancer", "Potion_master", "FBI_hunter"],
"Crazies" : ["Crazy_king", "Crazy", "Targeter", "Crazy_knight_hunter"],
"Creators" : ["Johannes", "Elias", "Oliver", "Jesper", "Kristian", "Mikael", "Ole_bjorn", "Snorre", "Creator_villager"],
"Dogs" : ["Herman", "Token", "Assassin_dog"],
"FBI" : ["FBI", "Agent", "Agent_ZK", "Coven_hunter"],
"Freezers" : ["Freezer", "Terrorist_hunter"],
"Knights" : ["King", "Queen", "Knight", "Archer", "Police_hunter"],
"Mafia" : ["Godfather", "Mafioso", "Murderer", "SK_hunter"],
"Poisoners" : ["Poisoner", "Pollutifier", "Mafia_hunter"],
"Police" : ["General", "Soldier", "Sniper", "Tankman", "Police", "Identifier", "Stupido_hunter"],
"Serial_killers" : ["Serial_killer", "Daylight_killer", "Nikkiller", "Crazy_hunter"],
"Stupidos" : ["Stupido", "Hunter_hunter"],
"Terrorists" : ["Terrorist", "Grenadethrower", "Combo_hunter"],
"Town" : [],
"Vampires" : ["Dracula", "Vampire", "Werewolf_hunter"],
"Werewolves" : ["Werewolf", "Jailwolf", "Werepup", "Dog_mauler", "Firefighter", "Poisoner_hunter"],
"Pestilence" : ["Pestilence"],
"Dragons" : ["Drage"],
"Ingenting" : ["Ingenting"]

}

    ArsonistKilling = ["Arsonist"]
    CrazyKilling = ["Crazy_king", "Crazy", "Targeter"]
    DogKilling = ["Herman", "Assassin_dog", "Token"]
    FreezerKilling = ["Freezer"]
    MafiaKilling = ["Godfather", "Mafioso", "Murderer"]
    PoisonerKilling = ["Poisoner", "Pollutifier"]
    SerialKilling = ["Serial_killer", "Daylight_killer", "Nikkiller"]
    StupidoKilling = ["Stupido"]
    TerroristKilling = ["Terrorist", "Grenadethrower"]
    VampireKilling = ["Dracula", "Vampire"]
    WerewolfKilling = ["Werewolf", "Jailwolf", "Werepup"]


    AmneList = ["Amnescriff", "Amneshiff", "Amnesiac"]

    InvestList = [ "Identifier", "Journalist", "Pestilence_hunter_R", "Statuschecker", "Sheriff"]

    NonVisitList = ["Sniper", "Archer", "Murderer", "Assassin_dog"]

    GoodList = ["Town", "Police", "FBI"]

    SurvivalList = ["Creator_hunter", "Killager", "Survivor", "Villager", "Writer"]





    '''The order in which the roles perform their actions during the night'''

    Night_action_order = ["Werepup", "Herman", "Eskimo", "Lifeguard1", "Lifeguard2", "Mayorguarder", "Sculpturer", "Washer", "Cooler",
                      "Jailor", "Pirate", "Huntrustiff", "Suicide_bomber", "Assisting_dog", "Medusa",
                      "Poisoner_saver", "Veteran", "Werewolf", "Transporter", "Idiot", "Coven_leader",
                      "Hypnotist", "Security_guard", "Ambusher", "Frenzied_thrall", "Elias",
                      "Pestilence", "Polar_bear", "Werewolf", "Escort", "Consort", "Thief", "Snorre", "Clown" ,"Necromancer",
                      "Digger", "Robber", "Robber", "Amnesiac", "FBI", "General", "Haunter", "King", "Queen",
                      "Retributionist", "Armorer", "Bodyguard", "Police", "Survivor", "Vigilante", "Killager",
                      "Villager", "Villargeter", "Crusader", "Armorer", "Eskimo", "Guardian_angel", "Kristian",
                      "Mikael", "Polar_bear", "Washer", "Bodyguard", "Doctor", "Doctor", "Immunist", "Pestilence_hunter_H",
                      "Police", "Potion_master", "Trapper", "Waller", "Hypnotist", "Cooler", "Trapper", "Clown", "Bulleter", "Amnescriff", "Amneshiff",
                      "Framer", "Unframer", "Remover", "Consigliere", "Identifier", "Investigator",
                      "Journalist", "Lookout", "Ole_bjorn", "Pestilence_hunter_R", "Potion_master", "Sheriff",
                      "Spy", "Statuschecker", "Tracker", "Robber", "Arsonist", "Incinerator", "Jailor",
                      "Writer", "Hunter_hunter", "Combo_hunter", "Coven_hunter", "Crazy_hunter",
                      "Crazy_knight_hunter", "Creator_hunter", "Dog_mauler", "FBI_hunter", "Firefighter",
                      "Freezer_hunter", "Mafia_hunter", "Pestilence_hunter_H", "Pestilence_hunter_K",
                      "Pestilence_hunter_R", "Poisoner_hunter", "Police_hunter", "SK_hunter",
                      "Stupido_hunter", "Terrorist_hunter", "Vampire_hunter", "Werewolf_hunter",
                      "Worker", "Scared", "Jester", "Nikkiller", "Elias", "Drage", "Huntrustiff",
                      "Pestilence_hunter_K", "Vigilante", "Police", "Soldier", "Killager", "Librarian",
                      "Pestilence", "Pirate", "Stupido", "Herman", "Token", "Assassin_dog", "Johannes",
                      "Oliver", "Poisoner", "Hex_master", "Godfather", "Mafioso", "Murderer", "Serial_killer", "Coven_leader",
                      "Hex_master", "Medusa", "Necromancer", "Potion_master", "Dracula", "Vampire",
                      "Crazy_king", "Crazy", "Targeter", "Poisoner", "Pollutifier", "Arsonist", "Gasthrower",
                      "Freezer", "Polar_bear", "Jailwolf", "Sniper", "Tankman", "Agent", "Agent_ZK",
                      "Terrorist", "Grenadethrower", "Werewolf", "Knight", "Archer", "Robber", "Jailor",
                      "Grenadethrower", "Suicide_bomber", "Coven_leader", "Arsonist", "Incinerator", "Janitor", "Sculpturer", "Jesper",
                      "Mafiturner", "Amnescriff", "Amneshiff", "Amnesiac", "Retributionist"]




    '''Dictionary that contains the players and their roles. Will maybe not be used'''

    Players = {

    }

    PlayerNames = [
    "Alice", "Bob", "Charlie", "Daisy", "Ethan", "Fiona", "George", "Hannah", "Ian", "Jenny",
    "Kevin", "Lily", "Mike", "Nina", "Oscar", "Penny", "Quinn", "Rachel", "Sam", "Tina",
    "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Andy", "Bella", "Chris", "Diana",
    "Eli", "Faith", "Gabe", "Holly", "Jack", "Katie", "Leo", "Mia", "Nate", "Olivia",
    "Pete", "Quincy", "Rose", "Steve", "Tara", "Ulysses", "Vera", "Will", "Xena", "Yvonne",
    "Zack", "Archie", "Becky", "Cody", "Dora", "Evan", "Freya", "Gus", "Hazel", "Isaac",
    "Jade", "Kyle", "Luna", "Max", "Nora", "Owen", "Piper", "Rex", "Sophie", "Tom",
    "Una", "Vince", "Willa", "Xavier", "Yvette", "Zoe", "Alfie", "Bonnie", "Caleb", "Duke",
    "Elsa", "Finn", "Grace", "Harry", "Ivy", "Jasper", "Kara", "Liam", "Molly", "Noah",
    "Opal", "Parker", "Riley", "Seth", "Toby", "Ursula", "Violet", "Wyatt", "Ximena", "Yosef",
    "Zelda", "Axel", "Betsy", "Clark", "Dolly", "Emmett", "Faye", "Gavin", "Hope", "Jax",
    "Kiki", "Lyle", "Mabel", "Nash", "Otis", "Poppy", "Ryder", "Sky", "Tucker", "Ugo",
    "Vance", "Waldo", "Xochitl", "Yanni", "Ziggy", "Buzz", "Chloe", "Dexter", "Elmo", "Frodo",
    "Groot", "Hermione", "Indy", "Juno", "Kermit", "Loki", "Minnie", "Neo", "Peppa", "Rocket",
    "Snoreham", "Haides_Zenon_Ab", "Aidon", "Nariman", "Jon_Snow", "KarlMikaelPerfekt", "Jhah",
    "Gondonk", "Henrik", "Dampskipsundervannsstyrkeprovemaskinerikonstruksjonsvanskeligheter"
]


    '''The sequence of the players and their roles in game. The lists are in the same order'''

    PlayerSequence = []
    RoleSequence = []

    PromoteList = [] #This list stores tuples that are supposed to be ran into the PromoteSpecific-function

    VoteList = [] #List that stores the people that are supposed to be voted out. Stores the information in tuples, (Player to be voted, Accuser, Role of accuser)
    VoteList2 = [] #Used for printing

    TurnList = [] #List of players supposed to be turned into vampires. Tuple with (Player, 36)

WinnerList = []



def FindIndex(Role): #Finds the index of the Role in Rolesequence
    if Role not in RoleSequence:
        return None
    else:
        return RoleSequence.index(Role)
    
def isInGame(Role, Alive = False, Real = False): #Checks if the given role is in the game. Alive = True -- Only returns True if role is also alive
                                 #Real = True -- Will ignore amne-roles 
    if not Real:
        if not Alive:
            for role in RoleSequence:
                if RoleStats[role][0] == Role:
                    return True
            return False
        else:
            for role in RoleSequence:
                if RoleStats[role][0] == Role and RoleStats[role][1]:
                    return True
            return False
    else:
        if not Alive:
            for role in RoleSequence:
                if RoleStats[role][0] == Role and role not in AmneList:
                    return True
            return False
        else:
            for role in RoleSequence:
                if RoleStats[role][0] == Role and RoleStats[role][1] and role not in AmneList:
                    return True
            return False
    
def LinkRoles(Role, number = None, Real = False, Amne = 0): #Finds out which "Player" a role is currently linked to. If multiple, returns the first one
    '''
    number is for when you want to check if a specific index is true
    Real is for if you want the role to not be an amne-role
    1 - Amnescriff
    2 - Amneshiff
    3 - Amnesiac
    '''
    if Real:
        for role in RoleSequence:
            if RoleStats[role][0] == Role and role not in AmneList and number == None:
                return role
            elif RoleStats[role][0] == Role and role not in AmneList and RoleStats[role][number]:
                return role
    else:
        for role in RoleSequence:
            if RoleStats[role][0] == Role:
                return role
            
def CheckMajority(Team): #Checks if the given team has an objective majority - 1, majority - 0, or not at all - None
    TeamCount = 0
    NonCount = 0
    RoleList = CreateCurrentRoleList()
    for role in RoleList:
        if RoleStats[role][4] == Team and RoleStats[role][4] != "Town" and RoleStats[role][4] != "Combo" and RoleStats[role][0] != "Murderer":
            TeamCount += 1
        else:
            NonCount += 1
    if Team == "Mafia":
        TeamCount += MafiaContactMurderer()
        NonCount -= MafiaContactMurderer()
    if NonCount > TeamCount:
        return None
    elif NonCount == TeamCount:
        return 0
    else:
        return 1

def AlivePlayers(): #Returns a list of the players in RoleSequence that are still alive
    AliveList = []
    for role in RoleSequence:
        if RoleStats[role][1]:
            AliveList.append(role)
    return AliveList

def InactiveHunter(Hunter): #Takes in a hunter and returns True if that hunter has no one to hunt.
    if RoleStats[Hunter][0] == "Hunter_hunter":
        for role in RoleSequence:
            if RoleStats[role][5] and RoleStats[role][1]:
                return False
    else:
        for role in RoleSequence:
            if RoleStats[role][4] == RoleStats[Hunter][6] and RoleStats[role][1]:
                return False
    return True

def CreateCurrentRoleList(): #Creates a list of the current alive active roles in the game (RoleStats[Role][0])
    CurrentRoleList = []
    for role in RoleSequence:
        if RoleStats[role][1]:
            CurrentRoleList.append(RoleStats[role][0])
    return CurrentRoleList

def CreateNewRoleList(Role):
    '''
    Creates and returns the RoleSequence, but reordered so that Role is first.
    '''
    NewRoleList = []
    if FindIndex(Role) == 0:
        NewRoleList = RoleSequence
    else:
        for i in range(FindIndex(Role), len(RoleSequence)):
            NewRoleList.append(RoleSequence[i])
        for i in range(0, FindIndex(Role)):
            NewRoleList.append(RoleSequence[i])
    
    return NewRoleList
    
def CreateTeamList(): #Creates a list of the teams that are currently alive in the game
    RoleList = AlivePlayers()
    TeamList = []
    for role in RoleList:
        if RoleStats[role][4] not in TeamList:
            TeamList.append(RoleStats[role][4])
    return TeamList

def AmountTeam(Team): #Returns the number of alive players on the given team
    AliveList = AlivePlayers()
    ct = 0
    for role in AliveList:
        if RoleStats[role][4] == Team:
            ct += 1
    return ct

def MafiaContactMurderer():
    '''
    Checks how many Murderers has contact with at least one mafia-member
    Mostly used for voting and majority-purposes
    '''
    Count = 0
    AliveList = AlivePlayers()
    for player in AliveList:
        if RoleStats[player][0] == "Murderer" and len(RoleStats[player][28]) != 0:
            Count += 1
    return Count

def PromoteSpecific(Role, NewRole): #Promotes a specific role to a new role
    for i in range(0,39):
        if i != 27:
            RoleStats[Role][i] = copy.deepcopy(TotalRoleStats[NewRole][i])
    if RoleStats[Role][4] == "Mafia":
        RoleStats[Role][35] = False
    elif HasTeammate(Role):
        RoleStats[Role][35] = False
    if RoleStats[Role][0] == "Vampire" and Role in AmneList:
        RoleStats[Role][36] = 3 - AmneList.index(Role)
    elif RoleStats[Role][0] == "Guardian_angel":
        FindTargetGA(Role)
    elif RoleStats[Role][0] == "Librarian":
        FindTargetLib(Role)
    elif RoleStats[Role][0] == "Identifier":
        CreateListIdentifier(Role)

def CheckRoleblock(Role):
    '''
    Checks if there is anything preventing the Role from performing its action
    In that case, it will return True, otherwise False
    '''
    if RoleStatuses[Role][8]:
        return True
    
    return False

def CheckAction(Role, Target): #Checks the most common checks after ExecuteTarget. To save time
    if Target != None and RoleStats[Role][1] and not CheckRoleblock(Role):
        return True
    return False

def HasTeammate(Role): #Checks if the given role has a teammate in the game
    if RoleStats[Role][4] == "Town" or RoleStats[Role][4] == "Combo":
        return False
    for role in RoleSequence:
        if RoleStats[role][4] == RoleStats[Role][4] and role != Role:
            return True
    return False

def Neighbor(Role, Direction):
    '''
    Returns the neighbor of the given role, alive or dead.
    Direction indicates on which side (right or left)
    '''
    Index = RoleSequence.index(Role)
    if Direction == "right":
        if Index == len(RoleSequence)-1:
            Player = RoleSequence[0]
        else:
            Player = RoleSequence[Index+1]
    elif Direction == "left":
        if Index == 0:
            Player = RoleSequence[-1]
        else:
            Player = RoleSequence[Index-1]
    return Player

def CheckFramed(Role):
    '''
    Takes in a role and returns True if that role will show up as framed (unframer included)
    '''
    if RoleStatuses[Role][27] and not RoleStatuses[Role][28]:
        return True
    return False

def LinkPerson(Role): #Links a ROLE up to the person (player name) with that role
    return PlayerSequence[RoleSequence.index(Role)]

def UpdateYoungest(): #Updates who is the current youngest vampire (the one that should bite)
    '''
    Vampire-info:
    21 - Nights until dying of hunger
    22 - Countdown used for when you are allowed to bite
    23 - Usual
    43 - Dracula-bitten or not (statuses)
    36 - Youngest-number
    Original vampire has Youngest-number 4. 1,2,3 is reserved for potential Amne
    '''
    Current = ""
    for role in RoleSequence:
        RoleStats[role][31] = False
        if RoleStats[role][1] and RoleStats[role][0] == "Vampire" and not RoleStatuses[role][43]:
            if Current == "" or RoleStats[role][36] > RoleStats[Current][36]:
                Current = role

    if Current == "":
        for role in RoleSequence:
            RoleStats[role][31] = False
            if RoleStats[role][1] and RoleStats[role][0] == "Vampire":
                if Current == "" or RoleStats[role][36] > RoleStats[Current][36]:
                    Current = role
    if Current != "":
        RoleStats[Current][31] = True

def FindTargetGA(Role): #Finds a target for guardian angel
    FindTarget(Role, [0])
    Target = RoleStats[Role][26][0]
    RoleStats[Role][26] = []
    RoleStats[Role][24] = [Target]
    
def FindTargetLib(Role): #Finds a target for librarian
    if RoleSequence[0] != Role:
        RoleStats[Role][24] = [RoleSequence[0]]
    else:
        RoleStats[Role][24] = [RoleSequence[1]]

def CreateListIdentifier(Role): #Creates list of list in 38 for identifier
    for role in RoleSequence:
        RoleStats[Role][38].append([role, 0])

def Control(Role): #Returns true if the given Role is controlled in any way
    if RoleStatuses[Role][29] or (RoleStatuses[Role][35] != False and RoleStatuses[Role][35] < Night):
        return True
    return False


def AppendToVoteList():
    for role in RoleSequence:
        if not RoleStatuses[role][34] and RoleStats[role][1]:

            if RoleStats[role][0] == "Huntrustiff" and RoleStatuses[role][47] != [] and (RoleStats[RoleStatuses[role][47][1]][4] != RoleStats[role][4] or (CheckFramed(RoleStatuses[role][47][1]) and RoleStats[role][4] != "Mafia")) and RoleStats[RoleStatuses[role][47][1]][1]:
                VoteList.append((RoleStatuses[role][47][1], LinkPerson(role), RoleStats[role][0]))
                VoteList2.append((RoleStatuses[role][47][1], LinkPerson(role), RoleStats[role][0]))

            elif RoleStats[role][0] == "Identifier" and RoleStats[role][34] and (RoleStats[RoleStats[role][26][0]][4] != RoleStats[role][4] or (CheckFramed(RoleStats[role][26][0]) and RoleStats[role][4] != "Mafia")) and RoleStats[RoleStats[role][36][0]][1]:
                VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                RoleStats[role][34] = False
            elif RoleStats[role][0] == "Identifier":
                RoleStats[role][34] = False

            elif RoleStats[role][0] == "Journalist" and RoleStats[role][34] and (RoleStats[RoleStats[role][26][0]][4] != RoleStats[role][4] or (CheckFramed(RoleStats[role][26][0]) and RoleStats[role][4] != "Mafia")) and RoleStats[RoleStats[role][36][0]][1]:
                VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                RoleStats[role][34] = False
            elif RoleStats[role][0] == "Journalist":
                RoleStats[role][34] = False

            elif RoleStats[role][0] == "Lookout" and RoleStats[role][29] != []:
                Target = RoleStats[role][36][0]
                if not RoleStats[Target][1] and RoleStatuses[Target][0] and len(RoleStats[role][29]) == 2 and RoleStats[RoleStats[role][29][1]][4] != RoleStats[role][4] and RoleStats[RoleStats[role][36][0]][1]:
                    VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                    VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))

            elif RoleStats[role][0] == "Pestilence_hunter_R" and RoleStats[role][34] and (RoleStats[RoleStats[role][26][0]][4] != RoleStats[role][4] or (CheckFramed(RoleStats[role][26][0]) and RoleStats[role][4] != "Mafia")) and RoleStats[RoleStats[role][36][0]][1]:
                VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                RoleStats[role][34] = False
            elif RoleStats[role][0] == "Pestilence_hunter_R":
                RoleStats[role][34] = False

            elif RoleStats[role][0] == "Sheriff" and RoleStats[role][34] and (RoleStats[RoleStats[role][26][0]][4] != RoleStats[role][4] or (CheckFramed(RoleStats[role][26][0]) and RoleStats[role][4] != "Mafia")) and RoleStats[RoleStats[role][36][0]][1]:
                VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                RoleStats[role][34] = False
            elif RoleStats[role][0] == "Sheriff":
                RoleStats[role][34] = False

            elif RoleStats[role][0] == "Statuschecker" and RoleStats[role][34] and (RoleStats[RoleStats[role][26][0]][4] != RoleStats[role][4] or (CheckFramed(RoleStats[role][26][0]) and RoleStats[role][4] != "Mafia")) and RoleStats[RoleStats[role][36][0]][1]:
                VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                RoleStats[role][34] = False
            elif RoleStats[role][0] == "Statuschecker":
                RoleStats[role][34] = False

            elif RoleStats[role][0] == "Tracker" and RoleStats[role][29] != [] and RoleStats[RoleStats[role][36][0]][4] != RoleStats[role][4]:
                if len(RoleStats[role][29]) == 2 and not RoleStats[RoleStats[role][29][1]][1] and RoleStatuses[RoleStats[role][29][1]][0] and RoleStats[RoleStats[role][36][0]][1]:
                    VoteList.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))
                    VoteList2.append((RoleStats[role][36][0], LinkPerson(role), RoleStats[role][0]))

def GiveNecronomicon():
    for role in RoleSequence:
        if RoleStats[role][33]:
            if RoleStats[role][1]:
                return
            else:
                RoleStats[role][33] = False
                break
    for role in MainKillingRoles["Coven"]:
        if role != "FBI_hunter":
            if isInGame(role, True, True):
                RoleStats[role][33]= True
                return
            elif isInGame(role, True):
                for Amne in AmneList:
                    if RoleStats[Amne][0] == role:
                        RoleStats[Amne][33] = True
                        return
                    
        

def ResetGame(): #Resets all players after a night
    global ERampageTrigger, WRampageTrigger, PRampageTrigger, GRampageTrigger, PBRampageTrigger, PoisonerSaver, Snorre, AssistingDog, Jester, Bulleter
    for role in RoleSequence:
        ResetPlayer(role)
        if RoleStats[role][0] == "Drage" and RoleStats[role][34]:
            RoleStats[role][2] = 0
            RoleStats[role][3] = 0
            RoleStats[role][34] = False
        if RoleStats[role][0] == "Elias" and RoleStats[role][2] != 0:
            RoleStats[role][2] = 0
            RoleStats[role][3] = 0 
    ERampageTrigger = False
    WRampageTrigger = False
    PRampageTrigger = False
    GRampageTrigger = False
    PBRampageTrigger = False
    PoisonerSaver = False
    Snorre = False
    Jester = False
    AssistingDog = False
    Bulleter = False


def ResetEntirely():
    global CPUGame, Nightmare, NightmareTrigger, ERampageTrigger, WRampageTrigger, PRampageTrigger, GRampageTrigger, PBRampageTrigger, PoisonerSaver, Snorre, PlayersAlive, DrawCount, Night, Day, Jester, AssistingDog, Bulleter, PlayerRevived, Win, PestilenceInGame, DrageTrigger, RoleStats, VoteList, PromoteList, TurnList
    '''
    Resets the entire game to scratch. Used for playing multiple times in a row
    ''' 
    CPUGame = True
    NightmareTrigger = False
    Nightmare = False
    ERampageTrigger = False
    WRampageTrigger = False
    PRampageTrigger = False
    GRampageTrigger = False
    PBRampageTrigger = False
    PoisonerSaver = False
    Snorre = False
    PlayersAlive = 0
    DrawCount = 0
    PlayerRevived = False
    Day = 1
    Night = 0
    Win = False
    Jester = False
    AssistingDog = False
    Bulleter = False
    PestilenceInGame = False
    DrageTrigger = 0
    VoteList = []
    TurnList = []
    PromoteList = []
    RoleStats = copy.deepcopy(TotalRoleStats)
    for i in RoleStatuses.keys():
        RoleStatuses[i] = copy.deepcopy(Template)

def ResetPlayer(Role): #Resets the given player
    RoleStats[Role][23] = TotalRoleStats[RoleStats[Role][0]][23]
    RoleStats[Role][25] = 0
    RoleStats[Role][26] = []
    RoleStats[Role][29] = []
    NonResetList = [0, 9, 10, 25, 26, 32, 33, 35, 36, 42, 43, 44, 45, 46]
    for i in range(0,48):
        if i not in NonResetList:
            RoleStatuses[Role][i] = copy.deepcopy(Template[i])

def runDay(): #Runs the day
    global PestilenceInGame
    global Nightmare
    global NightmareTrigger
    global Day
    global VoteList2
    global PlayersAlive
    global DrawCount
    global PlayerRevived
    Check = PestilenceInGame
    PestilenceInGame = False
    Day += 1
    print(f"Day {Day}")
    if (not DebugGame):
        input()
    AliveList = AlivePlayers()
    if PlayersAlive == len(AliveList) and PlayerRevived == False:
        DrawCount += 1
    else:
        PlayersAlive = len(AliveList)
        DrawCount = 0
    PlayerRevived = False


    if isInGame("Pestilence"):
        PestilenceInGame = True
    
    if Check and not PestilenceInGame:
        for role in RoleSequence:
            if RoleStats[role][0] == "Pestilence_hunter_R":
                RoleStats[role][24] = []

    if DrawCount == 6:
        endGame("Draw")

    for role in RoleSequence:
        if RoleStats[role][0] == "Librarian" and not RoleStats[RoleStats[role][24][0]][1]:
            RoleStats[role][3] = 0

    if CPUGame:
        Nightmare = False
        if isInGame("Daylight_killer", True, True):
            Daylight_killer_F(LinkRoles("Daylight_killer", None, True))
        for Amne in AmneList:
            if RoleStats[Amne][0] == "Daylight_killer":
                Daylight_killer_F(Amne)

        Promote()
        WinCheck()
        if Win:
            return
        if isInGame("Mayor", True, True):
            Mayor_F(LinkRoles("Mayor", None, True))

        Promote()
        WinCheck()
        if Win:
            return
        if isInGame("Dayriff", True, True):
            Dayriff_F(LinkRoles("Dayriff", None, True))
        for Amne in AmneList:
            if RoleStats[Amne][0] == "Dayriff":
                Dayriff_F(Amne)

        for vote in VoteList2:
            print(f"{vote[1]} claims {vote[2]} and accuses {LinkPerson(vote[0])} ({RoleStats[vote[0]][0]}) of treason!")
        VoteList2 = []

        runVote()
            
        Promote()
        WinCheck()
        if NightmareTrigger:
            Nightmare = True
            NightmareTrigger = False
        
        for role in RoleSequence:
            RoleStatuses[role][25] = False
    

def runNight(): 
    global Night
    Night += 1
    print(f"Night {Night}")
    if Night >= 3:
        GiveNecronomicon()
    UpdateYoungest()
    AliveList = AlivePlayers()
    for action in Night_action_order:
        actionF = action + "_F" 
        for role in RoleSequence:
            if role not in AmneList and RoleStats[role][0] == action:
                globals()[actionF](role)
        for Amne in AmneList:
            if RoleStats[Amne][0] == action and Amne in RoleSequence:
                globals()[actionF](Amne)
    AppendToVoteList()
    ResetGame()


def RunTurn(): #Turns players into vampires based on turnlist
    global TurnList
    for turn in TurnList:
        for i in range(0, 39):
            if i != 22 and i != 26 and i != 27 and i != 34 and RoleStats[turn[0]][1]:
                RoleStats[turn[0]][i] = copy.deepcopy(TotalRoleStats["Vampire"][i])
        RoleStats[turn[0]][36] = turn[1]
    TurnList = []


def runVote():
    global VoteList
    print("Running vote")
    if CPUGame:
        TeamList = CreateTeamList()

        if all(CheckMajority(team) != 1 for team in TeamList):
            print("Trying to vote from votelist")
            for vote in VoteList:
                if RoleStats[vote[0]][1] and RoleStatuses[vote[0]][25] == False and CheckMajority(RoleStats[vote[0]][4]) == None:
                    #print(f"{vote[1]} claims {vote[2]} and accuses {LinkPerson(vote[0])} ({vote[0]}) of being evil!")
                    Attack(None, vote[0], False, False, False, False, False, True)
                    VoteList.remove(vote)
                    break
                elif RoleStats[vote[0]][1] and RoleStatuses[vote[0]][25] == False:
                    return
        else:
            print("A team has majority")
            Majority = ""
            MainKilling = ""
            RoleList = CreateCurrentRoleList()
            for team in TeamList:
                if CheckMajority(team) == 1:
                    Majority = team
                    break
            for role in MainKillingRoles[Majority]:
                if isInGame(role, True, True):
                    MainKilling = LinkRoles(role, None, True)
                    break
                elif isInGame(role, True):
                    for amne in AmneList:
                        if RoleStats[amne][0] == role:
                            MainKilling = amne
                            break
            NextList = []
            print(MainKilling)
            FindTarget(MainKilling, [7], NextList)
            Target = RoleStats[MainKilling][26][0]
            while True:
                print(f"Trying to vote {Target}")
                if Target == 1:
                    return
                if RoleStatuses[RoleStats[MainKilling][26][0]][25] == False:
                    print(f"{Majority} has majority and votes {RoleStats[MainKilling][26][0]}")
                    Attack(None, RoleStats[MainKilling][26][0], False, False, False, False, False, True)
                    RoleStats[MainKilling][26] = []
                    break
                else:
                    NextList.append(RoleStats[MainKilling][26][0])
                    RoleStats[MainKilling][26] = []
                    FindTarget(MainKilling, [7], NextList)
        

def Promote():
    global PromoteList
    '''
    Handles promotion. Goes through all the roles and promotes if necessary.
    '''
    RoleList = CreateCurrentRoleList()
    AliveList = AlivePlayers()
    for role in AliveList:
        if role not in AmneList:
            if RoleStats[role][0] == "Vampire_hunter" and InactiveHunter(role):
                PromoteList.append((role, "Vigilante"))

            elif RoleStats[role][0] == "Lifeguard1" and "King" not in RoleList:
                PromoteList.append((role, "King"))

            elif RoleStats[role][0] == "Lifeguard2" and "Queen" not in RoleList:
                PromoteList.append((role, "Queen"))

            elif RoleStats[role][0] == "Stupido_hunter" and "Soldier" not in RoleList and "Sniper" not in RoleList and "Tankman" not in RoleList:
                PromoteList.append((role, "Soldier"))

            elif RoleStats[role][0] == "Creator_hunter" and InactiveHunter(role):
                PromoteList.append((role, "Villager"))

            elif RoleStats[role][0] == "Coven_hunter" and InactiveHunter(role) and "FBI" not in RoleList:
                PromoteList.append((role, "FBI"))

            elif RoleStats[role][0] == "Mayorguarder" and "Mayor" not in RoleList:
                PromoteList.append((role, "Bodyguard"))

            elif RoleStats[role][0] == "FBI_hunter" and InactiveHunter(role) and "Coven_leader" not in RoleList:
                PromoteList.append((role, "Coven_leader"))

            elif RoleStats[role][0] == "Police_hunter" and InactiveHunter(role) and "Knight" not in RoleList:
                PromoteList.append((role, "Knight"))

            elif RoleStats[role][0] == "Pollutifier" and RoleStats[role][21] == 0 and "Poisoner" not in RoleList:
                PromoteList.append((role, "Poisoner"))
                    
    for i in PromoteList:
        PromoteSpecific(i[0], i[1])
        if i[1] == "Vigilante":
            RoleStats[i[0]][21] = 0
        if i[1] == "Villager":
            RoleStats[i[0]][21] = 0
        if i[1] == "Bodyguard":
            RoleStats[i[0]][21] = 0
    PromoteList = []




    RoleList = CreateCurrentRoleList()
    
    for role in AliveList:
        if role in AmneList:
            if RoleStats[role][0] == "Vampire_hunter" and InactiveHunter(role):
                PromoteList.append((role, "Vigilante"))

            elif RoleStats[role][0] == "Lifeguard1" and "King" not in RoleList:
                PromoteList.append((role, "King"))

            elif RoleStats[role][0] == "Lifeguard2" and "Queen" not in RoleList:
                PromoteList.append((role, "King"))

            elif RoleStats[role][0] == "Stupido_hunter" and "Soldier" not in RoleList:
                PromoteList.append((role, "Soldier"))

            elif RoleStats[role][0] == "Creator_hunter" and InactiveHunter(role):
                PromoteList.append((role, "Villager"))

            elif RoleStats[role][0] == "Coven_hunter" and InactiveHunter(role) and "FBI" not in RoleList:
                PromoteList.append((role, "FBI"))

            elif RoleStats[role][0] == "Mayorguarder" and "Mayor" not in RoleList:
                PromoteList.append((role, "Bodyguard"))

            elif RoleStats[role][0] == "Police_hunter" and InactiveHunter(role) and "Knight" not in RoleList:
                PromoteList.append((role, "Knight"))

            elif RoleStats[role][0] == "Pollutifier" and RoleStats[role][21] == 0 and "Poisoner" not in RoleList:
                PromoteList.append((role, "Poisoner"))


            for i in PromoteList:
                PromoteSpecific(i[0], i[1])
                if i[1] == "Vigilante":
                    RoleStats[i[0]][21] = 0
                if i[1] == "Villager":
                    RoleStats[i[0]][21] = 0
                if i[1] == "Bodyguard":
                    RoleStats[i[0]][21] = 0
        
    PromoteList = []

    RoleList = CreateCurrentRoleList()
    
    NonPromotionList = ["Town", "Police", "Creators", "FBI", "Combo", "Knights", "Coven", "Pestilence", "Dragons"]
    TeamList = CreateTeamList()
    for team in TeamList:
        if team not in NonPromotionList:
            if team == "Arsonists":
                if all(player not in RoleList for player in ArsonistKilling):
                    if isInGame("Freezer_hunter", True, True) and InactiveHunter(LinkRoles("Freezer_hunter", None, True)):
                        PromoteList.append((LinkRoles("Freezer_hunter", None, True), "Arsonist"))
                    elif isInGame("Freezer_hunter", True) and InactiveHunter(LinkRoles("Freezer_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Freezer_hunter":
                                PromoteList.append((Amne, "Arsonist"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in ArsonistKilling and role != "Freezer_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Arsonist"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Arsonist"))
                                            break
                                    break

            elif team == "Crazies":
                if all(player not in RoleList for player in CrazyKilling):
                    if isInGame("Crazy_knight_hunter", True, True) and InactiveHunter(LinkRoles("Crazy_knight_hunter", None, True)):
                        PromoteList.append((LinkRoles("Crazy_knight_hunter", None, True), "Crazy"))
                    elif isInGame("Crazy_knight_hunter", True) and InactiveHunter(LinkRoles("Crazy_knight_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Crazy_knight_hunter":
                                PromoteList.append((Amne, "Crazy"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in CrazyKilling and role != "Crazy_knight_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Crazy"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Crazy"))
                                            break
                                    break

            elif team == "Dogs":
                if all(player not in RoleList for player in DogKilling):
                    for role in Teams[team]:
                        if role not in DogKilling:
                            if isInGame(role, True, True):
                                PromoteList.append((LinkRoles(role, None, True), "Herman"))
                                break
                            elif isInGame(role, True):
                                for Amne in AmneList:
                                    if RoleStats[Amne][0] == role:
                                        PromoteList.append((Amne, "Herman"))
                                        break
                                break

            elif team == "Freezers":
                if all(player not in RoleList for player in FreezerKilling):
                    if isInGame("Terrorist_hunter", True, True) and InactiveHunter(LinkRoles("Terrorist_hunter", None, True)):
                        PromoteList.append((LinkRoles("Terrorist_hunter", None, True), "Freezer"))
                    elif isInGame("Terrorist_hunter", True) and InactiveHunter(LinkRoles("Terrorist_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Terrorist_hunter":
                                PromoteList.append((Amne, "Freezer"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in FreezerKilling and role != "Terrorist_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Freezer"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Freezer"))
                                            break
                                    break

            elif team == "Mafia":
                if all(player not in RoleList for player in MafiaKilling):
                    if isInGame("SK_hunter", True, True) and InactiveHunter(LinkRoles("SK_hunter", None, True)):
                        PromoteList.append((LinkRoles("SK_hunter", None, True), "Mafioso"))
                    elif isInGame("SK_hunter", True) and InactiveHunter(LinkRoles("SK_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "SK_hunter":
                                PromoteList.append((Amne, "Mafioso"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in MafiaKilling and role != "SK_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Mafioso"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Mafioso"))
                                            break
                                    break

            elif team == "Poisoners":
                if all(player not in RoleList for player in PoisonerKilling):
                    if isInGame("Mafia_hunter", True, True) and InactiveHunter(LinkRoles("Mafia_hunter", None, True)):
                        PromoteList.append((LinkRoles("Mafia_hunter", None, True), "Poisoner"))
                    elif isInGame("Mafia_hunter", True) and InactiveHunter(LinkRoles("Mafia_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Mafia_hunter":
                                PromoteList.append((Amne, "Poisoner"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in PoisonerKilling and role != "Mafia_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Poisoner"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Poisoner"))
                                            break
                                    break

            elif team == "Serial_killers":
                if all(player not in RoleList for player in SerialKilling):
                    if isInGame("Crazy_hunter", True, True) and InactiveHunter(LinkRoles("Crazy_hunter", None, True)):
                        PromoteList.append((LinkRoles("Crazy_hunter", None, True), "Serial_killer"))
                    elif isInGame("Crazy_hunter", True) and InactiveHunter(LinkRoles("Crazy_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Crazy_hunter":
                                PromoteList.append((Amne, "Serial_killer"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in SerialKilling and role != "Crazy_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Serial_killer"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Serial_killer"))
                                            break
                                    break

            elif team == "Stupidos":
                if all(player not in RoleList for player in StupidoKilling):
                    if isInGame("Hunter_hunter", True, True) and InactiveHunter(LinkRoles("Hunter_hunter", None, True)):
                        PromoteList.append((LinkRoles("Hunter_hunter", None, True), "Stupido"))
                    elif isInGame("Hunter_hunter", True) and InactiveHunter(LinkRoles("Hunter_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Hunter_hunter":
                                PromoteList.append((Amne, "Stupido"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in StupidoKilling and role != "Hunter_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Stupido"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Stupido"))
                                            break
                                    break

            elif team == "Terrorists":
                if all(player not in RoleList for player in TerroristKilling):
                    if isInGame("Combo_hunter", True, True) and InactiveHunter(LinkRoles("Combo_hunter", None, True)):
                        PromoteList.append((LinkRoles("Combo_hunter", None, True), "Terrorist"))
                    elif isInGame("Combo_hunter", True) and InactiveHunter(LinkRoles("Combo_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Combo_hunter":
                                PromoteList.append((Amne, "Terrorist"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in TerroristKilling and role != "Combo_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Terrorist"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Terrorist"))
                                            break
                                    break

            elif team == "Vampires":
                if all(player not in RoleList for player in VampireKilling):
                    if isInGame("Werewolf_hunter", True, True) and InactiveHunter(LinkRoles("Werewolf_hunter", None, True)):
                        PromoteList.append((LinkRoles("Werewolf_hunter", None, True), "Vampire"))
                    elif isInGame("Werewolf_hunter", True) and InactiveHunter(LinkRoles("Werewolf_hunter")):
                        for Amne in AmneList:
                            if RoleStats[Amne][0] == "Werewolf_hunter":
                                PromoteList.append((Amne, "Vampire"))
                                break
                    else:
                        for role in Teams[team]:
                            if role not in VampireKilling and role != "Werewolf_hunter":
                                if isInGame(role, True, True):
                                    PromoteList.append((LinkRoles(role, None, True), "Vampire"))
                                    break
                                elif isInGame(role, True):
                                    for Amne in AmneList:
                                        if RoleStats[Amne][0] == role:
                                            PromoteList.append((Amne, "Vampire"))
                                            break
                                    break

            elif team == "Werewolves":
                if all(player not in RoleList for player in WerewolfKilling):
                    for role in Teams[team]:
                        if role not in WerewolfKilling:
                            if isInGame(role, True, True) and InactiveHunter(LinkRoles(role, None, True)):
                                PromoteList.append((LinkRoles(role, None, True), "Werewolf"))
                                break
                            elif isInGame(role, True) and InactiveHunter(LinkRoles(role)):
                                for Amne in AmneList:
                                    if RoleStats[Amne][0] == role:
                                        PromoteList.append((Amne, "Crazy"))
                                        break
                                break
    if "Elias" not in RoleList and "Oliver" not in RoleList and "Johannes" not in RoleList:
        if AmountTeam("Creators") == 1:
            for role in RoleList:
                if RoleStats[role][4] == "Creators":
                    PromoteList.append((role, "Johannes"))
                    break
    for i in PromoteList:
        PromoteSpecific(i[0], i[1])
    PromoteList = []


def WinCheck():
    global DrawCount
    '''
    Checks if a team has won the game or if the game has ended in a draw
    '''
    AliveList = CreateCurrentRoleList()
        
    if len(AliveList) == 0:
        endGame("Draw")

    elif all((RoleStats[role][4] == "Combo" or RoleStats[role][4] == "Ingenting") for role in AliveList):
        endGame("Draw")

    elif len(AliveList) <= 2 and "General" in AliveList:
        endGame("Police")

    elif len(AliveList) == 2 and "Godfather" in AliveList and "Serial_killer" in AliveList:
        endGame("Serial_killers")

    elif len(AliveList) <= 3 and ("Queen" in AliveList or "King" in AliveList):
        endGame("Knights")

    elif len(AliveList) <= 4 and "Queen" in AliveList and "King" in AliveList:
        endGame("Knights")

    elif len(AliveList) == 1:
        endGame(RoleStats[AliveList[0]][4])

    else:
        TeamList = []
        GoodList = ["Town", "Police", "FBI"]
        for role in AliveList:
            if RoleStats[role][4] != "Combo" and RoleStats[role][4] != "Ingenting":
                TeamList.append(RoleStats[role][4])
        
        if all(element == TeamList[0] for element in TeamList):
            endGame(TeamList[0])

        elif all(element in GoodList for element in TeamList):
            endGame("Town")

        return
    
    return
 

def endGame(Winner):
    global Win
    Win = True
    global winDictTeam
    if Winner in winDictTeam:
        winDictTeam[Winner] += 1
    else:
        winDictTeam[Winner] = 1
    GoodList = ["Town", "Police", "FBI"]
    WinList = []
    if Winner == "Draw":
        print("The game is a draw")
        if (not DebugGame):
            input()
    else:
        print(f"The game is over! {Winner} won!")
        if (not DebugGame):
            input()
        if Winner == "Town":
            for role in RoleSequence:
                if RoleStats[role][4] in GoodList:
                    WinList.append(RoleStats[role][0])
        else:
            for role in RoleSequence:
                if RoleStats[role][4] == Winner:
                    WinList.append(RoleStats[role][0])
        print("The following won:")
        for win in WinList:
            print(win)
        if (not DebugGame):
            input()
    ConditionWinList = []
    for role in RoleSequence:
        if RoleStats[role][30]:
            ConditionWinList.append(RoleStats[role][0])

    for role in RoleSequence:
        if RoleStats[role][0] in SurvivalList and RoleStats[role][1]:
            ConditionWinList.append(RoleStats[role][0])
        elif RoleStats[role][0] == "Guardian_angel" and RoleStats[RoleStats[role][24][0]][1]:
            ConditionWinList.append(RoleStats[role][0])
    
    VillargeterList = []
    for role in RoleSequence:
        if RoleStats[role][0] == "Villargeter" and RoleStats[role][1]:
            VillargeterList.append(role)

    if len(VillargeterList) == 1 and len(ConditionWinList) == 0:
        ConditionWinList.append(RoleStats[VillargeterList[0]][0])
    if len(ConditionWinList) != 0:
        print("The following won because of their own conditions:")
        global winDictRole
        for win in ConditionWinList:
            if win in winDictRole:
                winDictRole[win] += 1
            else:
                winDictRole[win] = 1
            print(win)
    print("These players were alive at the end:")
    print(AlivePlayers())
    if (not DebugGame):
        input()
    WinnerList.append(Winner)
    sys.stdout = open('./log.txt', 'a')
    return
    
    


def NonLethalAttack(Attacker, Defender):
    '''
    Handles an "attack" that isn't meant to kill, for example dousing and poisoning
    Returns True if the attack got stopped
    '''
    if RoleStatuses[Defender][1]:
        for guard in RoleStatuses[Defender][2]:
            Attack(guard, Attacker, False, False, False, False, True)
            Attack(Attacker, guard, True, False)
            return True
    return False


def Attack(Attacker, Defender, FromVisit = False, Votable = True, Ranged = False, Shooting = False, Protection = False, Day = False, SpecificAttack = None, Suicide = False):
    '''
    Handles when a role attacks another role
    Returns True when the attack was stopped, i.e. the defender survived
    '''
    if Attacker != None and Defender != None:
        print(f"{RoleStats[Attacker][0]} tries attacking {RoleStats[Defender][0]}")
    global NightmareTrigger
    global Jester

    if Suicide:
        RoleStats[Attacker][1] = False
        print(f"{Attacker} died for whatever reasons")
        return
    
    if RoleStats[Defender][1] == False:
        return
    
    if Attacker == Defender:
        FromVisit = True

    if Day and RoleStatuses[Defender][25] == False:
        print(f"{LinkPerson(Defender)} ({RoleStats[Defender][0]}) is voted out")
        RoleStats[Defender][1] = False
        if RoleStats[Defender][0] == "Magicmaker":
            NightmareTrigger = True
            RoleStats[Defender][30] = True
        elif RoleStats[Defender][0] == "Jester":
            RoleStats[Defender][30] = True
            Jester = True
        elif RoleStats[Defender][0] == "Nightmare":
            RoleStats[Defender][30] = True
            return True
        return
    elif Day:
        return

    if Ranged and RoleStatuses[Defender][4]:
        if CPUGame:
            print(f"Attack from {RoleStats[Attacker][0]} failed since {RoleStats[Defender][0]} was walled")
        return
    
    if Shooting and RoleStatuses[Defender][5]:
        if CPUGame:
            print(f"Attack from {RoleStats[Attacker][0]} failed because {RoleStats[Defender][0]} was bulletproof")
        return
    

    
    AttackVal = RoleStats[Attacker][2]
    if Protection:
        AttackVal = 7
    if RoleStats[Attacker][6] == RoleStats[Defender][4] or RoleStats[Attacker][0] == "Hunter_hunter" and RoleStats[Defender][5]:
        AttackVal = 7
    if SpecificAttack != None:
        AttackVal = SpecificAttack

    if FromVisit:
        ImmuneVal = max(RoleStats[Defender][3], RoleStats[Defender][25]) 
        if AttackVal > ImmuneVal:
            if CPUGame:
                print(f"{RoleStats[Attacker][0]} kills {RoleStats[Defender][0]}")
            RoleStats[Defender][1] = False

    else:
        ImmuneVal = max(RoleStats[Defender][3], RoleStats[Defender][25], RoleStatuses[Defender][3], RoleStatuses[Defender][7])
        print(AttackVal, ImmuneVal)
        if AttackVal > ImmuneVal:
            if CPUGame:
                print(f"{RoleStats[Attacker][0]} kills {RoleStats[Defender][0]}")
            RoleStats[Defender][1] = False
        elif RoleStatuses[Defender][1]:
            for i in RoleStatuses[Defender][2]:
                Attack(i, Attacker, True, False, False, False, True)
                Attack(Attacker, i, True, False)

    if RoleStats[Defender][1] == False and Votable:
        RoleStatuses[Defender][0] = True

    if RoleStats[Defender][1] == False and not FromVisit and RoleStats[Attacker][0] not in NonVisitList:
        Check = RoleStats[Attacker][1]
        if RoleStats[Defender][0] == "Archer" and not CheckRoleblock(Defender):
            Archer_F(Defender, True)
            RoleStats[Defender][34] = True
            if not RoleStats[Attacker][1] and Check:
                RoleStats[Defender][1] = True
        elif RoleStats[Defender][0] == "Targeter" and not CheckRoleblock(Defender):
            Targeter_F(Defender, True)
            RoleStats[Defender][34] = True
            if not RoleStats[Attacker][1] and Check:
                RoleStats[Defender][1] = True


    if RoleStats[Defender][1] == False:

        if RoleStats[Defender][0] == "Godfather":
            if isInGame("Mafioso", True, True):
                PromoteList.append((LinkRoles("Mafioso", None, True), "Godfather"))
            elif isInGame("Mafioso", True):
                for Amne in AmneList:
                    if RoleStats[Amne][0] == "Mafioso":
                        PromoteList.append((Amne, "Godfather"))
                        break

        if RoleStats[Defender][0] == "Crazy_king":
            if isInGame("Crazy", True, True):
                PromoteList.append((LinkRoles("Crazy", None, True), "Crazy_king"))
            elif isInGame("Crazy", True):
                for Amne in AmneList:
                    if RoleStats[Amne][0] == "Crazy":
                        PromoteList.append((Amne, "Crazy_king"))
                        break

        if CPUGame:
            KillingList = ["Nighter", "Jester", "Magicmaker", "Revengetaker"]
        else:
            KillingList = ["Nighter", "Magicmaker", "Revengetaker"]

        if RoleStats[Defender][0] in KillingList:
            Attack(Defender, Attacker, True, False)
            if RoleStats[Defender][0] != "Revengetaker":
                RoleStats[Defender][30] = True

        elif RoleStats[Defender][0] == "Nightmare":
            NightmareTrigger = True
            RoleStats[Defender][30] = True

        elif RoleStats[Defender][0] == "Haunter" and RoleStats[Defender][26] != []:
            Attack(Defender, RoleStats[Defender][26][0], True, False)
        
        elif RoleStats[Defender][0] == "FBI":
            NewRoleList = CreateNewRoleList(Defender)
            for role in NewRoleList:
                if RoleStats[role][1] and RoleStats[role][19] == False:
                    Attack(Defender, role, False, False)
                    break
        
        elif RoleStats[Defender][0] in InvestList:
            RoleStats[Defender][34] = False


def Roleblock(Roleblocker, Target):
    '''
    Roleblocks a target. Handles rage and Nikkiller
    '''
    print(f"{RoleStats[Roleblocker][0]} roleblocks {RoleStats[Target][0]}")
    if RoleStats[Target][14]:
        return 1
    
    if RoleStats[Target][15]:
        Attack(Target, Roleblocker, True)

    if RoleStats[Target][0] == "Nikkiller":
        RoleStats[Target][21] = 2
        return
    
    RoleStatuses[Target][8] = True


def Interrogate(Role, Target):
    print(f"{Role} interrogates {Target}")
    if (RoleStatuses[Target][27] or RoleStatuses[Target][26] or RoleStats[Target][11]) and RoleStatuses[Role][28] == False:
        RoleStats[Role][28].append(True)
        return
    else:
        RoleStats[Role][28].append(False)
        return


def Turn(Role, Target, Dracula = False):
    NonLethalAttack(Role, Target)
    if RoleStats[Role][1]:
        if not RoleStats[Target][35]:
            Attack(Role, Target)
        else:
            print(f"{RoleStats[Role][0]} converts {RoleStats[Target][0]}")
            TurnList.append((Target, RoleStats[Role][36]+1))
            RoleStatuses[Target][8] = True
            RoleStats[Target][22] = 2
            RoleStats[Target][4] = "Vampires"
            RoleStats[Target][35] = False
            if Dracula:
                RoleStatuses[Target][43] = True
            return True




def FindTarget(Role, num = None, next = None, IgnoreControl = False):
    '''
    Finds a target for a role. If it is a CPU-game, this function will be ran
    before every role does their action. The targeting is based on Target-type
    in the main dictionary.
    '''
    if not IgnoreControl:
        if RoleStatuses[Role][29] and not RoleStats[Role][17]:
            RoleStats[Role][26].append(RoleStats[RoleStatuses[Role][30]][26][1])
            return
            
        if RoleStatuses[Role][35] != False and RoleStatuses[Role][35] < Night and not RoleStats[Role][17] and RoleStatuses[Role][36] != "" and RoleStats[RoleStatuses[Role][36]][26] != []:
            RoleStats[Role][26].append(RoleStats[RoleStatuses[Role][36]][26][0])
            RoleStatuses[Role][35] = False
            RoleStatuses[Role][36] = ""
            return
    
    if CPUGame:
        TargetType = RoleStats[Role][13]
        NextList = RoleStats[Role][24]
        
        if num != None:
            TargetType = num
        if next != None:
            NextList = next
        NewRoleList = CreateNewRoleList(Role)
        for t in TargetType:
            TargetFound = False
            if t == 0:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1]:
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
            
            elif t == 1:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and (RoleStats[NewRoleList[i]][4] != RoleStats[Role][4] or (RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False)):
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break

            elif t == 2:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and RoleStats[NewRoleList[i]][4] == RoleStats[Role][4] and not(RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False):
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
            
            elif t == 3:
                ct = 0
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1]:
                        if ct != 1:
                            ct = 1
                            PotTarget = NewRoleList[i]
                        else:
                            RoleStats[Role][26].append(NewRoleList[i])
                            TargetFound = True
                            break
                if not TargetFound and ct == 1:
                    RoleStats[Role][26].append(PotTarget)
                    TargetFound = True
            
            elif t == 4:
                ct = 0
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and (RoleStats[NewRoleList[i]][4] != RoleStats[Role][4] or (RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False)):
                        if ct != 1:
                            ct = 1
                            PotTarget = NewRoleList[i]
                        else:
                            RoleStats[Role][26].append(NewRoleList[i])
                            TargetFound = True
                            break
                if not TargetFound and ct == 1:
                    RoleStats[Role][26].append(PotTarget)
                    TargetFound = True
            
            elif t == 5:
                ct = 0
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and RoleStats[NewRoleList[i]][4] == RoleStats[Role][4] and not(RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False):
                        if ct != 1:
                            ct = 1
                            PotTarget = NewRoleList[i]
                        else:
                            RoleStats[Role][26].append(NewRoleList[i])
                            TargetFound = True
                            break
                if not TargetFound and ct == 1:
                    RoleStats[Role][26].append(PotTarget)
                    TargetFound = True
            
            elif t == 6:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and NewRoleList[i] not in NextList:
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
            
            elif t == 7:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and (RoleStats[NewRoleList[i]][4] != RoleStats[Role][4] or (RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False)) and NewRoleList[i] not in NextList:
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break

            elif t == 8:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] == False and not RoleStats[NewRoleList[i]][18]:
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
            
            elif t == 9:
                for i in range(-1, 1, -1):
                    if RoleStats[NewRoleList[i]][1]:
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
            
            elif t == 10:
                for i in range(-1, 1, -1):
                    if RoleStats[NewRoleList[i]][1] and (RoleStats[NewRoleList[i]][4] != RoleStats[Role][4] or (RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False)):
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
            elif t == 11:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] and RoleStats[NewRoleList[i]][4] == RoleStats[Role][4] and not (RoleStats[NewRoleList[i]][0] == "Murderer" and RoleStats[Role][32] == False) and NewRoleList[i] not in NextList:
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break
                
            elif t == 12:
                for i in range(1, len(NewRoleList)):
                    if RoleStats[NewRoleList[i]][1] == False and RoleStats[NewRoleList[i]][4] in GoodList and RoleStats[NewRoleList[i]][4] != "Combo":
                        RoleStats[Role][26].append(NewRoleList[i])
                        TargetFound = True
                        break

            if TargetFound == False:
                RoleStats[Role][26].append(1)


def ExecuteTarget(Role, Target, Attacking = True, Visiting = True, IgnoreTrans = False): 
    global DrageTrigger
    '''
    This function executes what will happen when a role targets another role.
    Handles stuff like Veteran, Crusader and Rampages.
    Returns True if the character got hit by a rampage
    '''
    OriginalTarget = Target
    Rampage = False

    if Target == 1:
        return None, False
    if RoleStats[Role][0] != "Targeter":

        if Visiting and RoleStatuses[Role][37] and not RoleStats[Role][14]:
            RoleStatuses[Role][37] = False
            RoleStatuses[Role][8] = True
            return None, False
        elif Visiting and RoleStatuses[Role][37]:
            RoleStatuses[Role][37] = False
        
        if RoleStatuses[Target][11] and not IgnoreTrans:
            for i in RoleSequence:
                if i != Target and RoleStatuses[i][11]:
                    Target, Rampage = ExecuteTarget(Role, i, Attacking, Visiting, True)
                    return Target, Rampage
        
        if RoleStats[Target][0] == "Idiot" and RoleStatuses[Target][13]:
            Target, Rampage = ExecuteTarget(Role, RoleStats[Target][26][0], Attacking, Visiting, True)
            return Target, Rampage

        if RoleStatuses[Target][12]:
            Target, Rampage = ExecuteTarget(Role, "Security_guard", Attacking, Visiting, True)
            return Target, Rampage
        
    if RoleStats[Role][4] == "Mafia" and RoleStats[Target][0] == "Murderer" and RoleStats[Role][0] != "Murderer":
        for role in RoleSequence:
            if RoleStats[role][4] == "Mafia":
                RoleStats[role][32] = True

    LookoutCheck = False
    TrackerCheck = False
    if Visiting:
        LookoutCheck = True
        TrackerCheck = True
        #Jailor

        if RoleStats[Target][0] == "Drage":
            DrageTrigger += 1
        if RoleStats[Target][0] == "Veteran" and RoleStatuses[Target][13] and (RoleStats[Role][2] <= 4 or Attacking == False) and not RoleStatuses[Role][39]:
            Attack(Target, Role, True, False)
            if RoleStats[Role][0] != "Targeter":
                Target = None

        elif RoleStats[Target][0]== "Medusa" and RoleStatuses[Target][13] and (RoleStats[Role][2] <= 4 or Attacking == False) and RoleStats[Role][6] != "Coven" and not RoleStatuses[Role][39]:
            Attack(Target, Role, True)
            if RoleStats[Role][0] != "Targeter":
                Target = None

        elif RoleStats[Target][0] == "Poisoner" and PoisonerSaver == True and (RoleStats[Role][2] <= 4 or Attacking == False) and RoleStats[Role][6] != "Poisoners" and not RoleStatuses[Role][39]:
            Attack(LinkRoles("Poisoner_saver"), Role, True, False)

        elif RoleStats[Target][4] == "Creators" and Snorre and not(RoleStats[Role][14]) and not(RoleStats[Target][0] == "Snorre") and not(RoleStats[Role][6] == "Creators") and not(RoleStats[Role][4] == "Creators"):
            if RoleStats[Role][0] == "Nikkiller":
                Target = None
            else:
                SnorreList = []
                for i in RoleSequence:
                    if RoleStats[i][0] == "Snorre" and RoleStatuses[i][13]:
                        SnorreList.append(i)
                
                for i in SnorreList:
                    Roleblock(i, Role)
                if RoleStats[Role][0] != "Targeter":
                    Target = None

        elif RoleStats[Target][0] == "Werewolf" and RoleStatuses[Target][13] and (RoleStats[Role][2] <= 4 or Attacking == False) and RoleStats[Role][6] != "Werewolves" and not RoleStatuses[Role][39]:
            Attack(Target, Role, True)

        elif RoleStats[Target][0] == "Pestilence" and not RoleStatuses[Role][39] and RoleStats[Role][6] != "Pestilences":
            Attack(Target, Role, True)

        elif RoleStats[Target][0] == "Elias" and RoleStatuses[Target][13] and (RoleStats[Role][2] <= 5 or Attacking == False) and RoleStats[Role][6] != "Creators" and not RoleStatuses[Role][39]:
            Attack(Target, Role, True)

        elif RoleStats[Target][0] == "Suicide_bomber" and RoleStatuses[Target][13] and RoleStats[Role][6] != "Serial_killers" and not RoleStatuses[Role][39] and not RoleStats[Target][6] == "Terrorists":
            Attack(Target, Role, True, False)

        elif RoleStats[Target][0] == "Polar_bear" and RoleStatuses[Target][13] and RoleStats[Role][6] != "Freezers" and not RoleStatuses[Role][39]:
            Attack(Target, Role, True, False)

        if Target != None and RoleStatuses[Target][14] and RoleStats[Role][4] != "Mafia" and RoleStats[Role][6] != "Mafia" and not RoleStatuses[Role][39]:
            Attack(LinkRoles("Ambusher"), Role, True, False)
            RoleStatuses[Target][14] = False

        if Target != None and RoleStatuses[Target][15] and (RoleStats[Role][2] <= 4 or not Attacking) and not RoleStatuses[Role][39]:
            Attack(LinkRoles("Crusader"), Role, True, False)
            RoleStatuses[Target][15] = False

        if Target != None and RoleStatuses[Target][16] and RoleStats[Role][4] != "Vampires" and RoleStats[Role][6] != "Vampires" and not RoleStatuses[Role][39]:
            Attack(LinkRoles("Frenzied_thrall"), Role, True, False)

        if Target != None and RoleStatuses[Target][45] and Attacking:
            RoleStatuses[Target][45] = False
            RoleStatuses[Target][46] = ""
            for role in RoleSequence:
                if Target in RoleStats[role][24] and RoleStats[role][0] == "Trapper":
                    RoleStats[role][27].append(RoleStats[Role][0])
                    RoleStats[role][24].remove(Target)
                    break
            if RoleStats[Role][0] != "Targeter":
                Target = None

        if Target != None and RoleStats[Target][6] == RoleStats[Role][4]:
            if RoleStats[Target][19]:
                Attack(Target, Role, True, False)
            else:
                Attack(Target, Role, True)
        
        if Target != None and RoleStatuses[Target][17] and not RoleStatuses[Role][39] and RoleStats[Role][0] != "Werewolf":
            if WRampageTrigger:
                Attack(LinkRoles("Werewolf"), Role, True)
                Rampage = True
            
            else:
                RoleStatuses[Role][18] = True

        if Target != None and RoleStatuses[Target][19] and not RoleStatuses[Role][39] and RoleStats[Role][0] != "Pestilence":
            if PRampageTrigger:
                Attack(LinkRoles("Pestilence"), Role, True)
                Rampage = True
            
            else:
                RoleStatuses[Role][20] = True

        if Target != None and RoleStatuses[Target][21] and not RoleStatuses[Role][39] and RoleStats[Role][0] != "Elias":
            if ERampageTrigger:
                Attack(LinkRoles("Elias"), Role, True)
                Rampage = True
            
            else:
                RoleStatuses[Role][22] = True

        if Target != None and RoleStatuses[Target][23] and not RoleStatuses[Role][39] and RoleStats[Role][0] != "Grenadethrower":
            if GRampageTrigger:
                Attack(LinkRoles("Grenadethrower"), Role, True)
                Rampage = True
            
            else:
                RoleStatuses[Role][24] = True
            
        if Target != None and RoleStatuses[Target][40] and not RoleStatuses[Role][39] and RoleStats[Role][0] != "Polar_bear":
            if PBRampageTrigger:    
                Attack(LinkRoles("Polar_bear"), Role, True)
                Rampage = True
            
            else:
                RoleStatuses[Role][41] = True
        
    if RoleStats[Role][0] == "Targeter":
        Target = OriginalTarget
        if RoleStatuses[Role][37]:
            RoleStatuses[Role][37] = False

    if Target != None and LookoutCheck:
        for role in RoleSequence:
            if RoleStats[role][0] == "Lookout" and RoleStats[role][29] != [] and RoleStats[role][29][0] == Target:
                RoleStats[role][29].append(Role)

    if Target != None and TrackerCheck:
        for role in RoleSequence:
            if RoleStats[role][0] == "Tracker" and RoleStats[role][29] != [] and RoleStats[role][29][0] == Role:
                RoleStats[role][29].append(Target)

            
    return Target, Rampage

    
def runGame(List = None): #Runs the game
    global PestilenceInGame
    global RoleSequence
    global PlayerSequence
    global PlayersAlive
    if CPUGame:
        RoleSequence = List
        PlayerSequence = r.sample(PlayerNames, len(RoleSequence))
    # print("The following players are in the game:")
    # for name in PlayerSequence:
    #     print(name)
    #input()
    if isInGame("Guardian_angel"):
        FindTargetGA(LinkRoles("Guardian_angel"))
    if isInGame("Librarian"):
        FindTargetLib(LinkRoles("Librarian"))
    if isInGame("Token") and isInGame("Herman"):
        RoleStats[LinkRoles("Herman")][21] = 0
        RoleStats[LinkRoles("Herman")][2] = 2
    if isInGame("Identifier"):
        CreateListIdentifier(LinkRoles("Identifier"))
    if isInGame("Pestilence"):
        PestilenceInGame = True
    for role in RoleSequence:
        if RoleStats[role][4] == "Mafia":
            RoleStats[role][35] = False
        elif HasTeammate(role):
            RoleStats[role][35] = False
    PlayersAlive = len(RoleSequence)
    Promote()
    RunTurn()
    WinCheck()
    UpdateYoungest()
    if Win:
        return
    if CPUGame:
        while True:
            runNight()
            Promote()
            RunTurn()
            WinCheck()
            print(f"The current alive roles are: {CreateCurrentRoleList()}")
            if Win:
                return
            runDay()
            if Win:
                return
    else:
        print("These players are in the game:")
        for i in PlayerSequence:
            print(i)
        print("Good luck!")
        input()
        while True:
            for player in Players.keys():
                for i in range(15):
                    print("\n")
                print(f"It is {player}'s turn to choose target")
                input()
                PreNightCheck(player)

            for role in List:
                TargetCPU(List)
            runNight()

            #Controlling and hypnotizing

            for player in Players.keys():
                for i in range(15):
                    print("\n")
                print(f"It is {player}'s turn to check results")
                input()
                PostNightCheck(player)
            
            Promote()
            RunTurn()
            WinCheck()
            if Win:
                return
            
            runDay()
            if Win:
                return


StandardTargetList = ["Gasthrower", "Freezer_hunter", "Washer", "Amneshiff", "Creator_hunter", "Librarian", "Pirate", "Scared", 
                      "Writer", "FBI_hunter", "Hex_master", "Crazy", "Crazy_king", "Crazy_knight_hunter", "Targeter", "Thief", 
                      "Elias", "Jesper", "Johannes", "Kristian", "Ole_bjorn", "Assassin_dog", "Digger", "Herman", "Token", 
                      "Agent", "Agent_ZK", "Coven_hunter", "FBI", "Cooler", "Eskimo", "Freezer", "Polar_bear", "Sculpturer", 
                      "Terrorist_hunter", "Archer", "King", "Knight", "Police_hunter", "Queen", "Ambusher", "Consigliere", 
                      "Consort", "Framer", "Godfather", "Hypnotist", "Janitor", "Mafioso", "Mafiturner", "Murderer", "SK_hunter", 
                      "Unframer", "Mafia_hunter", "Poisoner", "Pollutifier", "General", "Identifier", "Sniper", "Soldier", 
                      "Stupido_hunter", "Tankman", "Crazy_hunter", "Serial_killer", "Clown", "Hunter_hunter", "Idiot", "Remover", 
                      "Stupido", "Combo_hunter", "Grenadethrower", "Crusader", "Escort", "Haunter", "Immunist", "Investigator", 
                      "Journalist", "Lookout", "Pestilence_hunter_R", "Pestilence_hunter_K", "Pestilence_hunter_H", "Security_guard", 
                      "Sheriff", "Spy", "Statuschecker", "Tracker", "Trapper", "Vampire_hunter", "Waller", "Worker", "Dracula", 
                      "Frenzied_thrall", "Vampire", "Werewolf_hunter", "Dog_mauler", "Firefighter", "Jailwolf", "Poisoner_hunter", 
                      "Pestilence"]

AlertList = []

NoActionList = []
        
def PreNightCheck(Player):
    '''
    Runs the targetting for players before the night begins
    '''
    Players[Player][2] = RoleStats[Players[Player][1]][0]
    Name = Players[Player][0]
    Ref = Players[Player][1]
    Role = Players[Player][2]
    print(f"Your alias is {Name}, keep it secret!")
    print(f"Your role is {Role}")
    print("\n")
    #Hunters
    #Librarian, guardian angel
    #The following must be checked if they can target this night:
    #Writer, Elias, Jesper, Mafiturner, Polar bear, Sculpturer, Janitor, Suicidal, Soldier
    #Tankman, Idiot, Journalist, PHK, Trapper, Worker, Dracula, Vampire
    Teammates = []
    for role in RoleSequence:
        if RoleStats[role][4] == RoleStats[Ref][4] and role != Ref and RoleStats[role][1]:
            Teammates.append(LinkPerson(role))
    
    if Teammates != [] and HasTeammate(Ref) and Role != "Murderer":
        if Night == 0:
            print("You are not alone! You have teammates to help you")
            print("They are:")
        else:
            print("Your teammates are:")
        for role in Teammates:
            print(f"{LinkPerson(role)} ({RoleStats[role][0]})")
    
    elif HasTeammate(Ref) and Role != "Murderer":
        print("Unfortunately, all your teammates are dead. You have to do this on your own")

    #Special case murderer

    input()

    if Role in StandardTargetList:
        print("Who do you want to target tonight?")
        TargetList = []
        NextList = []
        #Hex_master, Digger, Cooler, Hypnotist, Murderer, Immunist, Kristian

        if RoleStats[Ref][13][0] in [0, 3, 6, 9]:
            ct = 0
            for role in RoleSequence:
                if RoleStats[role][1] and Ref != role:
                    ct += 1
                    print(f"{ct} - {LinkPerson(role)}")
                    TargetList.append(role)

        elif RoleStats[Ref][13][0] in [1, 4, 7, 10]:
            ct = 0
            for role in RoleSequence:
                if RoleStats[role][1] and Role != role and RoleStats[role][4] != RoleStats[Ref][4]:
                    ct += 1
                    print(f"{ct} - {LinkPerson(role)}")
                    TargetList.append(role)

        elif RoleStats[Ref][13][0] in [2, 5, 11]:
            ct = 0
            for role in RoleSequence:
                if RoleStats[role][1] and Role != role and RoleStats[Ref][4] == RoleStats[role][4]:
                    ct += 1
                    print(f"{ct} - {LinkPerson(role)}")
                    TargetList.append(role)

        Target = input()
        try:
            int(Target)
            TargetList[Target-1]
            RoleStats[Ref][26] = [TargetList[Target-1]]
            Players[Player][3] = [TargetList[Target-1]]
        except:
            RoleStats[Ref][26] = [1]
            Players[Player][3] = [1]


def PostNightCheck(Player):
    '''
    Runs the part after the night is over, where the players get their information
    '''
    pass


def TargetCPU(Role):
    '''
    Function that chooses targets for the CPUs in a non-cpu game
    '''
    pass




def mainMenu():
    global CPUGame
    global DebugGame
    global RoleSequence
    global PlayerSequence
    print("Town of salem, chaos edition.")
    print("What do you wish to play?")
    print('''
1 - CPU-game
2 - Real game
3 - Debug Game''')
    Ans = input()
    if Ans == "1":
        CPUGame = True
        Amount = int(input("How many CPUs? "))
        Ans = input('''
Do you want to input your own CPUs or just pick randomly?
1 - Input CPUs
2 - Pick randomly'''
)
        if Ans == "1":
            CPUList = []
            for i in range(Amount):
                CPU = input(f"What is CPU {i+1}? ")
                CPUList.append(CPU)
            print(CPUList)
            input()
            runGame(CPUList)
        elif Ans == "2":
            CPUList = r.sample(RoleList, Amount)
            print(SpamTest)
            input()
            runGame(SpamTest)
    if Ans == "3":
        global Cycles
        Cycles = int(input("How many cycles do you want to run?\n"))
        sys.stdout = open('./log.txt', 'w')
        CPUGame = True
        DebugGame = True
        for i in range(Cycles):
            print("STARTING GAME")
            print(f"Cycle {i+1}")
            setGlobals(True)
            DebugTest = r.sample(RoleList, len(RoleList))
            print(DebugTest)
            runGame(DebugTest)
        print(winDictRole)
        print(winDictTeam)


    elif Ans == "2":
        Amount = int(input("How many players wish to play?"))
        for i in range(Amount):
            Player = input(f"What is the name of player {i+1}?")
            Players[Player] = []
        CPUAmount = int(input("How many CPUs do you wish to play with?"))
        RoleSequence = r.sample(RoleList, Amount+CPUAmount)
        PlayerSequence = r.sample(PlayerNames, len(RoleSequence))
        Aliases = r.sample(PlayerSequence, Amount)
        NonCPUList = []
        CPUList = []
        for i in range(len(Players.keys())):
            Players[Players.keys()[i]] = [Aliases[i], RoleSequence[PlayerSequence.index(Aliases[i])], RoleSequence[PlayerSequence.index(Aliases[i])], []]
            NonCPUList.append(RoleSequence[PlayerSequence.index(Aliases[i])])
        for role in RoleSequence:
            if role not in NonCPUList:
                RoleStats[role][20] = True
                CPUList.append(role)
        runGame(CPUList)

Test0 = ['Haunter', 'Ambusher', 'Agent', 'Security_guard', 'Werewolf', 'Consigliere', 'Pirate', 'SK_hunter', 'Thief', 'Sniper',
          'Retributionist', 'Mafioso', 'Arsonist', 'Frenzied_thrall', 'Crazy_hunter', 'Coven_hunter', 'Mayor', 'Jailwolf',
            'Guardian_angel', 'Daylight_killer', 'Lookout', 'Freezer_hunter', 'Poisoner_hunter', 'Robber', 'Nikkiller', 'Crazy',
              'Escort', 'Combo_hunter', 'Creator_hunter', 'Eskimo', 'Tracker', 'Investigator', 'Stupido', 'Poisoner', 'Lifeguard1',
                'Mafiturner', 'Nighter', 'Dracula', 'Journalist', 'Vampire', 'Identifier', 'Archer', 'Werepup', 'Necromancer',
                  'Bodyguard', 'Knight', 'Poisoner_saver', 'Spy', 'Unframer', 'Targeter', 'Hypnotist', 'Medium', 'Nightmare',
                    'Kristian', 'Dog_mauler', 'Villager', 'Trapper', 'Crazy_knight_hunter', 'Amnesiac', 'Godfather', 'Immunist',
                      'Digger', 'Pestilence', 'Clown', 'Mafia_hunter', 'Johannes', 'Polar_bear', 'Revengetaker', 'Hunter_hunter',
                        'Queen', 'Snorre', 'Jester', 'General', 'Police', 'Mikael', 'Magicmaker', 'Assisting_dog', 'Armorer', 'Idiot',
                          'King', 'Ingenting', 'Potion_master', 'Librarian', 'Stupido_hunter', 'Tankman', 'Transporter', 'Crusader',
                            'FBI_hunter', 'Waller', 'Ole_bjorn', 'Pollutifier', 'Drage', 'Incinerator', 'Coven_leader', 'Soldier',
                              'Cooler', 'Herman', 'Crazy_king', 'Suicide_bomber', 'Terrorist', 'Hex_master', 'Writer', 'Survivor',
                                'Doctor', 'Mayorguarder', 'Janitor', 'Jesper', 'Pestilence_hunter_R', 'Lifeguard2', 'FBI', 'Vigilante',
                                  'Grenadethrower', 'Sculpturer', 'Villargeter', 'Huntrustiff', 'Police_hunter', 'Pestilence_hunter_H',
                                    'Scared', 'Vampire_hunter', 'Washer', 'Murderer', 'Jailor', 'Amneshiff', 'Gasthrower',
                                      'Assassin_dog', 'Freezer', 'Dayriff', 'Consort', 'Amnescriff', 'Statuschecker',
                                        'Terrorist_hunter', 'Remover', 'Token', 'Serial_killer', 'Worker', 'Sheriff', 'Agent_ZK',
                                          'Pestilence_hunter_K', 'Medusa', 'Killager', 'Firefighter', 'Bulleter', 'Elias', 'Veteran',
                                            'Oliver', 'Framer', 'Werewolf_hunter']

Test1 = ["Consigliere", "Eskimo", "Statuschecker", "Vigilante", "Hex_master", "Poisoner", "Soldier", "Hunter_hunter", "Coven_hunter", "Crazy_knight_hunter"]
Test2 = ["FBI", "Elias", "Scared", "Consort", "Pestilence", "Bodyguard", "Vampire", "Spy", "Mafiturner", "Dog_mauler"]
Test3 = ["Tracker", "Snorre", "Targeter", "Lookout", "Serial_killer", "Archer", "Pirate", "Agent_ZK", "Werewolf_hunter", "Jesper"]
Test4 = ["King", "Mayor", "Creator_hunter", "Thief", "Werepup", "Retributionist", "Washer", "Writer", "Knight", "Mafioso"]
Test5 = ["Medusa", "Agent", "Sheriff", "Drage", "FBI_hunter", "Pestilence_hunter_K", "Revengetaker", "Jester", "Mayorguarder", "Polar_bear"]
Test6 = ["Jailwolf", "Security_guard", "Daylight_killer", "Assisting_dog", "Poisoner_hunter", "Lifeguard1", "Suicide_bomber", "Amnesiac", "Freezer_hunter", "Investigator"]
Test7 = ["Unframer", "Doctor", "Ole_bjorn", "Queen", "Framer", "Murderer", "Cooler", "Pestilence_hunter_H", "Lifeguard2", "Haunter"]
Test8 = ["Journalist", "Tankman", "Robber", "Nikkiller", "Ingenting", "Amneshiff", "Crazy", "Crusader", "Frenzied_thrall", "Idiot"]
Test9 = ["Clown", "SK_hunter", "Token", "Hypnotist", "Veteran", "Terrorist_hunter", "Villargeter", "Assassin_dog", "General", "Gasthrower", "Immunist"]
Test10 = ["Poisoner_saver", "Sniper", "Necromancer", "Mikael", "Villager", "Crazy_hunter", "Killager", "Stupido_hunter", "Amnescriff", "Jailor", "Police"]
Test11 = ["Potion_master", "Dracula", "Police_hunter", "Mafia_hunter", "Ambusher", "Escort", "Digger", "Janitor", "Huntrustiff", "Remover", "Worker"]
Test12 = ["Pestilence_hunter_R", "Grenadethrower", "Waller", "Incinerator", "Transporter", "Nightmare", "Firefighter", "Kristian", "Stupido", "Vampire_hunter", "Crazy_king"]
Test13 = ["Medium", "Sculpturer", "Survivor", "Trapper", "Combo_hunter", "Terrorist", "Godfather", "Dayriff", "Bulleter", "Magicmaker", "Pollutifier"]
Test14 = ["Armorer", "Librarian", "Arsonist", "Identifier", "Nighter", "Herman", "Coven_leader", "Werewolf", "Freezer", "Johannes", "Oliver", "Guardian_angel"]

'''Following are all of the functions for the roles. Prepare yourself'''

SpamTest = ['Nighter', 'Lifeguard2', 'Terrorist_hunter', 'Necromancer', 'Clown', 'Bulleter', 'General', 'Pestilence_hunter_H', 'Librarian', 'Murderer', 'Writer', 'Crazy_king', 'Washer', 'Pestilence', 'Ingenting', 'Guardian_angel', 'Huntrustiff', 'Villargeter', 'Pollutifier', 'Terrorist', 'Cooler', 'SK_hunter', 'Werewolf', 'Revengetaker', 'Sheriff', 'Killager', 'Potion_master', 'Jester', 'Mikael', 'Snorre', 'Amnesiac', 'King', 'Ole_bjorn', 'Vampire_hunter', 'Doctor', 'Targeter', 'Lifeguard1', 'Tracker', 'Retributionist', 'Security_guard', 'Eskimo', 'Armorer', 'Dayriff', 'Oliver', 'Worker', 'Mafioso', 'Unframer', 'Frenzied_thrall', 'Villager', 'Poisoner', 'Vampire', 'Framer', 'FBI_hunter', 'Escort', 'Mayor', 'Herman', 'Mafiturner', 'Transporter', 'Godfather', 'Crazy_knight_hunter', 'Coven_hunter', 'Incinerator', 'Consigliere', 'Police_hunter', 'Janitor', 'Johannes', 'Veteran', 'Scared', 'Werewolf_hunter', 'Mayorguarder', 'Immunist', 'Elias', 'Arsonist', 'Stupido', 'Vigilante', 'Freezer', 'Werepup', 'Kristian', 'Crazy', 'Medusa', 'Statuschecker', 'Tankman', 'Trapper', 'Nikkiller', 'Thief', 'Crazy_hunter', 'Stupido_hunter', 'Dog_mauler', 'Haunter', 'Sculpturer', 'Journalist', 'Digger', 'Agent_ZK', 'Queen', 'Police', 'Identifier', 'Coven_leader', 'Medium', 'Lookout', 'Combo_hunter', 'Hex_master', 'Waller', 'Ambusher', 'Assassin_dog', 'Robber', 'Jailwolf', 'Hunter_hunter', 'Poisoner_saver', 'Amnescriff', 'Serial_killer', 'Jesper', 'Drage', 'Remover', 'Pirate', 'Creator_hunter', 'Hypnotist', 'Knight', 'Archer', 'Jailor', 'Crusader', 'Sniper', 'Polar_bear', 'Gasthrower', 'FBI', 'Pestilence_hunter_R', 'Agent', 'Amneshiff', 'Spy', 'Daylight_killer', 'Suicide_bomber', 'Nightmare', 'Idiot', 'Magicmaker', 'Token', 'Bodyguard', 'Soldier', 'Freezer_hunter', 'Grenadethrower', 'Pestilence_hunter_K', 'Mafia_hunter', 'Dracula', 'Poisoner_hunter', 'Investigator', 'Consort', 'Firefighter', 'Assisting_dog', 'Survivor']
#Used for brute-force testing a bunch of games

def Arsonist_F(Role): #(1,0,2)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    NextList = []
    NonList = []
    for role in RoleSequence:
        if RoleStatuses[role][26]:
            NextList.append(role)
        elif RoleStats[role][4] != "Arsonists":
            NonList.append(role)
    if RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if (RoleStats[Role][21] == 0 or NonList == []) and not CheckRoleblock(Role) and RoleStats[Role][1] and not Control(Role) and not isInGame("Incinerator", True):
            if CPUGame:
                print("Incineration started")
            RoleStats[Role][22] = 1
        elif isInGame("Incinerator", True):
            RoleStats[Role][21] = 1

    elif RoleStats[Role][23] == 1:
        if (RoleStats[Role][21] == 1 or Control(Role)) and not CheckRoleblock(Role) and RoleStats[Role][1] and NonList != []:
            if CPUGame:
                FindTarget(Role, None, NextList)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Check = NonLethalAttack(Role, Target)
                if not Check:
                    print(f"{RoleStats[Target][0]} doused")
                    RoleStatuses[Target][26] = True
            RoleStats[Role][21] = 0
        RoleStats[Role][23] = 0

    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][22] == 1:
            RoleStats[Role][22] = 0
            for role in RoleSequence:
                if RoleStatuses[role][26]:
                    RoleStatuses[role][26] = False
                    if RoleStats[role][1]:
                        Attack(Role, role, True, False, False, False, False, False)
            RoleStats[Role][21] = 1

def Gasthrower_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if not CheckRoleblock(Role) and RoleStats[Role][1]:
        NextList = []
        for role in RoleSequence:
            if RoleStatuses[role][26]:
                NextList.append(role)
        if CPUGame:
            FindTarget(Role, None, NextList)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Check = NonLethalAttack(Role, Target)
            if not Check:
                if CPUGame:
                    print(f"{Target} doused")
                RoleStatuses[Target][26] = True

def Incinerator_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        if not CheckRoleblock(Role) and RoleStats[Role][1]:
            if CPUGame:
                print("Incineration started")
                RoleStats[Role][22] = 1
        RoleStats[Role][23] = 0

    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][22] == 1:
            RoleStats[Role][22] = 0
            for role in RoleSequence:
                if RoleStatuses[role][26]:
                    RoleStatuses[role][26] = False
                    if RoleStats[role][1]:
                        Attack(Role, role, True, False, False, False, False, False)

def Freezer_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target, False, False)

def Washer_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        for role in RoleSequence:
            if RoleStats[role][4] == "Arsonists" and RoleStats[role][25] <= 1:
                RoleStats[role][25] = 1

    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Role][24] = [Target]
                RoleStatuses[Target][6] = True
                RoleStatuses[Target][7] = max(RoleStatuses[Target][7], 4)

def Amnescriff_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            List = RoleStats[Role][24]
            if CPUGame:
                FindTarget(Role, None, List)
            if not RoleStats[RoleStats[Role][26][0]][18]:
                RoleStats[Role][29].append(RoleStats[RoleStats[Role][26][0]][0])
            else:
                RoleStats[Role][24].append(RoleStats[Role][26][0])
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not RoleStats[Role][29] == []:
            PromoteList.append((Role, RoleStats[Role][29][0]))

def Amneshiff_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target) and not RoleStats[RoleStats[Role][26][0]][18]:
                RoleStats[Role][29].append(RoleStats[RoleStats[Role][26][0]][0])
            elif CheckAction(Role, Target):
                RoleStats[Role][24].append(RoleStats[Role][26][0])
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not RoleStats[Role][29] == []:
            PromoteList.append((Role, RoleStats[Role][29][0]))

def Amnesiac_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            if RoleStats[Role][26][0] != 1 and not RoleStats[RoleStats[Role][26][0]][18]:
                RoleStats[Role][29].append(RoleStats[RoleStats[Role][26][0]][0])
            else:
                RoleStats[Role][24].append(RoleStats[Role][26][0])
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not RoleStats[Role][29] == []:
            PromoteList.append((Role, RoleStats[Role][29][0]))

def Creator_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target, False, False)

def Guardian_angel_F(Role): #(2,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
        if CPUGame:
            RoleStatuses[RoleStats[Role][24][0]][25] = True
            RoleStats[RoleStats[Role][24][0]][25] = max(RoleStats[RoleStats[Role][24][0]][25], 6)
            RoleStats[Role][21] -= 1

def Jester_F(Role):
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if Jester:
        if CPUGame:
            FindTarget(Role)
        Attack(Role, RoleStats[Role][26][0], True, False)

def Killager_F(Role): #(1,3,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][21] == 1 and not CheckRoleblock(Role) and RoleStats[Role][1] and not Control(Role) and RoleStats[Role][22] > 0:
            RoleStats[Role][25] = 4
            RoleStats[Role][22] -= 1
            RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if (RoleStats[Role][21] == 0 or Control(Role)) and not CheckRoleblock(Role) and RoleStats[Role][1] and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Attack(Role, Target, False, False)
            if RoleStats[Role][22] > 0:
                RoleStats[Role][21] = 1
        if RoleStats[Role][34] and CPUGame:
            RoleStats[Role][21] = 0
            RoleStats[Role][34] = False

def Librarian_F(Role): #(0,0,0) #Target is at 24
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    AliveList = AlivePlayers()
    if RoleStats[Role][24][0] in AliveList and not CheckRoleblock(Role) and RoleStats[Role][1] and not Nightmare and not RoleStats[Role][30]:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target, False, False)
            if not RoleStats[Target][1] and Target == RoleStats[Role][24][0]:
                RoleStats[Role][30] = True
                RoleStats[Role][3] = 0

def Pirate_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target = RoleStats[Role][26][0]
            if Target != 1:
                RoleStatuses[Target][8] = True
                if CPUGame:
                    Random = 3
                else:
                    Random = r.randint(1,3)
                if Random == 3:
                    RoleStats[Role][34] = True
    
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][34] and RoleStats[Role][1]:
            Attack(Role, RoleStats[Role][26][0], False, False)
            if not RoleStats[RoleStats[Role][26][0]][1]:
                RoleStats[Role][21] += 1
            RoleStats[Role][34] = False
    if RoleStats[Role][21] == 2:
        RoleStats[Role][30]= True

def Scared_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            if RoleStats[Target][8] == "Killing" and RoleStats[Target][19]:
                Attack(Target, Role, True, False)
                RoleStatuses[Target][8] =  True
            elif RoleStats[Target][8] == "Killing":
                Attack(Target, Role, True)
                RoleStatuses[Target][8] =  True
            else:
                Attack(Role, Target, False, False)
                if not RoleStats[Target][1]:
                    RoleStats[Role][21] += 1
    if RoleStats[Role][21] == 2:
        RoleStats[Role][30] = True

def Survivor_F(Role): #(4,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        RoleStatuses[Role][5] = True
        RoleStats[Role][21] -= 1

def Villager_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        RoleStats[Role][25] = 4
        RoleStats[Role][21] -= 1

def Villargeter_F(Role): #(4,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        RoleStats[Role][25] = 4
        RoleStats[Role][21] -= 1

def Writer_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not RoleStats[Role][34] and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        if RoleStats[Role][26][0] != 1:
            Attack(Role, RoleStats[Role][26][0], False, False)
            RoleStats[Role][34]= True

def Coven_leader_F(Role): #(0,0,2) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target) and not RoleStatuses[Target][29] and RoleStats[Role][26][1] != None:
                RoleStatuses[Target][29] = True
                RoleStatuses[Target][30] = Role
    elif RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][33]:
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Check = NonLethalAttack(Role, Target)
                if not Check:
                    RoleStats[Role][26] = [Target, RoleStats[Role][26][1]]
                    RoleStats[Role][34] = True
    
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][34] and RoleStats[RoleStats[Role][26][0]][1]:
            Attack(Role, RoleStats[Role][26][0], True)
        RoleStats[Role][34]= False

def FBI_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Hex_master_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][24] != [] and (Night%2 == 0 or RoleStats[Role][33]):
            RoleStatuses[RoleStats[Role][24][0]][31] = False
            if RoleStats[RoleStats[Role][24][0]][1]:
                Attack(Role, RoleStats[Role][24][0], True, False)
            RoleStats[Role][24].remove(RoleStats[Role][24][0])

    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            HexList = []
            for role in RoleSequence:
                if RoleStatuses[role][31]:
                    HexList.append(role)
            if CPUGame:
                FindTarget(Role, None, HexList)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Check = NonLethalAttack(Role, Target)
                if not Check:
                    RoleStatuses[Target][31] = True
                    RoleStats[Role][24].append(Target)

def Medusa_F(Role): #(3,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if not RoleStats[Role][33] and RoleStats[Role][21] > 0 and RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][22] == 0:
            RoleStatuses[Role][13] = True
            RoleStats[Role][21] -= 1
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][33] and RoleStats[Role][1] and not CheckRoleblock(Role) and not RoleStatuses[Role][13] and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Attack(Role, Target)
                if not RoleStats[Target][1]:
                    RoleStatuses[Target][32] = True

def Necromancer_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    pass

def Potion_master_F(Role): #(2,0,2)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 0:
        if RoleStats[Role][33] or RoleStats[Role][21] == 1:
            if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
                if CPUGame:
                    FindTarget(Role, [1])
                Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
                if CheckAction(Role, Target):
                    Attack(Role, Target)
                    RoleStats[Role][34] = True
        if RoleStats[Role][34] and CPUGame:
            RoleStats[Role][34] = False
            if RoleStats[Role][21] == 0:
                RoleStats[Role][21] = 2
            elif RoleStats[Role][21] == 2:
                RoleStats[Role][21] = 1
            elif RoleStats[Role][21] == 1:
                RoleStats[Role][21] = 0
    
    elif RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if RoleStats[Role][21] == 2 and RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role, [3])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Target][25] = max(RoleStats[Target][25], 6)
                RoleStats[Role][34] = True

    elif RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][21] == 0 and RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role, [7])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Role][28].append(RoleStats[Target][0])
                RoleStats[Role][24].append(Target)
                RoleStats[Role][34] = True

def Crazy_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Crazy_king", False, True) and RoleStats[LinkRoles("Crazy_king", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("Crazy_king", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("Crazy_king", None, True)][26][0]]
        elif CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Crazy_king_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Crazy", True, True) and not CheckRoleblock(LinkRoles("Crazy", None, True)):
            RoleStats[Role][24] = [LinkRoles("Crazy", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Crazy", True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Crazy" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)
        else:
            RoleStats[Role][24] = []
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Attack(Role, Target)

def Crazy_knight_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Targeter_F(Role, Attacked = False): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if (RoleStats[Role][1] or Attacked) and not CheckRoleblock(Role) and not Nightmare and not RoleStats[Role][34]:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if Target != None:
            Attack(Role, Target, False, True, True, True)
    RoleStats[Role][34] = False

def Thief_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            Roleblock(Role, Target)

def Elias_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global ERampageTrigger
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%3 == 0:
            RoleStatuses[Role][13] = True
            RoleStats[Role][2] = 6
            RoleStats[Role][3]= 5
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStatuses[Target][21] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%3 == 0:
            if RoleStats[Role][26] != []:
                ERampageTrigger = True
                Attack(Role, RoleStats[Role][26][0])
                for role in RoleSequence:
                    if RoleStatuses[role][22]:
                        Attack(Role, role, True)

def Jesper_F(Role): #(3,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][21] -= 1
            if RoleStats[Target][35]:
                PromoteList.append((Target, "Creator_villager"))
                RoleStats[Role][21] = 0
            else:
                RoleStats[Role][24].append(RoleStats[Role][26][0])

def Johannes_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Kristian_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target) and Target != Role:
            RoleStatuses[Target][1] = True
            RoleStatuses[Target][2].append(Role)
            RoleStatuses[Target][3] = 6
            RoleStats[Role][24] = [Target]
            RoleStats[Role][34] = True
    if not RoleStats[Role][34]:
        RoleStats[Role][24] = []
    else:
        RoleStats[Role][34] = False

def Mikael_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        RoleStats[Role][21] -= 1
        for role in RoleSequence:
            if RoleStats[role][4] == "Creators" and RoleStats[role][1] and role != Role:
                RoleStatuses[role][6] = True
                RoleStatuses[role][7] = 4

def Ole_bjorn_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][28].append(RoleStats[Target][0])
            RoleStats[Role][24].append(Target)

def Oliver_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][24] = []
    if Night%2 == 0:
        RoleStats[Role][21] += 1
    while RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and not Nightmare:
        RoleStats[Role][21] -= 1
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            RoleStats[Role][26] = []
        else:
            return

def Snorre_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global Snorre
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        RoleStats[Role][21] -= 1
        Snorre = True
        RoleStatuses[Role][13] = True

def Assassin_dog_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True, False)
        if CheckAction(Role, Target):
            Attack(Role, Target)
            if RoleStats[Target][1] and AssistingDog:
                RoleStats[Role][26] = []
                if CPUGame:
                    FindTarget(Role, None, [Target])
                else:
                    TargetList = []
                    for role in CreateCurrentRoleList():
                        if RoleStats[role][4] != "Dogs" and role != Target:
                            TargetList.append(role)
                    if TargetList != []:
                        RoleStats[Role][26] = [r.choice(TargetList)]
                    else:
                        RoleStats[Role][26] = [1]
                Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True, False)
                if CheckAction(Role, Target):
                    Attack(Role, Target)

def Assisting_dog_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global AssistingDog
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
        RoleStats[Role][21] -= 1
        AssistingDog = True

def Digger_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        DigList = []
        for role in RoleSequence:
            if not RoleStatuses[role][37]:
                DigList.append(role)
        if DigList != []:
            if CPUGame:
                FindTarget(Role, None, DigList)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStatuses[Role][37] = True

def Herman_F(Role): #(1,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][34] and Night != 1:
            RoleStats[Role][34] = False
            if RoleStats[Role][21] == 1:
                if RoleStats[Role][2] < 6:
                    RoleStats[Role][2] += 1
                RoleStats[Role][21] = 0
            elif RoleStats[Role][21] == 0:
                RoleStats[Role][21] = 1
                if RoleStats[Role][3] < 6:
                    RoleStats[Role][3] += 1
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStats[Role][34] = True
                Attack(Role, Target)
                if RoleStats[Target][1] and AssistingDog:
                    RoleStats[Role][26] = []
                    if CPUGame:
                        FindTarget(Role, None, [Target])
                    else:
                        TargetList = []
                        for role in CreateCurrentRoleList():
                            if RoleStats[role][4] != "Dogs" and role != Target:
                                TargetList.append(role)
                        if TargetList != []:
                            RoleStats[Role][26] = [r.choice(TargetList)]
                        else:
                            RoleStats[Role][26] = [1]
                    Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
                    if CheckAction(Role, Target):
                        Attack(Role, Target)

def Token_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][24]= []
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)
            if RoleStats[Target][1] and AssistingDog:
                RoleStats[Role][26] = []
                if CPUGame:
                    FindTarget(Role, None, [Target])
                else:
                    TargetList = []
                    for role in CreateCurrentRoleList():
                        if RoleStats[role][4] != "Dogs" and role != Target:
                            TargetList.append(role)
                    if TargetList != []:
                        RoleStats[Role][26] = [r.choice(TargetList)]
                    else:
                        RoleStats[Role][26] = [1]
                Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
                if CheckAction(Role, Target):
                    Attack(Role, Target)

def Agent_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("FBI", False, True) and RoleStats[LinkRoles("FBI", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("FBI", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("FBI", None, True)][26][0]]
        elif CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target, False, False, True, True)

def Agent_ZK_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target, False, False)

def Coven_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target, False, False)

def FBI_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Agent", True, True) and not CheckRoleblock(LinkRoles("Agent", None, True)):
            RoleStats[Role][24] = [LinkRoles("Agent", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Agent", True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Agent" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)

def Cooler_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        for role in RoleSequence:
            if RoleStatuses[role][9] and RoleStats[role][1] and RoleStats[role][3] > 0:
                RoleStats[role][3] -= 1
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            AirList = []
            for role in RoleSequence:
                if RoleStatuses[role][9]:
                    AirList.append(role)
            if CPUGame:
                FindTarget(Role, None, AirList)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStatuses[Target][9] = True

def Eskimo_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1]:
            for role in RoleSequence:
                if RoleStats[role][4] == "Freezers" and RoleStats[role][25] == 0:
                    RoleStats[role][25] = 1
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target) and RoleStats[Target][3] < 6:
                RoleStatuses[Target][6] = True
                RoleStatuses[Target][7] = RoleStats[Target][3] + 2

def Freezer_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Polar_bear_F(Role): #(0,0,2)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global PBRampageTrigger
    if RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%3 == 0:
            RoleStatuses[Role][13] = True
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStatuses[Target][40] = True
    elif RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%3 != 0:
            if isInGame("Freezer", True, True):
                RoleStatuses[LinkRoles("Freezer", None, True)][39] = True
            elif isInGame("Freezer", True):
                for Amne in AmneList:
                    if RoleStats[Amne][0] == "Freezer":
                        RoleStatuses[Amne][39] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%3 == 0:
            if RoleStats[Role][26] != []:
                PBRampageTrigger = True
                Attack(Role, RoleStats[Role][26][0])
                for role in RoleSequence:
                    if RoleStatuses[role][41]:
                        Attack(Role, role, True)

def Sculpturer_F(Role): #(3,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        for role in RoleSequence:
            if RoleStats[role][1] and RoleStats[role][4] == "Freezers":
                RoleStatuses[role][28] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
            if CPUGame and not Control(Role):
                if isInGame("Freezer", True, True) and RoleStats[LinkRoles("Freezer", None, True)][26] != []:
                    RoleStats[Role][26] = RoleStats[LinkRoles("Freezer", None, True)][26]
                elif isInGame("Freezer", True):
                    for Amne in AmneList:
                        if RoleStats[Amne][0] == "Freezer" and RoleStats[Amne][26] != []:
                            RoleStats[Role][26] = RoleStats[Amne][26]
            elif CPUGame:
                FindTarget(Role)
            if RoleStats[Role][26] != []:
                Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
                if CheckAction(Role, Target):
                    RoleStatuses[Target][42] = True
                    RoleStats[Role][21] -= 1

def Terrorist_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Archer_F(Role, Attacked = False): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if (RoleStats[Role][1] or Attacked) and not CheckRoleblock(Role) and not Nightmare and not RoleStats[Role][34]:
        if isInGame("Queen", False, True) and RoleStats[LinkRoles("Queen", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("Queen", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("Queen", None, True)][26][0]]
        elif isInGame("King", False, True) and RoleStats[LinkRoles("King", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("King", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("King", None, True)][26][0]]
        elif CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True, False)
        if CheckAction(Role, Target) or (Target != None and Attacked and not CheckRoleblock(Role)):
            Attack(Role, Target, False, True, True)
    RoleStats[Role][34] = False

def King_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Knight", True, True) and not CheckRoleblock(LinkRoles("Knight", None, True)):
            RoleStats[Role][24] = [LinkRoles("Knight", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Knight", True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Knight" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)
        elif isInGame("Archer", True, True) and not CheckRoleblock(LinkRoles("Archer", None, True)) and not isInGame("Queen", True, True) and not isInGame("Knight", True, True):
            RoleStats[Role][24] = [LinkRoles("Archer", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Archer", True) and not isInGame("Queen", True, True) and not isInGame("Knight", True, True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Archer" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)
        
def Knight_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("King", False, True) and RoleStats[LinkRoles("King", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("King", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("King", None, True)][26][0]]
        elif isInGame("Queen", False, True) and RoleStats[LinkRoles("Queen", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("King", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("Queen", None, True)][26][0]]
        elif CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Lifeguard1_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1]:
        for role in RoleSequence:
            if RoleStats[role][0] == "King":
                RoleStatuses[role][6] = True
                RoleStatuses[role][7] = 4
                break

def Lifeguard2_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1]:
        for role in RoleSequence:
            if RoleStats[role][0] == "Queen":
                RoleStatuses[role][6] = True
                RoleStatuses[role][7] = 4
                break

def Police_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Queen_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Archer", True, True) and not CheckRoleblock(LinkRoles("Archer", None, True)):
            RoleStats[Role][24] = [LinkRoles("Archer", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Archer", True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Archer" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)
        elif isInGame("Knight", True, True) and not CheckRoleblock(LinkRoles("Knight", None, True)) and not isInGame("King", True, True) and not isInGame("Archer", True, True):
            RoleStats[Role][24] = [LinkRoles("Knight", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Knight", True) and not isInGame("King", True, True) and not isInGame("Archer", True, True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Knight" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)

def Ambusher_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][14] = True

def Consigliere_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][28].append(RoleStats[Target][0])
            RoleStats[Role][24].append(Target)

def Consort_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            Roleblock(Role, Target)

def Framer_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][27] = True

def Godfather_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Mafioso", True, True) and not CheckRoleblock(LinkRoles("Mafioso", None, True)):
            RoleStats[Role][24] = [LinkRoles("Mafioso", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Mafioso", True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Mafioso" and not CheckRoleblock(Amne):
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)
        else:
            RoleStats[Role][24] = []
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Attack(Role, Target, False, True, True, True)

def Hypnotist_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] == 1:
            if CPUGame:
                FindTarget(Role, [4])
            RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] == 0:
            if CPUGame:
                FindTarget(Role, [1])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target) and  not RoleStatuses[Target][29] and not RoleStatuses[Target][35]:
                RoleStatuses[Target][35] = Night
                RoleStatuses[Target][36] = Role
                RoleStats[Role][34] = True
        if RoleStats[Role][34]:
            RoleStats[Role][34] = False
            if RoleStats[Role][21] == 1:
                RoleStats[Role][21] = 0
            elif RoleStats[Role][21] == 0:
                RoleStats[Role][21] = 1

def Janitor_F(Role): #(3,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
        if CPUGame and not Control(Role):
            if isInGame("Godfather", True, True) and RoleStats[LinkRoles("Godfather", None, True)][26] != []:
                RoleStats[Role][26] = RoleStats[LinkRoles("Godfather", None, True)][26]
            elif isInGame("Mafioso", True, True) and RoleStats[LinkRoles("Mafioso", None, True)][26] != []:
                RoleStats[Role][26] = RoleStats[LinkRoles("Mafioso", None, True)][26]
            elif isInGame("Mafioso", True):
                for Amne in AmneList:
                    if RoleStats[Amne][0] == "Mafioso" and RoleStats[Amne][26] != []:
                        RoleStats[Role][26] = RoleStats[Amne][26]
        elif CPUGame:
            FindTarget(Role)
        if RoleStats[Role][26] != []:
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Target][33] = True
                RoleStats[Role][21] -= 1
            
def Mafioso_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Godfather", False, True) and RoleStats[LinkRoles("Godfather", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("Godfather", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("Godfather", None, True)][26][0]]
        elif CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target, False, True, True, True)

def Mafiturner_F(Role): #(3,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][21] -= 1
            if RoleStats[Target][35]:
                PromoteList.append((Target, "Mafia_villager"))
                RoleStats[Role][21] = 0
            else:
                RoleStats[Role][24].append(RoleStats[Role][26][0])

def Murderer_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    for role in RoleSequence:
        if role not in RoleStats[Role][24] and RoleStats[role][32]:
            RoleStats[Role][24].append(role)
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True, False)
        if CheckAction(Role, Target):
            if RoleStats[Target][4] == "Mafia" and RoleStats[Target][0] != "Murderer" and Target not in RoleStats[Role][24]:
                RoleStats[Role][24].append(Target)
            else:
                Attack(Role, Target, False, False)

def SK_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Unframer_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][28]

def Mafia_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Poisoner_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        for role in RoleSequence:
            if RoleStatuses[role][44]:
                if RoleStats[role][1]:
                    Attack(Role, role, True, False)
                RoleStatuses[role][44] = False
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True)
            if CheckAction(Role, Target):
                Check = NonLethalAttack(Role, Target)
                if not Check:
                    RoleStatuses[Target][44] = True
                    print(f"{RoleStats[Target][0]} poisoned")

def Poisoner_saver_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global PoisonerSaver
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        PoisonerSaver = True
        RoleStats[Role][21] -= 1

def Pollutifier_F(Role): #(1,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target, False, False)
            Attack(Role, Neighbor(Target, "right"), True, False)
            Attack(Role, Neighbor(Target, "left"), True, False)
            RoleStats[Role][21] = 0

def General_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if isInGame("Soldier", True, True) and not CheckRoleblock(LinkRoles("Soldier", None, True)) and not RoleStats[LinkRoles("Soldier", None, True)][34]:
            RoleStats[Role][24] = [LinkRoles("Soldier", None, True)]
            if CPUGame:
                FindTarget(Role)
        elif isInGame("Soldier", True):
            for Amne in AmneList:
                if RoleStats[Amne][1] == "Soldier" and not CheckRoleblock(Amne) and not RoleStats[Amne][34]:
                    RoleStats[Role][24] = [Amne]
                    if CPUGame:
                        FindTarget(Role)

def Identifier_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][36] = []
    RoleStats[Role][34] = False
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, None, None, True)
            RoleStats[Role][36] = RoleStats[Role][26]
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            for i in range(len(RoleStats[Role][38])):
                if RoleStats[Role][38][i][0] == Target:
                    List = RoleStats[Role][38][i]
                    break
            print(List)
            if not RoleStatuses[Role][34]:
                if List[1] == 0:
                    if RoleStats[Target][9] == "Neutral" and not CheckFramed(Target):
                        RoleStats[Role][38][i][1] = 1
                    elif RoleStats[Target][9] == "Mafia" or CheckFramed(Target):
                        RoleStats[Role][34] = True
                        RoleStats[Role][24].append(Target)
                    elif RoleStats[Target][9] == "Town" and not CheckFramed(Target):
                        RoleStats[Role][24].append(Target)
                    RoleStats[Role][27].append([Target, RoleStats[Target][9]])
                elif List[1] == 1 and not CheckFramed(Target):
                    RoleStats[Role][38][i][1] = 2
                elif List[1] == 1:
                    RoleStats[Role][34] = True
                    RoleStats[Role][24].append(Target)
                elif List[1] >= 2:
                    RoleStats[Role][24].append(Target)
                    if not RoleStats[Target][19] or CheckFramed(Target):
                        RoleStats[Role][34] = True

def Police_F(Role): #(1,0,2) (3)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0 and not Control(Role):
            RoleStats[Role][21] -= 1
            RoleStatuses[Role][5] = True
            RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if (not RoleStats[Role][34] or Control(Role)) and not CheckRoleblock(Role) and (RoleStats[Role][21] == 0 or Control(Role)) and RoleStats[Role][1]:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][0], False)
            if CheckAction(Role, Target) and Target != Role:
                RoleStatuses[Target][1] = True
                RoleStatuses[Target][2].append(Role)
                RoleStatuses[Target][3] = 6
        else:
            RoleStats[Role][34] = False
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][22] == 1 and RoleStats[Role][36] > 0 and not Control(Role):
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Attack(Role, Target, False, False)
                RoleStats[Role][36] -= 1

def Sniper_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][34] and RoleStats[Role][1]:
        Attack(Role, None, False, False, False, False, False, False, None, True)
    elif RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare and not RoleStats[Role][34]:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True, False)
        if CheckAction(Role, Target):
            Check = RoleStats[Target][1]
            Attack(Role, Target, False, False)
            if not RoleStats[Target][1] and Check and RoleStats[Target][4] == "Town":
                RoleStats[Role][34] = True

def Soldier_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare and not RoleStats[Role][34]:
        if isInGame("General", False, True) and RoleStats[LinkRoles("General", None, True)][24] == [Role] and not Control(Role) and RoleStats[LinkRoles("General", None, True)][26] != []:
            RoleStats[Role][26] = [RoleStats[LinkRoles("General", None, True)][26][0]]
        elif CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Check = RoleStats[Target][1]
            Attack(Role, Target, False, False, True, True)
            if not RoleStats[Target][1] and Check and RoleStats[Target][4] == "Town":
                RoleStats[Role][34] = True

def Stupido_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target, False, False)

def Tankman_F(Role): #(3,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare and RoleStats[Role][21] > 0:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target, False, False)
            RoleStats[Role][21] -= 1

def Crazy_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Daylight_killer_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1]:
        if CPUGame:
            FindTarget(Role)
        Attack(Role, RoleStats[Role][26][0], False, False, False, False, False, True)
        RoleStats[Role][26] = []

def Nikkiller_F(Role): #(3,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%3 == 0 and not Nightmare:
        if CPUGame:
            FindTarget(Role)
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            if Control(Role):
                RoleStatuses[Role][29] = False
                RoleStatuses[Role][35] = 0
            FindTarget(Role)
            RoleStats[Role][24].append(RoleStats[Role][26][1])
            FindTarget(Role)
            RoleStats[Role][24] = []
        if RoleStats[Role][21] == 3:
            Target1, Rampage1 = ExecuteTarget(Role, RoleStats[Role][26][0])
        Target2, Rampage2 = ExecuteTarget(Role, RoleStats[Role][26][1])
        Target3, Rampage3 = ExecuteTarget(Role, RoleStats[Role][26][2])
        if RoleStats[Role][21] == 3 and Target1 != None:
            Attack(Role, Target1)
        if Target2 != None:
            Attack(Role, Target2)
        if Target3 != None:
            Attack(Role, Target3)
    RoleStats[Role][21] = 3

def Robber_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    pass

def Serial_killer_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Clown_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        for role in RoleSequence:
            if RoleStatuses[role][10]:
                RoleStatuses[role][8] = True
                RoleStatuses[role][10] = False
    elif RoleStats[Role][23] == 0 and RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][10] = True

def Hunter_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Target][5]:
            Attack(Role, Target)

def Idiot_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        if CPUGame:
            FindTarget(Role)
        RoleStatuses[Role][13] = True
        RoleStats[Role][21] -= 1

def Remover_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][34] = True

def Stupido_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Armorer_F(Role): #(1,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0 and not Control(Role):
            RoleStatuses[Role][5] = True
            RoleStats[Role][21] -= 1
            RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and (RoleStats[Role][21] == 0 or RoleStats[Role][22] == 1 or Control(Role)) and not RoleStats[Role][34]:
            SBList = []
            for role in RoleSequence:
                if RoleStats[role][0] == "Suicide_bomber":
                    SBList.append(role)
            RoleStats[Role][24] += SBList
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStatuses[Target][5] = True
                RoleStats[Role][24] = [RoleStats[Role][26][0]]
        if RoleStats[Role][34]:
            RoleStats[Role][34] = False

def Bulleter_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global Bulleter
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        Bulleter = True

def Combo_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Grenadethrower_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global GRampageTrigger
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStatuses[Target][23] = True
                RoleStats[Role][34] = True
                RoleStats[Role][24] = [Target]
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][34]:
            GRampageTrigger = True
            Attack(Role, RoleStats[Role][24][0])
            for role in RoleSequence:
                if RoleStatuses[role][24]:
                    Attack(Role, role, True)
        RoleStats[Role][34] = False

def Suicide_bomber_F(Role): #(0,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            RoleStatuses[Role][13] = True
    elif RoleStats[Role][23] == 0:
        if RoleStatuses[Role][13]:
            Attack(Role, None, False, False, False, False, False, False, None, True)

def Terrorist_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][34] = False
    RoleStats[Role][21] += 1
    if Bulleter:
        RoleStats[Role][21] += 1
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        while RoleStats[Role][21] > 0 and not RoleStats[Role][34]:
            if CPUGame:
                FindTarget(Role)
            if Control(Role):
                RoleStatuses[Role][29] = False
                RoleStatuses[Role][35] = 0
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStats[Role][21] -= 1
                Attack(Role, Target, False, True, True, True)
                RoleStats[Role][24].append(Target)
                RoleStats[Role][26] = []
            else:
                RoleStats[Role][34] = True
        RoleStats[Role][24] = []

def Bodyguard_F(Role): #(1,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0 and not Control(Role):
            RoleStats[Role][21] -= 1
            RoleStatuses[Role][5] = True
            RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if (not RoleStats[Role][34] or Control(Role)) and not CheckRoleblock(Role) and (RoleStats[Role][21] == 0 or Control(Role)) and RoleStats[Role][1]:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target) and Target != Role:
                RoleStatuses[Target][1] = True
                RoleStatuses[Target][2].append(Role)
                RoleStatuses[Target][3] = 6

        else:
            RoleStats[Role][34] = False

def Crusader_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][15] = True

def Dayriff_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        if RoleStats[Role][26][0] != 1:
            Target = RoleStats[Role][26][0]
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            if RoleStats[Target][11]:
                VoteList.append((Target, LinkPerson(Role), "Dayriff"))
                VoteList2.append((Target, LinkPerson(Role), "Dayriff"))
            RoleStats[Role][28].append(RoleStats[Target][11])
            RoleStats[Role][27].append([Target, RoleStats[Target][11]])

def Doctor_F(Role): #(1,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0 and not Control(Role):
            RoleStats[Role][21] -= 1
            RoleStats[Role][25] = max(RoleStats[Role][25], 6)
            RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if (not RoleStats[Role][34] or Control(Role)) and not CheckRoleblock(Role) and (RoleStats[Role][21] == 0 or Control(Role)) and RoleStats[Role][1]:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Target][25] = max(RoleStats[Target][25], 6)

        else:
            RoleStats[Role][34] = False

def Escort_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            Roleblock(Role, Target)

def Haunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)

def Huntrustiff_F(Role): #(3,3,1) #Next (0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStats[Role][21] -= 1
                RoleStats[Role][36] = 1
                if not RoleStats[Target][19]:
                    RoleStats[Role][34] = True
                    if RoleStats[Role][22] == 0:
                        RoleStatuses[Role][47] = [True, Target]
                else:
                    RoleStats[Role][24].append(Target)
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare and RoleStats[Role][22] > 0:
            if RoleStats[Role][34] and RoleStats[Role][22] > 0:
                Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
                if CheckAction(Role, Target):
                    RoleStats[Role][22] -= 1
                    Attack(Role, Target, False, False, True, True)
                    if RoleStats[Target][1]:
                        RoleStatuses[Role][47] = [True, Target]
            elif RoleStats[Role][21] == 0 and RoleStats[Role][36] != 1 and RoleStats[Role][22] > 0:
                if CPUGame:
                    FindTarget(Role)
                Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
                if CheckAction(Role, Target):
                    RoleStats[Role][22] -= 1
                    Attack(Role, Target, False, False, True, True)
        RoleStats[Role][34] = False
        RoleStats[Role][36] = 0

def Immunist_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, [0])
            RoleStats[Role][24] = [RoleStats[Role][26][0]]
            if not RoleStats[Role][38] == []:
                RoleStats[Role][24].append(RoleStats[Role][38][0])
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Target][25] = 7
            RoleStats[Role][38] = [RoleStats[Role][26][0]]
    else:
        RoleStats[Role][24] = []
        RoleStats[Role][38] = []

def Investigator_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            RoleStats[Role][28].append(RoleStats[Target][12])
            RoleStats[Role][27].append([Target, [RoleStats[Target][9], RoleStats[Target][12]]])

def Jailor_F(Role): #(3,0,2) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role)
            Target = RoleStats[Role][26][0]
            RoleStatuses[Target][8] = True
            RoleStatuses[Target][38] = True
            RoleStats[Target][25] = 6
    elif RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][26] != []:
            Target = RoleStats[Role][26][0]
            RoleStatuses[Target][1] = False
            RoleStatuses[Target][2] = []
            RoleStatuses[Target][3] = 0
            RoleStatuses[Target][6] = False
            RoleStatuses[Target][7] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and Night != 1:
            Attack(Role, RoleStats[Role][26][0], False, False)
            RoleStats[Role][21] -= 1
            if not RoleStats[Target][1]:
                RoleStats[Role][34] = True
                if RoleStats[Target][4] == "Town":
                    RoleStats[Role][21] = 0
    elif RoleStats[Role][23]:
        if not RoleStats[Role][34] and RoleStats[Role][26] != [] and (RoleStats[RoleStats[Role][26][0]][15] or (RoleStats[RoleStats[Role][26][0]][0] == "Elias" and Night%3 == 0)):
            Attack(RoleStats[Role][26][0], Role, True)

def Journalist_F(Role): #(1,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][34] = False
    RoleStats[Role][36] = []
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
        if CPUGame:
            FindTarget(Role, None, None, True)
            RoleStats[Role][36] = RoleStats[Role][26]
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][21] -= 1
            RoleStats[Role][28].append(RoleStats[Target][0])
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            if not RoleStats[Target][19]:
                RoleStats[Role][34] = True

def Lookout_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][36] = []
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, None, None, True)
            RoleStats[Role][36] = RoleStats[Role][26]
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, False)
        if CheckAction(Role, Target):
            RoleStats[Role][29] = [Target]

def Mayor_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1]:
        if CPUGame:
            FindTarget(Role)
        Attack(Role, RoleStats[Role][26][0], False, False, False, False, False, True)
        RoleStats[Role][26] = []

def Mayorguarder_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1]:
        if isInGame("Mayor", True, True):
            Mayor = LinkRoles("Mayor", None, True)
            RoleStatuses[Mayor][6] = True
            RoleStatuses[Mayor][7] = 4

def Medium_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    pass

def Pestilence_hunter_H_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if not PestilenceInGame and RoleStats[Role][1] and not CheckRoleblock(Role):
            if CPUGame:
                FindTarget(Role, [3])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Target][25] = max(RoleStats[Target][25], 6)
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and PestilenceInGame:
            if CPUGame:
                FindTarget(Role, [6])
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
            if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
                Attack(Role, Target)

def Pestilence_hunter_K_F(Role): #(3,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and PestilenceInGame:
            if CPUGame:
                FindTarget(Role, [6])
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
            if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
                Attack(Role, Target)
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not PestilenceInGame and RoleStats[Role][21] > 0:
            if CPUGame:
                FindTarget(Role, [0])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            Check = RoleStats[Target][1]
            if CheckAction(Role, Target):
                Attack(Role, Target, False, False, True, True)
                if not RoleStats[Target][1] and Check and RoleStats[Target][4] == "Town":
                    RoleStats[Role][21] = 0

def Pestilence_hunter_R_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][36] = []
    RoleStats[Role][34] = False
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not PestilenceInGame:
            if CPUGame:
                FindTarget(Role, None, None, True)
                RoleStats[Role][36] = RoleStats[Role][26]
                RoleStats[Role][26] = []
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                RoleStats[Role][24].append(RoleStats[Role][26][0])
                if RoleStats[Target][11] or CheckFramed(Target):
                    RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and PestilenceInGame:
            if CPUGame:
                FindTarget(Role)
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
            if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
                Attack(Role, Target)

def Retributionist_F(Role): #(1,0,1) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global PlayerRevived
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0:
            if CPUGame:
                FindTarget(Role)
            if RoleStats[Role][26][0] != 1:
                RoleStats[Role][34] = True
                RoleStats[Role][21] = 0
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][34]:
            RoleStats[Role][34] = False
            PlayerRevived = True
            RoleStats[RoleStats[Role][26][0]][1] = True
            print(f"{RoleStats[Role][26][0]} revived")
            
def Security_guard_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][12] = True

def Sheriff_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][36] = []
    RoleStats[Role][34] = False
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, None, None, True)
            RoleStats[Role][36] = RoleStats[Role][26]
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            if RoleStats[Target][11] or CheckFramed(Target):
                RoleStats[Role][34] = True
            RoleStats[Role][28].append((RoleStats[Target][11] or CheckFramed(Target)))
            RoleStats[Role][27].append([Target, (RoleStats[Target][11] or CheckFramed(Target))])

def Spy_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            RoleStats[Role][28].append(RoleStats[Target][8])
            RoleStats[Role][27].append([Target, RoleStats[Target][8]])

def Statuschecker_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][36] = []
    RoleStats[Role][34] = False
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, None, None, True)
            RoleStats[Role][36] = RoleStats[Role][26]
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            if RoleStats[Target][9] == "Mafia" or CheckFramed(Target):
                RoleStats[Role][34] = True
            RoleStats[Role][28].append(RoleStats[Target][9] == "Mafia" or CheckFramed(Target))
            RoleStats[Role][27].append([Target, [RoleStats[Target][9], RoleStats[Target][10]]])

def Tracker_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    RoleStats[Role][36] = []
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, None, None, True)
            RoleStats[Role][36] = RoleStats[Role][26]
            RoleStats[Role][26] = []
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, False)
        if CheckAction(Role, Target):
            RoleStats[Role][29] = [Target]

def Transporter_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not RoleStats[Role][34]:
        if CPUGame:
            FindTarget(Role, [0,3])
        Target1, Rampage1 = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        Target2, Rampage2 = ExecuteTarget(Role, RoleStats[Role][26][1], False)
        if CheckAction(Role, Target1) and CheckAction(Role, Target2) and not RoleStatuses[Target1][38] and not RoleStatuses[Target2][38] and Target1 != Target2:
            RoleStatuses[Target1][11] = True
            RoleStatuses[Target2][11] = True
            RoleStats[Role][34] = True
    elif RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role, [0])
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target) and not RoleStatuses[Target][38] and not RoleStatuses[Role][38]:
            RoleStatuses[Target][11] = True
            RoleStatuses[Role][11] = True
            RoleStats[Role][34] = False

def Trapper_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][34] and RoleStats[Role][1] and not CheckRoleblock(Role):
            NextList = []
            for role in RoleSequence:
                if RoleStatuses[role][45] and RoleStatuses[role][46] == Role:
                    NextList.append(role)
            RoleStats[Role][21] = 1
            if CPUGame:
                FindTarget(Role, None, NextList)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target) and not RoleStatuses[Target][45]:
                RoleStatuses[Target][45] = True
                RoleStatuses[Target][46] = Role
                RoleStats[Role][24].append(Target)
                RoleStats[Role][34] = False
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] == 0:
            RoleStats[Role][34] = True
        RoleStats[Role][21] = 0

def Vampire_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target, False, False)

def Veteran_F(Role): #(3,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0:
        RoleStatuses[Role][13] = True
        RoleStats[Role][21] -= 1

def Vigilante_F(Role): #(1,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][21] > 0 and RoleStats[Role][22] == 0 and not Control(Role):
            RoleStats[Role][21] -= 1
            RoleStatuses[Role][5] = True
            RoleStats[Role][22] = 1
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][34]:
            RoleStats[Role][34] = False
            Attack(Role, None, False, False, False, False, False, False, None, True)
        if not RoleStats[Role][22] == 1 and not CheckRoleblock(Role) and (RoleStats[Role][21] == 0 or Control(Role)) and RoleStats[Role][1] and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
            if CheckAction(Role, Target):
                Check = RoleStats[Target][1]
                Attack(Role, Target, False, False, True, True)
                if not RoleStats[Target][1] and Check and RoleStats[Target][4] == "Town":
                    RoleStats[Role][34] = True

        else:
            RoleStats[Role][22] = 0

def Waller_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][4] = True

def Worker_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and Night%2 == 0:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            Attack(Role, Target, False, False)

def Dracula_F(Role): #(3,1,0) (1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][22] != 0:
        RoleStats[Role][22] -= 1
    if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][22] == 0:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Check = Turn(Role, Target, True)
            RoleStats[Role][22] = 2
            if not Check:
                RoleStats[Role][21] -= 1
    else:
        RoleStats[Role][21] -= 1

def Frenzied_thrall_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False)
        if CheckAction(Role, Target):
            RoleStatuses[Target][16] = True

def Vampire_F(Role): #(3,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][31]:
        if RoleStats[Role][22] != 0:
            RoleStats[Role][22] -= 1
        if RoleStats[Role][21] == 0:
            Attack(Role, None, False, False, False, False, False, False, None, True)
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][22] == 0:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                Check = Turn(Role, Target)
                RoleStats[Role][22] = 2
                if not Check:
                    RoleStats[Role][21] -= 1
                    RoleStats[Role][22] = 0
        else:
            RoleStats[Role][21] -= 1
    else:
        RoleStats[Role][21] = 3
        RoleStats[Role][22] = 2

def Werewolf_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Dog_mauler_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Firefighter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Jailwolf_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
        if CheckAction(Role, Target):
            Attack(Role, Target)

def Poisoner_hunter_F(Role): #(0,0,0)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][1] and not CheckRoleblock(Role):
        if CPUGame:
            FindTarget(Role)
        Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], False, True)
        RoleStats[Role][24].append(RoleStats[Role][26][0])
        if CheckAction(Role, Target) and RoleStats[Role][6] == RoleStats[Target][4]:
            Attack(Role, Target)

def Werepup_F(Role):
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    if RoleStats[Role][21] == 3 and RoleStats[Role][1]:
        PromoteList.append((Role, "Werewolf"))
    elif RoleStats[Role][1]:
        RoleStats[Role][21] += 1
        if RoleStats[Role][21] >= 2:
            RoleStats[Role][3] += 1

def Werewolf_F(Role): #(0,0,2)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global WRampageTrigger
    if RoleStats[Role][23] == 2:
        RoleStats[Role][23] = 1
        if RoleStats[Role][1] and not CheckRoleblock(Role) and RoleStats[Role][34]:
            RoleStatuses[Role][13] = True
            if (CPUGame):
                print(f"{RoleStats[Role][0]} stays at home")
    elif RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not RoleStats[Role][34] and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0], True, False)
            if CheckAction(Role, Target):
                RoleStatuses[Target][17] = True
                RoleStats[Role][21] = 1
                RoleStats[Role][24] = [Target]
                RoleStats[Role][34] = True
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][21] == 1 and RoleStats[Role][1] and not CheckRoleblock(Role):
            WRampageTrigger = True
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][24][0], True, True, True)
            if CheckAction(Role, Target):
                Attack(Role, Target)
                for role in RoleSequence:
                    if RoleStatuses[role][18] and role != Role:
                        Attack(Role, role, True)
                RoleStats[Role][21] = 0
        if RoleStatuses[Role][13]:
            RoleStats[Role][34] = False

def Drage_F(Role): #(0,0,0) CEI
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global DrageTrigger
    if RoleStats[Role][1] and not CheckRoleblock(Role) and DrageTrigger >= 3:
        RoleStats[Role][2] = 5
        RoleStats[Role][3] = 5
        if CPUGame:
            FindTarget(Role)
            RoleStats[Role][24].append(RoleStats[Role][26][0])
            FindTarget(Role)
            RoleStats[Role][24].append(RoleStats[Role][26][1])
            FindTarget(Role)
            RoleStats[Role][24] = []
        Target1, Rampage1 = ExecuteTarget(Role, RoleStats[Role][26][0])
        Target2, Rampage2 = ExecuteTarget(Role, RoleStats[Role][26][1])
        Target3, Rampage3 = ExecuteTarget(Role, RoleStats[Role][26][2])
        if Target1 != None:
            Attack(Role, Target1)
        if Target2 != None:
            Attack(Role, Target2)
        if Target3 != None:
            Attack(Role, Target3)
        RoleStats[Role][34] = True
        DrageTrigger = 0
    
def Pestilence_F(Role): #(0,0,1)
    if (DebugGame and RoleStats[Role][1]):
        print(f"Running {RoleStats[Role][0]}")
    global PRampageTrigger
    if RoleStats[Role][23] == 1:
        RoleStats[Role][23] = 0
        if RoleStats[Role][1] and not CheckRoleblock(Role) and not Nightmare:
            if CPUGame:
                FindTarget(Role)
            Target, Rampage = ExecuteTarget(Role, RoleStats[Role][26][0])
            if CheckAction(Role, Target):
                RoleStatuses[Target][19] = True
                RoleStats[Role][21] = 1
                RoleStats[Role][24] = [Target]
    elif RoleStats[Role][23] == 0:
        if RoleStats[Role][21] == 1 and RoleStats[Role][1] and not CheckRoleblock(Role):
            PRampageTrigger = True
            Attack(Role, RoleStats[Role][24][0])
            for role in RoleSequence:
                if RoleStatuses[role][20]:
                    Attack(Role, role, True)
            RoleStats[Role][21] = 0
setGlobals()
mainMenu()
# WinnerList
# Listlol = ["Hypnotist", "Framer", "Vigilante", "Tracker", "Sheriff", "Medium", "Journalist", "Doctor", "Pestilence_hunter_H", "Mafioso", "Villager"]
# List = ['Mafiturner', 'Jailor', 'Dog_mauler', 'Medusa', 'Snorre', 'Werepup', 'Doctor', 'Archer', 'Freezer', 'King', 'Herman', 'Poisoner_hunter', 'Huntrustiff', 'Vampire_hunter', 'Agent', 'Immunist', 'Consigliere', 'Villargeter', 'Johannes', 'Polar_bear', 'Ambusher', 'Janitor', 'Clown', 'Mikael', 'Kristian', 'Robber', 'Hex_master', 'Eskimo', 'Stupido_hunter', 'Drage', 'Crazy_king', 'Elias', 'Godfather', 'Investigator', 'Transporter', 'Bulleter', 'General', 'Trapper', 'Lifeguard1', 'Medium', 'FBI_hunter', 'Police', 'Digger', 'Werewolf', 'Pollutifier', 'Writer', 'Oliver', 'Serial_killer', 'Murderer', 'Hunter_hunter', 'Haunter', 'Terrorist', 'Hypnotist', 'Vigilante', 'Werewolf_hunter', 'Sheriff', 'Mayor', 'Worker', 'FBI', 'Librarian', 'Vampire', 'Combo_hunter', 'Daylight_killer', 'Mafia_hunter', 'Remover', 'Journalist', 'Assassin_dog', 'Statuschecker', 'Retributionist', 'Jesper', 'Survivor', 'Incinerator', 'Tankman', 'Sculpturer', 'Jailwolf', 'Bodyguard', 'Ole_bjorn', 'Stupido', 'Grenadethrower', 'Pestilence', 'Police_hunter', 'Freezer_hunter', 'Amnesiac', 'Nikkiller', 'Armorer', 'Jester', 'Guardian_angel', 'Amnescriff', 'Terrorist_hunter', 'Tracker', 'Washer', 'Scared', 'Identifier', 'Lifeguard2', 'Nightmare', 'Assisting_dog', 'Crazy', 'SK_hunter', 'Crazy_hunter', 'Mayorguarder', 'Pestilence_hunter_K', 'Magicmaker', 'Pirate', 'Revengetaker', 'Dracula', 'Coven_leader', 'Framer', 'Security_guard', 'Cooler', 'Nighter', 'Knight', 'Sniper', 'Lookout', 'Crusader', 'Poisoner_saver', 'Coven_hunter', 'Poisoner', 'Consort', 'Arsonist', 'Villager', 'Agent_ZK', 'Necromancer', 'Pestilence_hunter_R', 'Creator_hunter', 'Mafioso', 'Amneshiff', 'Token', 'Soldier', 'Crazy_knight_hunter', 'Killager', 'Gasthrower', 'Suicide_bomber', 'Waller', 'Pestilence_hunter_H', 'Dayriff', 'Veteran', 'Spy', 'Potion_master', 'Queen', 'Targeter', 'Frenzied_thrall', 'Ingenting', 'Firefighter', 'Escort', 'Thief', 'Unframer', 'Idiot']
# for i in range(100):
#     List = r.sample(RoleList, 147)
#     print(List)
#     runGame(List)
#     ResetEntirely()
# #runGame(List)
print("The code is finished")
print(WinnerList)
