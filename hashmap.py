'''
set 쓰면 array에서 중복 걸러짐
dictionary 1줄 생성

'''


def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list} # dictionary 1줄 생성 
    
    for r in set(report):
        reports[r.split()[1]] += 1
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer


def solution(id_list, report, k):
    reportMap = {}
    for pair in report:
        reporter, reportee = pair.split(" ")
        reporters = reportMap.get(reportee)
        if reporters:
            if reporter in reporters:
                continue
            else:
                reporters.append(reporter)
        else:
            reportMap[reportee] = [reporter]
    
    resultMap = {}
    for reportee, reporters in reportMap.items():
        if len(reporters) >= k:
            for reporter in reporters:
                resultMap[reporter] = resultMap.get(reporter, 0) + 1
    
    answer = []
    
    for id in id_list:
        answer.append(resultMap.get(id, 0))

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
2))
