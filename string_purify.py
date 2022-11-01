import re

def solution(new_id):
    st = new_id
    st = st.lower()
    # a-z, 0-9, -, _, . 뺴고 삭제
    st = re.sub('[^a-z0-9\-_.]', '', st)
    # . 1개 이상 반복 -> . 치환
    st = re.sub('\.+', '.', st)
    # . 시작, . 끝 제거
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]

    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("=.="))
