class Role {
    constructor(name, team, type, attack, immunity, targetImmunity, target, countdown, roleblockimmune, rage, controlimmune, controleffectimmune, unique) {
        this.Name = name;
        this.Team = team;
        this.Type = type; //Killing, Protective, Investigative, Support, Deception, Evil, Benign, Chaos
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
    }
}