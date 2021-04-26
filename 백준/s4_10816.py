import sys
import collections

input = sys.stdin.readline

n = int(input())
have_card = list(map(int, input().split()))
m = int(input())
do_you_have = list(map(int, input().split()))


result = []
# Sol 1
have_card = collections.Counter(have_card)

# print(have_card[-5])
for card in do_you_have:
    result.append(have_card[card])

for r in result:
    print(r, end=' ')
