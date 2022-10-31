'''
s = s.replace 로 해야 함
original string은 immutable

'''
def solution(s):
    dictl = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for key, value in dictl.items():
        s = s.replace(key, value)

    return int(s)

print(solution("one4seveneight"))
