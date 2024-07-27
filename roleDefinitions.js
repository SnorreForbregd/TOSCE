requires("./role.js")

// Liste Hvor vi putter inn alle roller
let RoleList = [];

// RoleList.push(new Role(Name [string], Team [string], Attack [integer], Immunity [integer], TargetImmunity [integer], TargetType [integer], Countdown [integer], RoleblockImmune [bool], Rage [bool]));
RoleList.push(new Role("Sheriff", "Town", 0, 0, 0, 7, 1, false, false));