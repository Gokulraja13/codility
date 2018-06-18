def solution(Number):
    Binary_string = '{0:b}'.format(Number)
    print(Binary_string)
    count = 0
    Global_count = 0
    length = len(Binary_string)
    for i in range(length):
        if (Binary_string[i] == '0'):
            count = count + 1
        else:
            if(count > Global_count):
                Global_count = count
            count = 0
    print(Global_count)
