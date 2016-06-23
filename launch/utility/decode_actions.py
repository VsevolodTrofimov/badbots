def decode(commands):
    act = []
    for i in range(15):
        act.append(False)

    if "forward" in commands:
        act[0] = True

    if "backward" in commands:
        act[1] = True

    if "strife_left" in commands:
        act[2] = True

    if "strif_right" in commands:
        act[3] = True

    if "turn_left" in commands:
        act[4] = True

    if "turn_right" in commands:
        act[5] = True

    if "attack" in commands:
        act[6] = True

    if "weapon_1" in commands:
        act[7] = True

    if "weapon_2" in commands:
        act[8] = True

    if "weapon_3" in commands:
        act[9] = True

    if "weapon_4" in commands:
        act[10] = True

    if "weapon_5" in commands:
        act[11] = True

    if "weapon_6" in commands:
        act[12] = True

    if "weapon_0" in commands:
        act[13] = True

    if "use" in commands:
        act[14] = True
    print("decoded", commands, act)
    return act
