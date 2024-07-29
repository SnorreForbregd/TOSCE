function NightActionFunc(CPUList, NightActionList) {
    let UpdatedNightActionList = NightActionList.filter((NightAction) => {CPUList.some((Cpu) => {Cpu.Role.Name == NightAction})})
    UpdatedNightActionList.forEach(entry => {
        let CPU = CPUList.Find((cpu) => {cpu.Role.Name == entry})
        switch(entry) {
        //Target(CPU, Attacking = true, Visiting = true)
        //Attack(Attacker, Target, FromVisit = false, Votable = true, Ranged = false, Shooting = false)
            case "Bodyguard":
                if (CPU.Props.Roleblocked == false){
                    if (CPU.Role.Countdown == 1){
                        CPU.Props.Bulletproof = true
                        CPU.Role.Countdown = 0
                    }
                    else {
                        (Target(CPU, false))
                        if (CPU.Target[0].Props.Jailed == false){
                            CPU.Target[0].Role.Immunity = CPU.Role.TargetImmunity
                            CPU.Target[0].ProtectedBy = CPUList.indexOf(CPU)
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
            case "Sheriff":
                //Sheriff nightaction
            break;
            case "Werewolf":
                //Werewolf nightaction
            break;
            case "Johannes":
                
                // Fordi visiting-parameteret sin default er true og er optional,
                // Trenger vi ikke skrive inn den for besøkende roller
                Target(CPU, true);

                // siden alle default parameter er korrekte for johannes, trenger vi ikke skrive de inn
                Attack(CPU, CPU.Target);
            break;
            //Resten av cases
            default:
            break;
        }
    });
}