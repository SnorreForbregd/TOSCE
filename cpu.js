class CPU {
    constructor(
        role,
        relativeTargetPos,
        state = 0,
        props = new Props()
    ) {
        this.Role = role;
        this.DoneAction = 0;
        this.Target = relativeTargetPos;
        this.State = state;
        this.Props = props;
    }
}