function NightActionFunc(CPUList, NightActionList) {
    let UpdatedNightActionList = NightActionList.filter((NightAction) => {CPUList.some((Cpu) => {Cpu.Role.Name == NightAction})})
    UpdatedNightActionList.forEach(entry => {
        switch(entry) {
            case "Sheriff":
                //Sheriff nightaction
            break;
            case "Werewolf":
                //Werewolf nightaction
            break;
            //Resten av cases
            default:
            break;
        }
    });
}