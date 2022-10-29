'''
k진수로 바꾸기: '' += str(n % k ) while n//k > 0 -> reverse [::-1]

'''
def convert(n, k):
    if (k == 10):
        return str(n)

    result = ''
    while n:
        result += str(n % k)
        n //= k
    
    return result[::-1]

def is_prime(n):
    if n == 1: return False

    i = 2

    while (i*i <= n):
        if n % i == 0: return False
        i += 1
    return True


def solution(n, k):
    k_base = convert(n, k)
    nums = k_base.split("0")
    answer = 0
    print(nums)
    for num in nums:
        if not num:
            continue
        if is_prime(int(num)):
            answer += 1

    return answer

print(solution(437674, 3))