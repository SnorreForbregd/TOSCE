requires("./role.js")

// Liste Hvor vi putter inn alle roller
let RoleList = [];

// RoleList.push(new Role(Name [string], Team [string], Type (string), Attack [integer], Immunity [integer], TargetImmunity [integer], TargetType [array([integer])], Countdown [integer], RoleblockImmune [bool], Rage [bool], ControlImmune [bool], ControlImmuneEffect [bool], Unique [bool]));

RoleList.push(new Role("Bodyguard", "Town", "Protective", 7, 0, 6, [4], 1, false, false, false, false, false))
RoleList.push(new Role("Crusader", "Town", "Protective", 1, 0, 4, [4], 1, false, false, false, false, false))
RoleList.push(new Role("Dayriff", "Town", "Investigative", 0, 0, 0, [7], 1, false, false, false, true, false))
RoleList.push(new Role("Doctor", "Town", "Protective", 0, 0, 6, [4], 1, false, false, false, false, false));
RoleList.push(new Role("Escort", "Town", "Support", 0, 0, 0, [2], 1, true, false, false, false, false))
RoleList.push(new Role("Haunter", "Town", "Killing", 7, 0, 0, [2], 1, false, false, true, true, false))
RoleList.push(new Role("Huntrustiff", "Town", "Killing", 1, 0, 0, [7], 1, false, false, false, false)) //unique?
RoleList.push(new Role("Immunist", "Town", "Protective", 0, 0, 7, [4], 1, false, false, false, false, false))
RoleList.push(new Role("Investigator"))
RoleList.push(new Role("Jailor"))
RoleList.push(new Role("Journalist"))
RoleList.push(new Role("Lookout"))
RoleList.push(new Role("Mayor"))
RoleList.push(new Role("Mayorguarder"))
RoleList.push(new Role("Medium"))
RoleList.push(new Role("Pestilence Hunter H"))
RoleList.push(new Role("Pestilence Hunter K"))
RoleList.push(new Role("Pestilence Hunter R"))
RoleList.push(new Role("Retributionist"))
RoleList.push(new Role("Revengetaker"))
RoleList.push(new Role("Security Guard"))
RoleList.push(new Role("Sheriff", "Town", 0, 0, 0, [7], 1, false, false, false, false, false))
RoleList.push(new Role("Spy"))
RoleList.push(new Role("Statuschecker"))
RoleList.push(new Role("Tracker"))
RoleList.push(new Role("Transporter"))
RoleList.push(new Role("Trapper"))
RoleList.push(new Role("Vampire Hunter"))
RoleList.push(new Role("Veteran"))
RoleList.push(new Role("Vigilante"))
RoleList.push(new Role("Waller"))
RoleList.push(new Role("Worker"))
RoleList.push(new Role("General"))
RoleList.push(new Role("Identifier"))
RoleList.push(new Role("Police"))
RoleList.push(new Role("Sniper"))
RoleList.push(new Role("Soldier"))
RoleList.push(new Role("Stupidos Hunter"))
RoleList.push(new Role("Tankman"))
RoleList.push(new Role("Agent"))
RoleList.push(new Role("Agent ZK"))
RoleList.push(new Role("Coven Hunter"))
RoleList.push(new Role("FBI"))
RoleList.push(new Role("Ambusher"))
RoleList.push(new Role("Consigliere"))
RoleList.push(new Role("Consort"))
RoleList.push(new Role("Framer"))
RoleList.push(new Role("Godfather"))
RoleList.push(new Role("Hypnotist"))
RoleList.push(new Role("Janitor"))
RoleList.push(new Role("Mafioso"))
RoleList.push(new Role("Mafiturner"))
RoleList.push(new Role("Murderer"))
RoleList.push(new Role("SK Hunter"))
RoleList.push(new Role("Unframer"))
RoleList.push(new Role("Coven Leader"))
RoleList.push(new Role("FBI Hunter"))
RoleList.push(new Role("Hex Master"))
RoleList.push(new Role("Medusa"))
RoleList.push(new Role("Necromancer"))
RoleList.push(new Role("Potion Master"))
RoleList.push(new Role("Crazy Hunter"))
RoleList.push(new Role("Daylight Killer"))
RoleList.push(new Role("Nikkiller"))
RoleList.push(new Role("Robber"))
RoleList.push(new Role("Serial Killer"))
RoleList.push(new Role("Arsonist"))
RoleList.push(new Role("Freezer Hunter"))
RoleList.push(new Role("Gasthrower"))
RoleList.push(new Role("Incinerator"))
RoleList.push(new Role("Washer"))
RoleList.push(new Role("Dog Mauler"))
RoleList.push(new Role("Firefighter"))
RoleList.push(new Role("Jailwolf"))
RoleList.push(new Role("Poisoner Hunter"))
RoleList.push(new Role("Werepup"))
RoleList.push(new Role("Werewolf"))
RoleList.push(new Role("Crazy"))
RoleList.push(new Role("Crazy King"))
RoleList.push(new Role("Crazy Knight Hunter"))
RoleList.push(new Role("Targeter"))
RoleList.push(new Role("Thief"))
RoleList.push(new Role("Archer"))
RoleList.push(new Role("King"))
RoleList.push(new Role("Knight"))
RoleList.push(new Role("Lifeguard 1"))
RoleList.push(new Role("Lifeguard 2"))
RoleList.push(new Role("Queen"))
RoleList.push(new Role("Police Hunter"))
RoleList.push(new Role("Armorer"))
RoleList.push(new Role("Bulleter"))
RoleList.push(new Role("Combo Hunter"))
RoleList.push(new Role("Grenadethrower"))
RoleList.push(new Role("Suicide Bomber"))
RoleList.push(new Role("Terrorist"))
RoleList.push(new Role("Dracula"))
RoleList.push(new Role("Frenzied Thrall"))
RoleList.push(new Role("Vampire"))
RoleList.push(new Role("Werewolf Hunter"))
RoleList.push(new Role("Mafia Hunter"))
RoleList.push(new Role("Poisoner"))
RoleList.push(new Role("Poisoner Saver"))
RoleList.push(new Role("Pollutifier"))
RoleList.push(new Role("Anarchist"))
RoleList.push(new Role("Clown"))
RoleList.push(new Role("Hunter Hunter"))
RoleList.push(new Role("Idiot"))
RoleList.push(new Role("Remover"))
RoleList.push(new Role("Stupido"))
RoleList.push(new Role("Elias"))
RoleList.push(new Role("Jesper"))
RoleList.push(new Role("Johannes"))
RoleList.push(new Role("Kristian"))
RoleList.push(new Role("Mikael"))
RoleList.push(new Role("Ole Bjørn"))
RoleList.push(new Role("Oliver"))
RoleList.push(new Role("Snorre"))
RoleList.push(new Role("Cooler"))
RoleList.push(new Role("Eskimo"))
RoleList.push(new Role("Freezer"))
RoleList.push(new Role("Polar Bear"))
RoleList.push(new Role("Sculpturer"))
RoleList.push(new Role("Terrorist Hunter"))
RoleList.push(new Role("Assassin Dog"))
RoleList.push(new Role("Assisting Dog"))
RoleList.push(new Role("Digger"))
RoleList.push(new Role("Herman"))
RoleList.push(new Role("Token"))
RoleList.push(new Role("Amnescriff"))
RoleList.push(new Role("Amneshiff"))
RoleList.push(new Role("Amnesiac"))
RoleList.push(new Role("Creator Hunter"))
RoleList.push(new Role("Guardian Angel"))
RoleList.push(new Role("Jester"))
RoleList.push(new Role("Killager"))
RoleList.push(new Role("Librarian"))
RoleList.push(new Role("Magicmaker"))
RoleList.push(new Role("Nigher"))
RoleList.push(new Role("Nightmare"))
RoleList.push(new Role("Pirate"))
RoleList.push(new Role("Scared"))
RoleList.push(new Role("Survivor"))
RoleList.push(new Role("Villager"))
RoleList.push(new Role("Villargeter"))
RoleList.push(new Role("Writer"))
RoleList.push(new Role("Ingenting"))
RoleList.push(new Role("Pestilence"))
RoleList.push(new Role("Drage"))