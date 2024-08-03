class Role {
    constructor(name, team, hunter, type, suspicious, attack, immunity, targetImmunity, target, countdown, roleblockimmune, rage, controlimmune, controleffectimmune, unique, good) {
        this.Name = name;
        this.Team = team;
        this.Hunter = hunter;
        this.Type = type; //Killing, Protective, Investigative, Support, Deception, Evil, Benign, Chaos, Hunting
        this.Suspicious = suspicious
        this.Attack = attack;
        this.Immunity = immunity;
        this.TI = targetImmunity;
        this.Target = target;
        this.CountDown = countdown;
        this.RoleblockImmune = roleblockimmune
        this.Rage = rage;
        this.ControlImmune = controlimmune
        this.ControlEffectImmune = controleffectimmune
        this.Unique = unique
        this.Good = good
    }
}