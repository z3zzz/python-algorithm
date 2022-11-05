'''
hashmap: 숫자 key와 숫자 string key는 다름 ('1' 말고 1)
격자이동 거리: x 차이 절대값 + y 차이 절대값
'''
def solution(numbers, hand):
    keypads = {
            1: (0,0), 2: (0,1), 3: (0,2), 
            4: (1,0), 5: (1,1), 6: (1,2), 
            7: (2,0), 8: (2,1), 9: (2,2), 
            '*': (3,0), 0: (3,1), '#': (3,2), 
            }

    cur_left = '*'
    cur_right = '#'
    
    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            cur_left = n
        elif n in [3, 6, 9]:
            answer += 'R'
            cur_right = n
        else:
            dist_left = abs(keypads[n][0] - keypads[cur_left][0]) + abs(keypads[n][1] - keypads[cur_left][1]) 
            dist_right = abs(keypads[n][0] - keypads[cur_right][0]) + abs(keypads[n][1] - keypads[cur_right][1]) 
            # print(n, cur_left, cur_right, dist_left, dist_right)

            if dist_left < dist_right:
                answer += 'L'
                cur_left = n
            elif dist_left > dist_right:
                answer += 'R'
                cur_right = n
            else:
                if hand == "right":
                    answer += 'R'
                    cur_right = n
                else:
                    answer += 'L'
                    cur_left = n

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
