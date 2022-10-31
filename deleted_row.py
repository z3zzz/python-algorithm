def apply_command(cmd, cur, deleted, deleted_stack, n, bottom):
    if len(cmd) == 3:
        cmd_type, amount = cmd.split()
        amount = int(amount)
    else:
        cmd_type = cmd

    if cmd_type == "U":
        while amount > 0:
            cur -= 1

            if not deleted[cur]:
                amount -= 1

    if cmd_type == "D":
        while amount > 0:
            cur += 1
            if not deleted[cur]:
                amount -= 1

    if cmd_type == "C":
        deleted[cur] = True
        deleted_stack.append(cur)

        if cur == bottom:
            while deleted[cur]:
                cur -= 1
            bottom = cur
        else:
            while deleted[cur]:
                cur += 1

    if cmd_type == "Z":
        restored = deleted_stack.pop()
        deleted[restored] = False

        if restored > bottom:
            bottom = restored

    return cur, bottom

def solution(n, k, cmds):
    answer, cur, deleted, deleted_stack, bottom = "O"*n, k, {x: False for x in range(n)}, [], n - 1
    
    for cmd in cmds:
        cur, bottom = apply_command(cmd, cur, deleted, deleted_stack, n, bottom)

    for d in deleted_stack:
        answer = answer[:d] + "X" + answer[d + 1:]

    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
