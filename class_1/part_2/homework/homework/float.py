x = float(input('input a decimal number:'))
p = 0
while ((2**p)*x)%1 != 0:
    print('Reminder = '+str(((2**p)*x)-int((2**p)*x)))
    p+=1
num = int((2**p)*x)
result = ''
if num == 0:
    result = '0'
while num>0:
    result = str(num%2)+ result
    num = num//2
for i in range(p-len(result)):
    result = '0'+ result
print('the binary is '+ result[0:-p] + '.'+result[-p:])


