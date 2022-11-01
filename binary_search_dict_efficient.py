'''
O(mn) -> m 을 가지고 data structure(hash table 등) 만든 후, O(n) 처리
숫자 비교(점수 일정 이상 등) -> binary search (중간 시작, l, r 조정)
binary search 하려면 일단 sort 해야
dict().setdefault((a,b,c,d), value) -> key로 튜플 가능

array.sort()는 1번만 진행하도록 위치 잘 둬야 함
for loop 등에 두면 무의미한 반복임

dict의 value가 array인 경우, key가 동일하게 반복할 수 있는데, 그 때마다 sort하면 무의미함

'''

def solution(infos, querys):
    answer = []

    scores = dict()
    for a in ["cpp", "java", "python", "-"]:
        for b in ["backend", "frontend", "-"]:
            for c in ["junior", "senior", "-"]:
                for d in ["chicken", "pizza", "-"]:
                    scores.setdefault((a, b, c, d), list())

    for info in infos:
        info = info.split()
        for a in [info[0], "-"]:
            for b in [info[1], "-"]:
                for c in [info[2], "-"]:
                    for d in [info[3], "-"]:
                        scores[(a,b,c,d)].append(int(info[4]))

    for key in scores:
        scores[key].sort()
    
    for query in querys:
        query = query.split()
        key = (query[0], query[2], query[4], query[6])
        criteria = int(query[7])

        candidates = scores[key]

        l, r = 0, len(candidates)

        while l < r:
            m = (l + r) // 2
            if candidates[m] < criteria:
                l = m + 1
            else:
                r = m

        answer.append(len(candidates) - l)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
