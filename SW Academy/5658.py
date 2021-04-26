import sys
import collections
input = sys.stdin.readline

test_case = int(input())

for t in range(test_case):
    n, k = map(int, input().split())
    nums = input().strip()
    result  = []
    # n//4 번 만큼 회전
    for i in range(n//4):
        result.append(int(''.join(nums[0:n//4]), 16))
        result.append(int(''.join(nums[n//4:n//2]), 16))
        result.append(int(''.join(nums[n//2:n//4*3]), 16))
        result.append(int(''.join(nums[n//4*3:]), 16))

        last = nums[-1]
        nums = last + nums[:-1]
    
    result = list(set(result))
    result.sort(reverse= True)

    print('#%d %d' %(t+1, result[k-1]))


