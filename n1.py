example_01 = "abcdedcba" # TRUE
example_02 = "abcddbab" # FALSE


def check_palindrome(example:str):
    # SOL 3
    if len(example)<=1: return True
    if example[0] != example[-1]: return False
    return check_palindrome(example[1:-1])
    
    # SOL 2 
    for i in range(len(example)//2): # 0  -1 / 1 -2 / 2 -3/
        if example[i]!=example[-i-1]:
            return False
    return True

    # SOL1
    return example[:]==example[::-1]

print(check_palindrome(example_01))
print(check_palindrome(example_02))