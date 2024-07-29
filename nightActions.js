function NightActionFunc(CPUList, NightActionList) {
    let UpdatedNightActionList = NightActionList.filter((NightAction) => {CPUList.some((Cpu) => {Cpu.Role.Name == NightAction})})
    UpdatedNightActionList.forEach(entry => {
        let CPU = CPUList.Find((cpu) => {cpu.Role.Name == entry})
        switch(entry) {
        //Target(CPU, Attacking = true, Visiting = true)
        //Attack(Attacker, Target, FromVisit = false, Votable = true, Ranged = false, Shooting = false)
            case "Bodyguard":
                
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