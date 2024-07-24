// Oversikt over alle night actions blant alle roller
const NightActions = ["Werepup", "Herman", "Eskimo", "Lifeguard 1", "Lifeguard 2", "Washer", "Cooler", "Jailor", "Pirate", "Huntrustiff", "Suicide Bomber", "Assisting Dog", "Idiot", "Medusa", "Poisoner Saver", "Veteran", "Werewolf", "Transporter", "Coven Leader", "Hypnotist", "Security Guard", "Anarchist", "Ambusher", "Frenzied Thrall", "Escort", "Consort", "Thief", "Snorre", "Clown", "Necromancer", "Digger", "Robber", "Amnesiac", "FBI", "General", "King", "Queen", "Retributionist", "Armorer", "Bodyguard", "Police", "Survivor", "Vigilante", "Killager", "Villager", "Villargeter", "Werewolf", "Crusader", "Armorer", "Eskimo", "Guardian Angel", "Kristian", "Mikael", "Polar Bear", "Washer", "Bodyguard", "Doctor", "Immunist", "Pestilence Hunter H", "Police", "Potion Master", "Trapper", "Waller", "Hypnotist", "Cooler", "Worker", "Trapper", "Clown", "Bulleter", "Amneshiff", "Amnescriff", "Framer", "Unframer", "Remover", "Consigliere", "Identifier", "Investigator", "Journalist", "Lookout", "Ole Bjørn", "Pestilence Hunter R", "Potion Master", "Sheriff", "Spy", "Status Checker", "Tracker", "Arsonist", "Incinerator", "RAGE", "Jailor", "Writer", "Hunter Hunter", "Combo Hunter", "Coven Hunter", "Crazy Hunter", "Crazy Knight Hunter", "Creator Hunter", "Dog Mauler", "FBI Hunter", "Firefighter", "Freezer Hunter", "Mafia Hunter", "Pestilence Hunter H", "Pestilence Hunter K", "Pestilence Hunter R", "Poisoner Hunter", "Police Hunter", "SK Hunter", "Stupido Hunter", "Terrorist Hunter", "Vampire Hunter", "Werewolf Hunter", "Worker", "Scared", "Jester", "Nikkiller", "Elias", "Drage", "Huntrustiff", "Pestilence Hunter K", "Vigilante", "Soldier", "Police", "Killager", "Librarian", "Pestilence", "Pirate", "Stupido", "Herman", "Token", "Assassin Dog", "Johannes", "Oliver", "Poisoner", "Hex Master", "Godfather", "Mafioso", "Murderer", "Serial Killer", "Hex Master", "Medusa", "Necromancer", "Potion Master", "Dracula", "Vampire", "Crazy King", "Crazy", "Targeter", "Poisoner", "Pollutifier", "Arsonist", "Gasthrower", "Freezer", "Polar Bear", "Jailwolf", "Sniper", "Tankman", "Agent", "Agent ZK", "Terrorist", "Grenadethrower", "Werewolf", "Knight", "Archer", "Jailor", "Grenadethrower", "Coven Leader", "INCINERATE", "Janitor", "Jesper", "Mafiturner", "Amnescriff", "Amneshiff", "Amnesiac", "Retributionist"];
// Liste over alle roller
let RoleList = [];
// Liste over CPUer i et spill
let CPUList = [];
// Globale variabler
let GlobalMods = {GameEnded: false, PosionerSaver: false, Mikael: false, Snorre: false, AssistingDog: false, Nightmare: false, NightmareTrigger: false, DayNumber: 1, Day: true}
// Arrays med promotion-rekkefølge
let PromLists = [
    ["Mafioso", "SK Hunter", "Ambusher", "Consigliere", "Consort", "Framer", "Hypnotist", "Janitor", "Mafiturner", "Unframer", "MafVillager"],
    ["Arsonist", "Freezer Hunter", "Gasthrower", "Incinerator", "Washer"],
    ["Coven Leader", "FBI Hunter"],
    ["Crazy", "Crazy Knight Hunter", "Thief"],
    ["Herman", "Assisting Dog", "Digger"],
    ["FBI", "Coven Hunter"],
    ["Freezer", "Terrorist Hunter", "Cooler", "Eskimo", "Polar Bear"],
    ["Knight", "Police Hunter"],
    ["Poisoner", "Mafia hunter", "Poisoner Saver", "Pollutifier"],
    ["Soldier", "Stupido Hunter"],
    ["Serial Killer", "Crazy Hunter", "Robber"],
    ["Stupido", "Hunter Hunter", "Anarchist", "Clown", "Idiot", "Remover"],
    ["Terrorist", "Combo Hunter", "Armorer", "Bulleter", "Suicide Bomber"],
    ["Vampire", "Werewolf Hunter", "Frenzied Thrall"],
    ["Werewolf", "Dog Mauler", "Firefighter", "Poisoner Hunter"]
]


function RunGame() {
    //while(!GlobalMods.GameEnded) {
        Promote();
        WinCheck();
        Day = !Day;
        Day ? RunNight() : RunDay();
    //}
}
function RunNight() {
    GlobalMods.Nightmare = GlobalMods.NightmareTrigger
    GlobalMods.NightmareTrigger = false

    NightActions.forEach(NARole => {
    
    });
    Reset()
    Promote()
    WinCheck()
}
function RunDay() {
    
DayNumber++
//Amne-folket blir om til rolle
//Daylight killer angriper om eksisterende
//Mayor stemmer om eksisterende
//Utstemming av sus om eksisterende
}

function Reset() {


}

function WinCheck() {

    
}

function TestProperties(Attacker, Target) {
    if ((Attacker.Role.Props.AttackType == "Shot" && Target.Bulletproof) || (Attacker.Role.Props.AttackType == "Ranged" && Target.Walled)) {
        return false;
    }
    return true;
}

function Roleblock(Roleblocker, Target) {
    if (Target.Role.RoleblockImmune) {
        return;
    }
    if (Target.Role.Rage) {
        Attack(Target, Roleblocker, true)
    }
    if(Target.Role.Name == "Nikkiller") {
        Target.Role.Target[2] = -1
        return;
    }
    Target.Props.Roleblocked = true
}

// 0 - Target Self
// 1 - Target First Non-team
// 2 - Target First
// 3 - Target 2nd Non-team
// 4 - Target 2nd
// 5 - Target Team
// 6 - Target Next Non-Team
// 7 - Target Next
// 8 - Control Target
// 9 - Dead

function Target(CPU, Attacking = true, Visiting = true) {
    let Cpu;
    for(let i=0; i<CPU.Role.Target.Length;i++) 
    {
        switch (CPU.Role.Target[i]) {
            case 0:
                CPU.Target[i] = CPUList.indexOf(CPU)
                break
            case 1:
                CPU.Target[i] = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )})
            break
            case 2:
                CPU.Target[i] = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && (cpu.State == 0 && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )})
            break
            case 3:
                Cpu = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && (cpu.State == 0 && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )})
                CPU.Target[i] = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (Ind > CPUList.indexOf(Cpu)) != -1) ? (Ind > CPUList.indexOf(Cpu)) : true )})
            break
            case 4:
                Cpu = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && (cpu.State == 0 && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )})
                CPU.Target[i] = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && (cpu.State == 0 && (Ind > CPUList.indexOf(Cpu)) != -1) ? (Ind > CPUList.indexOf(Cpu)) : true )})
            break
            case 5:
                CPU.Target[i] = CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && cpu.Role.Team == CPU.Role.Team && (cpu.State == 0 && cpu.Role.Team == CPU.Role.Team && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )})
            break
            case 6:
                CPU.Target[i] = (CPU.Target.isNaN()) ? CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )}) : CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (Ind > CPU.Target[i]) != -1) ? (Ind > CPU.Target[i]) : true )})
            break
            case 7:
                CPU.Target[i] = (CPU.Target.isNaN()) ? CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (cpu.State == 0 && cpu.Role.Team != CPU.Role.Team && (Ind > CPUList.indexOf(CPU)) != -1) ? (Ind > CPUList.indexOf(CPU)) : true )}) : CPUList.findIndex((cpu, Ind) => {return (cpu.State == 0 && (cpu.State == 0 && (Ind > CPU.Target[i]) != -1) ? (Ind > CPU.Target[i]) : true )})
            break
            case 8:
                CPU.Target[i] = (CPUList.Find((Controller) => {CPUList.indexOf(Controller) == CPU.ControlledBy}).Target[1]);
            break
            case 9:

            break
            default:
            break
        }
        if (CPU.Role.Name != "Targeter") {
            if (CPU.Target[i].Props.Transported) {
                CPU.Target[i] = CPUList.indexOf(CPUList.Find((Transported) => {Transported.Props.Transported && Transported != CPU.Target[i]}))
            }
            if (CPU.Target[i].Role.Name == "Idiot" && CPU.Target[i].Props.Alert) {
                CPU.Target[i] = CPU.Target[i].Target[0];
            }
            if (CPU.Target[i].Props.Secured) {
                CPU.Target[i] = CPUList.indexOf(CPUList.Find((SecurityGuard) => {SecurityGuard.Role.Name == "Security Guard"}))
            }
        }
    if (Visiting && CPU.Role.Target[i] != 9)
    // Husk Rampage, Idiot, Anarchist, Jailor, Døde folk, Ambusher, Crusader
    {
        if (CPU.Target[i].Role.Name == "Veteran" && CPU.Target[i].Props.Alert && CPU.role.AttackVal <= 4)
        {
            Attack(CPU.Target[i], CPU, true)
            
        }
        else if (CPU.Target[i].Role.Name == "Poisoner" && GlobalMods.PosionerSaver && CPU.role.AttackVal <= 4 && CPU.Role.Hunter != "Poisoners")
        {
            Attack(CPUList.Find((PoisonerSaverProtect) => {PoisonerSaverProtect.Role.Name == "Poisoner Saver"}), CPU, true);
            
        }
        else if (CPU.Target[i].Team == "Creators" && CPU.Target[i].Role.Name != "Snorre" && GlobalMods.Snorre && CPU.Role.RoleblockImmune && CPU.Role.Hunter != "Creators")
        {
            Roleblock(CPUList.Find((PoisonerSaverProtect) => {PoisonerSaverProtect.Role.Name == "Snorre"}), CPU)
            
        }
        else if (CPU.Target[i].Role.Name == "Pestilence" && CPU.Role.Hunter != "Pestilence" && CPU.Role.AttackVal <= 6)
        {
            Attack(CPU.Target[i], CPU, true)
            
        }
        else if (CPU.Target[i].Role.Name == "Werewolf" && CPU.Role.Hunter != "Werewolves" && CPU.Role.AttackVal <= 4 && CPU.Target[i].Props.Alert)
        {
            Attack(CPU.Target[i], CPU, true)
            
        }
        else if (CPU.Target[i].Role.Name == "Elias" && CPU.Role.Hunter != "Creators" && CPU.Role.AttackVal <= 5 && CPU.Target[i].Role.CountDown == 0)
        {
            Attack(CPU.Target[i], CPU, true)
            
        }
        else if (CPU.Target[i].Role.Name == "Suicide Bomber" && CPU.Target[i].Props.Alert)
        {
            Attack(CPU.Target[i], CPU, true)
        }
        else if (CPU.Target[i].Props.Ambushed && CPU.Role.Team != "Mafia"){
            Attack(CPUList.Find((AmbusherAmbush) => {AmbusherAmbush.Role.Name == "Ambusher"}), CPU, true)
            CPU.Target[i].Props.Ambushed = false;
            if (CPU.State != 1) return;
        }
        else if (CPU.Target[i].Props.Thralled && CPU.Role.Team != "Vampire"){
            Attack(CPUList.Find((AmbusherAmbush) => {AmbusherAmbush.Role.Name == "Frenzied Thrall"}), CPU, true)
            if (CPU.State != 1) return;
        }    
        else if (CPU.Target[i].Props.Crusaded && CPU.Role.AttackVal <= 4){
            Attack(CPUList.Find((CrusaderProtect) => {CrusaderProtect.Role.Name == "Crusader"}), CPU, true)
            CPU.Target[i].Props.Crusaded = false;
        }
        else if (CPU.Target[i].Role.Hunter == CPU.Target[i].Team){
            Attack(CPU, CPU.Target[i], true, false)
        }
        else return
    if (CPU.Role.Name != "Targeter")
    {
        CPU.Target[i] = null
    }
    }
    
}
}
function Promote() {

        if (!(CPUList.some((cpuEntry) => {
            return (cpuEntry.Role.Name == "King" && cpuEntry.State == 0)
        }))) {
            CPUList.find((FoundCPU) => {
                return FoundCPU.Role.Name == "Lifeguard 1" && cpuEntry.State == 0
            }).Role = RoleList.find((roleByName) => {
                return roleByName.Name == "King"
            })
        }

        if (!(CPUList.some((cpuEntry) => {
            return (cpuEntry.Role.Name == "Queen" && cpuEntry.State == 0)
        }))) {
            CPUList.find((FoundCPU) => {
                return FoundCPU.Role.Name == "Lifeguard 2" && cpuEntry.State == 0
            }).Role = RoleList.find((roleByName) => {
                return roleByName.Name == "Queen"
            })
        }

        if (!(CPUList.some((cpuEntry) => {
            return (cpuEntry.Role.Name == "Mayor" && cpuEntry.State == 0)
        }))) {
            CPUList.find((FoundCPU) => {
                return FoundCPU.Role.Name == "Mayorguarder" && cpuEntry.State == 0
            }).Role = RoleList.find((roleByName) => {
                return roleByName.Name == "Bodyguard"
            })
        }   

        if (!(CPUList.some((cpuEntry) => {
            return (cpuEntry.Role.Team == "Vampires" && cpuEntry.State == 0)
        }))) {
            CPUList.find((FoundCPU) => {
                return FoundCPU.Role.Name == "Vampire Hunter" && cpuEntry.State == 0
            }).Role = RoleList.find((roleByName) => {
                return roleByName.Name == "Vigilante"
            })
        }

        if (!(CPUList.some((cpuEntry) => {
            return (cpuEntry.Role.Team == "Creators" && cpuEntry.State == 0)
        }))) {
            CPUList.find((FoundCPU) => {
                return FoundCPU.Role.Name == "Creator Hunter" && cpuEntry.State == 0
            }).Role = RoleList.find((roleByName) => {
                return roleByName.Name == "Villager"
            })
        }

        PromLists.forEach(PromArr => {
            switch (PromArr[0]) {
                case("Mafioso"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Godfather" || cpu.Role.Name == "Murderer") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Crazy"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Crazy King" || cpu.Role.Name == "Targeter") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Herman"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Token" || cpu.Role.Name == "Assassin Dog") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Knight"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Archer") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Soldier"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Sniper" || cpu.Role.Name == "Tankman") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Serial Killer"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Daylight Killer" || cpu.Role.Name == "Nikkiller") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Terrorist"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Grenadethrower") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Vampire"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Dracula") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                case("Werewolf"):
                    if(CPUList.every((cpu) => {
                        return !((cpu.Role.Name == "Jailwolf" || cpu.Role.Name == "Werepup") && cpu.State == 0)
                    })) {
                        CyclePromArray(PromArr)
                    }
                break;
                default:
                    CyclePromArray(PromArr)
            }
        });        
}

function CyclePromArray(Arr) {
    Arr.forEach(roleName => {
        if (CPUList.some( (cpu) => {
            return (cpu.Role.Name == roleName && cpu.state == 0 && (cpu.Role.Hunter == "" || CPUList.some((ListCPU) => {return (ListCPU.Role.Team == cpu.Role.Hunter && ListCPU.State == 0)})))
        })) {
            CPUList[CPUList.indexOf(cpu)].Role = RoleList[RoleList.find((role) => {
                return role.Name == Arr[0];
            })]
        }
        return;
    });
}

function Attack(Attacker, Target, FromVisit = false, Votable = true) {
    let AttackVal = Attacker.Role.Attack;
    let ImmuneVal = Target.Immunity;
    let BaseImmuneVal = Target.Role.Immunity;
    if (Attacker.Role.Hunter == Target.Role.Team) {
        AttackVal = 7
    } else if (Attacker.Role.Name == "Hunter Hunter" && Target.Role.Hunter != "") {
        AttackVal = 7
    }
    else if (Target.Role.Hunter == Attacker.Role.Team) {
        Attack(Target, Attacker, true, false);
        return
    }
    if (FromVisit) {
        if (Target.ProtectedBy == -1) {
            if (AttackVal > ImmuneVal) {
                Target.State = 1
            }
        } else if (AttackVal > Math.max(Target.HealedAmount, BaseImmuneVal)) {
            Target.State = 1
        }
    } else if (Target.ProtectedBy == -1) {
        if (AttackVal > ImmuneVal && TestProperties(Attacker, Target)) {
            Target.State = 1
        }
    } else if (AttackVal > ImmuneVal && TestProperties(Attacker, Target)) {
        Target.State = 1
    } else {
        Attack(Attacker, CPUList[Target.ProtectedBy], true)
        Attack(CPUList[Target.ProtectedBy], Attacker, true)
    }
    if (Target.State == 1) {
        switch(Target.Role.Name) {
            case("Nighter" || "Jester" || "Magicmaker" || "Revengetaker"):
                Attack(Target, Attacker, true)
            break;
            case("Nightmare"):
                NightmareTrigger = true;
            break;
            case("Haunter"):
                Attack(Target, Target.Target[0])
            break;
            case("FBI"):
                let newArr = CPUList.slice(0, CPUList.indexOf(Target))
                let endArr = CPUList.slice(CPUList.indexOf(Target)+1)
                let fullArr = endArr.concat(newArr)
                let PotentialTarget = CPUList.indexOf(fullArr.find((CpU) => {return CpU.Role.Team != "Town" && CpU.Role.Team != "FBI" && CpU.Role.Team != "Police" && CpU.Role.Team != "Combo" && CpU.State == 0}))
                if (PotentialTarget != -1) {
                    Attack(Target, PotentialTarget)
                }
            break;
            case("Godfather"):
                let Mafioso = CPUList.find((cPu) => {return cPu.Role.Name == "Mafioso"})
                if (Mafioso != undefined) {
                    Mafioso.Role = RoleList[RoleList.FindIndex((Ind) => {
                        return Ind.Name == "Godfather";
                    })]
                }
            break;
            case("Crazy King"):
                let Crazy = CPUList.find((cPu) => {return cPu.Role.Name == "Crazy"})
                if (Crazy != undefined) {
                    Crazy.Role = RoleList[RoleList.FindIndex((Ind) => {
                        return Ind.Name == "Crazy King";
                    })]
                }
            break;
        }
    }
}