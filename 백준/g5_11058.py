n = int(input())

key = [i for i in range(101)]
for i in range(6, 101):
    key[i] = key[i-1] + 1    
    key[i] = max(key[i-3]*2, key[i-4]*3, key[i-5]*4)
print(key[n])