T = int(input())

for tc in range(1, T+1):
    D, N, K = map(int, input().split())
    festival = [[] for _ in range(D+1)]

    print(D,N,K, festival)