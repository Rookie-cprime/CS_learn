"""
write a program  that prints the longest substring of s
 in which the letters occur in alphabetical order.
"""

    s = str(input('please type a string:'))
    j = ' '
    temp = ''
    result = ''
    for i in s:
        if(j == ' '):
            temp = temp+i[:]
        elif(i>=j):
            temp = temp + i[:]
        else:
            if(result == ''):
                result = temp[:]
                temp = i[:]
            elif(len(result)<len(temp)):
                result = temp[:]
                temp = i[:]
            else:
                temp = i[:]
        j = i[:]

    print(result)
