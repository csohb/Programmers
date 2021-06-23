
def solution(phone_book):
    '''
        문자열 배열이기 때문에 존재하는지 안하는지 생각해보면 됨
        in, not in 
    '''
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        else:
            return True
            
def solution2(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True