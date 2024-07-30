function NightActionFunc(CPUList, NightActionList) {
    let UpdatedNightActionList = NightActionList.filter((NightAction) => {CPUList.some((Cpu) => {Cpu.Role.Name == NightAction})})
    UpdatedNightActionList.forEach(entry )=>{
        let CPU = CPUList.Find((cpu) => {cpu.Role.Name == entry})
        switch(entry) {
        //Target(CPU, Attacking = true, Visiting = true)
        //Attack(Attacker, Target, FromVisit = false, Votable = true, Ranged = false, Shooting = false)
            case "Bodyguard":
                if (CPU.Props.Action != 0){
                    if (CPU.Props.Action == 1){
                        if (CPU.Props.Roleblocked == false){
                            if (CPU.Role.Countdown == 1){
                                 CPU.Props.Bulletproof = true
                                 CPU.Role.Countdown = 0
                                 CPU.Props.Action = 0
                                 break;
                            }
                            else {
                                CPU.Props.Action = 2
                                break;
                            }
                        }
                        else {
                            CPU.Props.Action = 0
                            break;
                        }
                    }
                    else {
                        if (CPU.Props.Roleblocked == false){
                            (Target(CPU, false))
                            if (CPU.Target[0].Props.Jailed == false){
                                CPU.Target[0].Role.Immunity = CPU.Role.TargetImmunity
                                CPU.Target[0].ProtectedBy = CPUList.indexOf(CPU)
                            }
                        }
                    }
                }
            break;
            case "Crusader":
                if (CPU.Props.Roleblocked == false){
                    Target(CPU, false)
                    if (CPU.Target[0].Props.Jailed == false){
                        CPU.Target[0].Props.Crusaded = true
                    }
                }
            break;
            case "Doctor":
                if (CPU.Props.Roleblocked == false){
                    if (CPU.Role.Countdown == 1) {
                        CPU.HealedAmount = 6
                        CPU.Immunity = 6
                        CPU.Role.Countdown = 0
                    }
                    else {
                        Target(CPU, false)
                        if (CPU.Target[0].Props.Jailed == false){
                            CPU.Target[0].HealedAmount = 6
                            CPU.Target[0].Immunity = 6
                        }
                    }
                }
            break;
            case "Sheriff":
                //Sheriff nightaction
            break;
            case "Werewolf":
                //Werewolf nightaction
            break;
            case "Johannes":
                if (CPU.Props.Roleblocked == false && GlobalMods.Nightmare == false){
                    Target(CPU, true);
                    Attack(CPU, CPU.Target);
                }
            break;
            //Resten av cases
            default:
            break;
        }
    }
}
