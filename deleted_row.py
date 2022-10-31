'''
self.prev 혹은 next 로 나아갈때는 일단 self.prev나 next 존재여부 if로 확인
bottom 여부는 self.next 존재 여부로 판단 가능하므로 굳이 저장 안해도 됨. root만 중요
삭제한 최신 순부터 복구하기 때문에 문제가 복잡하지 않아짐
cmd 길이가 마음대로 "C 3" 으로 길이 3이라고 생각하면 안 됨 "C 10"도 가능함

string 인덱스 변환 시 s[:n] + "새 문자열" + s[n+1:] 방식은 1번 당 시간 O(n)
따라서 string 대신 각 문자로 이루어진 배열 사용 -> 마지막에 "".join 사용

'''

class LinkedList:
    class Node:
        def __init__(self, n, prev):
            self.n = n
            self.prev = prev
            self.next = None

    def __init__(self, n, k):
        self.root = self.Node(0, None)
        self.current = None
        self.deleted_stack = []
        self.temp = self.root

        for i in range(1, n):
            new_node = self.Node(i, self.temp)
            self.temp.next = new_node
            if i == k:
                self.current = new_node
            self.temp = new_node

    def up(self, x):
        for _ in range(x):
            if self.current.prev:
                self.current = self.current.prev
    def down(self, x):
        for _ in range(x):
            if self.current.next:
                self.current = self.current.next

    def delete(self):
        delete_node = self.current
        self.deleted_stack.append(delete_node)
        if delete_node.next:
            if delete_node.prev:
                delete_node.prev.next = delete_node.next
            delete_node.next.prev = delete_node.prev
            self.current = delete_node.next
            if delete_node == self.root:
                self.root = delete_node.next
        else:
            self.current = delete_node.prev
            self.current.next = None

    def restore(self):
        restore_node = self.deleted_stack.pop()
        if restore_node.prev:
            restore_node.prev.next = restore_node
        if restore_node.next:
            restore_node.next.prev = restore_node
            if restore_node.next == self.root:
                self.root = restore_node
    
    def get_root(self):
        return self.root
    
    def get_deleted(self):
        return self.deleted_stack

def solution(n, k, cmds):
    chart = LinkedList(n, k)
    
    for cmd in cmds:
        if cmd[0] == "U":
            chart.up(int(cmd.split()[1]))
        if cmd[0] == "D":
            chart.down(int(cmd.split()[1]))
        if cmd[0] == "C":
            chart.delete()
        if cmd[0] == "Z":
            chart.restore()

    deleted_stack = chart.get_deleted()

    answer = ["X"] * n

    node = chart.get_root()

    while node:
        answer[node.n] = "O"
        node = node.next

    return "".join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
