if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    print(hash(tuple(integer_list))) 


#Given code is for python 2 - in py3 hash() generates different value
