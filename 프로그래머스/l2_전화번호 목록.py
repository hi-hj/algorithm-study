def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):

        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
        



solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])