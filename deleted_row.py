def apply_command(cmd, cur, deleted, deleted_stack, n, top, bottom):
    if len(cmd) == 3:
        cmd_type, amount = cmd.split()
        amount = int(amount)
    else:
        cmd_type = cmd

    if cmd_type == "U":
        while amount > 0 and cur > top:
            if not deleted[cur-1]:
                cur -= 1
            else:
                cur -= 2
            amount -= 1

        cur = max(cur, top)

    if cmd_type == "D":
        while amount > 0 and cur < bottom:
            if not deleted[cur+1]:
                cur += 1
                amount -= 1
            else:
                cur += 2
                amount -= 1

        cur = min(cur, bottom)

    if cmd_type == "C":
        deleted[cur] = True
        deleted_stack.append(cur)
        cur += 1

        while deleted[cur] and cur < n:
            cur += 1

        cur = min(cur, n - 1)

    if cmd_type == "Z":
        restored = deleted_stack.pop()
        deleted[restored] = False

    return cur

def solution(n, k, cmds):
    answer, cur, deleted, deleted_stack = "O"*n, k, {x: False for x in range(n)}, []
    
    for cmd in cmds:
        cur = apply_command(cmd, cur, deleted, deleted_stack, n, 0, n-1)

    for d in deleted_stack:
        answer = answer[:d] + "X" + answer[d + 1:]

    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
